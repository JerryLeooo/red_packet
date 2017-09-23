# -*- coding: utf-8 -*-

from red_packet.core.database import db, CRUDMixin, SurrogatePK


class User(db.Model, CRUDMixin, SurrogatePK):

    __tablename__ = 'user'

    username = db.Column(db.Text, nullable=False)

    def get_own_credits(self):
        pass

    # 暂未考虑分页
    def get_own_shares(self):

        from red_packet.models.share import Share

        shares = Share.query.filter_by(owner_id=self.id).all()
        return [share.as_dict() for share in shares]
