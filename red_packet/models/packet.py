# -*- coding: utf-8 -*-

from red_packet.core.database import db, CRUDMixin, DateMixin, SurrogatePK
from red_packet.core.utils import gen_token

class RedPacket(db.Model, CRUDMixin, DateMixin, SurrogatePK):

    __tablename__ = 'red_packet'

    token = db.Column(db.String(8))
    amount = db.Column(db.Integer, nullable=False)
    count = db.Column(db.Integer, nullable=False)
    creator_id = db.Column(db.Integer, nullable=False)

    @classmethod
    def get_by_token(cls, token):
        return cls.query.get(token)

    def get_token(self):
        if self.token:
            return self.token
        else:
            token = gen_token(self.id)
            self.update(token=token)
            return token

    def as_dict(self):
        return {
            'token': self.token,
            'amount': self.amount,
            'count': self.count,
            'creator_id': self.creator_id
        }

    def next_share(self):
        return 0, 0
