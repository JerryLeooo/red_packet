# -*- coding: utf-8 -*-

from red_packet.core.extensions import db


class CRUDMixin(object):

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.iteritems():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        db.session.add(self)
        if commit == True:
            db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self

class SurrogatePK(object):

    id = db.Column(db.Integer, primary_key=True)

    @classmethod
    def get_by_id(cls, id):
        if any(
            (isinstance(id, basestring) and id.isdigit(),
             isinstance(id, (int, float))),
        ):
            return cls.query.get(int(id))
        return None

class DateMixin(object):
    date_created = db.Column(
        'date_created', db.DateTime(timezone=True),
        server_default=db.func.current_timestamp(),
        nullable=False, index=True)
    date_updated = db.Column(
        'date_updated', db.DateTime(timezone=True),
        server_default=db.func.current_timestamp(),
        nullable=False, index=True)
