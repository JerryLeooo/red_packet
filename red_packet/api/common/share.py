# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask_login import current_user, login_required
from red_packet.models.packet import RedPacket
from red_packet.models.share import Share
from red_packet.core.errors import ApiError


class NewShareAPI(Resource):

    method_decorators = [login_required]

    def post(self, token):
        red_packet = RedPacket.get_by_token(token)
        if not red_packet:
            raise ApiError(ApiError.red_packet_not_found)

        share = red_packet.get_next_share(current_user)
        return share.as_dict(), 201

