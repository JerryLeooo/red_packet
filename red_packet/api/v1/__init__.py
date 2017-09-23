# -*- coding: utf-8 -*-

from flask import Blueprint
import flask_restful as restful

from red_packet.api.common.packet import NewRedPacketAPI, AllRedPacketsAPI
from red_packet.api.common.share import NewShareAPI
from red_packet.api.common.me import MeCreditsAPI, MeShareListAPI

RESOURCE_URLS = [
    ('/red_packet', NewRedPacketAPI, 'red_packet.create'),
    ('/red_packet/<token>', NewShareAPI, 'share.get'),
    ('/me/credits', MeCreditsAPI, 'me.credits'),
    ('/me/shares_got', MeShareListAPI, 'me.shares'),
    ('/red_packets', AllRedPacketsAPI, 'red_packets.list')
]

blueprint = Blueprint('api.v1', __name__, url_prefix='/api/v1')

def configure_api(blueprint):
    api = restful.Api(blueprint, catch_all_404s=True)

    for url, view, endpoint in RESOURCE_URLS:
        api.add_resource(view, url, endpoint=endpoint)

configure_api(blueprint)
