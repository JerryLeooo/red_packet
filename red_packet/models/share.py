# -*- coding: utf-8 -*-

from red_packet.core.database import db, CRUDMixin, SurrogatePK, DateMixin

class Share(db.Model, CRUDMixin, SurrogatePK, DateMixin):

    __tablename__ = 'share'

    amount = db.Column(db.Integer)
    red_packet_token = db.Column(db.String(8))
    owner_id = db.Column(db.Integer)
