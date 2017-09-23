# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask_login import current_user, login_required
from red_packet.models.user import User


class MeCreditsAPI(Resource):

    method_decorators = [login_required]

    def get(self):
        return {
            'code': 0,
            'user_id': current_user.id,
            'credits': current_user.get_own_credits()
        }

class MeShareListAPI(Resource):

    method_decorators = [login_required]

    def get(self):
        return {
            'code': 0,
            'user_id': current_user.id,
            'shares': current_user.get_own_shares()
        }
