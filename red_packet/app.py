# -*- coding: utf-8 -*-

import os
from flask import Flask, g, jsonify
from red_packet.core.extensions import (db, migrate, login_manager,
                                        cache)
from red_packet.api import v1
from red_packet.core.errors import ApiError


def create_app(Mode='Development'):
    app = Flask('red_packet')
    if os.getenv('RED_PACKET_PRODUCTION'):
        Mode = 'Production'
    app.config.from_object('red_packet.settings.%sConfig' % Mode)

    configure_blueprints(app)
    configure_extensions(app)
    configure_errorhandlers(app)

    return app

def configure_after_request(app):
    def rollback(response):
        db.session.rollback()

    app.after_request(rollback)

def configure_blueprints(app):
    for m in (v1, ):
        app.register_blueprint(m.blueprint)

def configure_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    cache.init_app(app)

def configure_errorhandlers(app):

    @app.errorhandler(ApiError)
    def api_error_handler(error):
        response = jsonify(error.as_dict())
        response.status_code = error.status_code
        return response

