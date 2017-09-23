# -*- coding: utf-8 -*-

from red_packet.core.database import db, CRUDMixin, DateMixin, SurrogatePK
from red_packet.core.helpers import (gen_token,
                                     gen_sequence_key,
                                     gen_share_sequence)
from red_packet.core.extensions import redis_store
from red_packet.core.errors import ApiError

class RedPacket(db.Model, CRUDMixin, DateMixin, SurrogatePK):

    __tablename__ = 'red_packet'

    token = db.Column(db.String(8))
    amount = db.Column(db.Integer, nullable=False)
    count = db.Column(db.Integer, nullable=False)
    creator_id = db.Column(db.Integer, nullable=False)

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        instance = instance.save()
        instance.token = gen_token(instance.id)
        gen_share_sequence(instance.token, instance.amount, instance.count)
        return instance.save()

    @classmethod
    def get_by_token(cls, token):
        return cls.query.filter_by(token=token).one()

    def get_next_share(self, share_getter):
        from red_packet.models.share import Share

        share = Share.get_by_token_and_owner(self.token, share_getter.id)
        if share:
            raise ApiError(ApiError.share_get_forbidden)

        key = gen_sequence_key(self.token)
        share_amount = redis_store.lpop(key)
        if share_amount:
            share = Share.create(amount=share_amount,
                                 owner_id=share_getter.id,
                                 red_packet_token=self.token)
            return share
        
        raise ApiError(ApiError.red_packet_run_out)

    def as_dict(self):
        return {
            'token': self.token,
            'amount': self.amount,
            'count': self.count,
            'creator_id': self.creator_id
        }
