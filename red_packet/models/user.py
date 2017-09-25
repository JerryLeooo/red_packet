# -*- coding: utf-8 -*-

from flask_login import UserMixin
from red_packet.core.database import db, CRUDMixin, SurrogatePK
from sqlalchemy import text

class User(db.Model, CRUDMixin, SurrogatePK, UserMixin):

    __tablename__ = 'user'

    username = db.Column(db.Text, nullable=False)
    api_key = db.Column(db.Text, index=True)
    returned_credits = db.Column(db.Integer, default=0)

    def get_own_credits(self):
        sql = text("select sum(amount) "
                   "from share "
                   "where owner_id=%s" % self.id)
        result = db.engine.execute(sql)
        return int(result.fetchone()[0]) + self.returned_credits

    # 暂未考虑分页
    def get_own_shares(self):

        from red_packet.models.share import Share

        shares = Share.query.filter_by(owner_id=self.id).all()
        return shares
