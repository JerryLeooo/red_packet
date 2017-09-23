# -*- coding: utf-8 -*-

from flask_login import current_user, login_required
from flask_restful import Resource, reqparse
from red_packet.models.packet import RedPacket

parser = reqparse.RequestParser()
parser.add_argument('total_amount', required=True)
parser.add_argument('count', required=True)

class NewRedPacketAPI(Resource):

    method_decorators = [login_required]

    def post(self):
        args = parser.parse_args()
        red_packet = RedPacket.create(
            total_amount=args.total_amount,
            count=args.count,
            creator_id=current_user.id
        )
        return red_packet.as_dict()

# 调试用
class AllRedPacketsAPI(Resource):

    def get(self):
        red_packets = RedPacket.query.all()
        return [p.as_dict() for p in red_packets]