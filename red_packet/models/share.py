# -*- coding: utf-8 -*-

from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from red_packet.core.database import db, CRUDMixin, SurrogatePK, DateMixin

class Share(db.Model, CRUDMixin, SurrogatePK, DateMixin):

    __tablename__ = 'share'

    __table_args__ = (
        db.Index('ix_token_and_owner_id',
                 'red_packet_token', 'owner_id'),
    )

    amount = db.Column(db.Integer)
    red_packet_token = db.Column(db.String(8))
    owner_id = db.Column(db.Integer, index=True)

    @classmethod
    def get_by_token_and_owner(cls, token, owner_id):
        try:
            return cls.query.filter_by(red_packet_token=token,
                                       owner_id=owner_id).one()
        except NoResultFound:
            return None

    def as_dict(self):
        return {
            'amount': self.amount,
            'red_packet_token': self.red_packet_token,
            'owner_id': self.owner_id
        }
