# -*- coding: utf-8 -*-

from flask import Blueprint
from flask.ext import restful

from red_packet.api.common.red_packet import NewRedPacketAPI
from red_packet.api.common.share import NewShareAPI
from red_packet.api.common.me import MeCreditsAPI, MeShareListAPI

RESOURCE_URLS = [
    ('/red_packet', NewRedPacketAPI, 'red_packet.create'),
    ('/red_packet/<token>', NewShareAPI, 'share.get'),
    ('/me/credits', MeCreditsAPI, 'me.credits'),
    ('/me/shares', MeShareListAPI, 'me.shares')
]

blueprint = Blueprint('api.v1', __name__, url_prefix='/api/v1')

def configure_api(blueprint):
    api = restful.Api(blueprint)

    for url, view, endpoint in RESOURCE_URLS:
        api.add_resource(view, url, endpoint=endpoint)

configure_api(blueprint)
