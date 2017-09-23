# -*- coding: utf-8 -*-

from flask_restful import Resource, reqparse
from flask_login import current_user, login_required
from red_packet.models.packet import RedPacket
from red_packet.core.errors import ApiError

parser = reqparse.RequestParser()
parser.add_argument('token', required=True)

code_map = {
    403: ApiError.share_get_forbidden
}


class NewShareAPI(Resource):

    method_decorators = [login_required]

    def post(self):
        args = parser.parse_args()
        red_packet = RedPacket.get_by_token(args.token)
        if not red_packet:
            raise ApiError(ApiError.red_packet_not_found)

        share, code = red_packet.next_share(current_user)
        if code == 0:
            return share.as_dict()
        else:
            raise ApiError(code_map.get(code, 403))

