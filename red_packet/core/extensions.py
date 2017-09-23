# -*- coding: utf-8 -*-

import base64
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_caching import Cache
from fakeredis import FakeStrictRedis
from werkzeug.local import LocalProxy
from os import environ
from redis import StrictRedis
from werkzeug.utils import import_string
from celery import Celery


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
cache = Cache(config={'CACHE_TYPE': 'simple'})

@login_manager.request_loader
def load_user_from_request(request):

    from red_packet.models.user import User

    # first, try to login using the api_key url arg
    api_key = request.args.get('api_key')
    if api_key:
        user = User.query.filter_by(api_key=api_key).first()
        if user:
            return user

    # next, try to login using Basic Auth
    api_key = request.headers.get('Authorization')
    if api_key:
        api_key = api_key.replace('Basic ', '', 1)
        try:
            api_key = base64.b64decode(api_key)
        except TypeError:
            pass
        user = User.query.filter_by(api_key=api_key).first()
        if user:
            return user

    # finally, return None if both methods did not login the user
    return None

def get_redis():

    from flask import current_app as app

    if app.testing:
        return FakeStrictRedis()
    else:
        return StrictRedis(
            host=environ.get("REDIS_PORT_6379_TCP_ADDR", 'localhost'),
            port=environ.get("REDIS_PORT_6379_TCP_PORT", 6379))

redis_store = LocalProxy(get_redis)

def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery