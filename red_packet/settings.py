# -*- coding: utf-8 -*-

import os
import sys

_VERSION_STR = '{0.major}{0.minor}'.format(sys.version_info)


class DefaultConfig(object):

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    DEBUG = True
    TESTING = False

    SEND_LOGS = False

    INFO_LOG = "info.log"
    ERROR_LOG = "error.log"

    database_url = os.getenv("DATABASE_URL", None)
    if database_url:
        SQLALCHEMY_DATABASE_URI = database_url
    else:
        SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s:%s/%s' % (
            os.getenv('POSTGRESQL_USERNAME', 'leo'),
            os.getenv('POSTGRESQL_PASSWORD', '1iuyang'),
            os.getenv('POSTGRESQL_PORT_5432_TCP_ADDR', 'localhost'),
            os.getenv('POSTGRESQL_PORT_5432_TCP_PORT', '5432'),
            os.getenv('POSTGRESQL_INSTANCE_NAME', 'postgres'))

    SQLALCHEMY_ECHO = False

    redis_url = os.getenv("REDIS_URL", None)
    if redis_url:
        REDIS_URL = redis_url
    else:
        REDIS_URL = "redis://:%s@%s:%s/0" % (
            os.getenv("REDIS_PASSWORD", ''),
            os.getenv("REDIS_PORT_6379_TCP_ADDR", 'localhost'),
            os.getenv("REDIS_PORT_6379_TCP_PORT", 6379))

    SQLALCHEMY_ECHO = False

    SERVER_NAME = os.getenv('RED_PACKET_SERVER') or 'r.instask.me:8888'
    SECRET_KEY = 'secret key'

    CACHE_TYPE = "simple"
    CACHE_DEFAULT_TIMEOUT = 60

    SECRET_KEY = "dsafasfawt23"

class DevelopmentConfig(DefaultConfig):
    pass

class TestingConfig(DefaultConfig):
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        'sqlite://'
    )

class ProductionConfig(DefaultConfig):
    TESTING = False
    DEBUG = os.getenv("RED_PACKET_PRODUCTION", True)
    SECRET_KEY = "SecretKeyForSessionSigning"
    ADMINS = ["whilgeek@gmail.com"]
