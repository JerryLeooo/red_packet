# -*- coding: utf-8 -*-

from flask import request


class ApiError(Exception):

    share_get_forbidden = (1001, "Share get foribidden", 403)
    not_found           = (1002, "Not Found", 404)
    red_packet_not_found = (1003, "Red packet not found", 404)
    red_packet_run_out = (1004, "Red packet run out", 404)

    def __init__(self, error_msg, extra_msg=None):
        Exception.__init__(self)
        error_code, msg, status_code = error_msg
        is_api = request and request.path.startswith("/api/")
        self.status_code = status_code if is_api else 200
        self.message = "%s (%s)" % (msg, extra_msg) if extra_msg else msg
        self.data = {
            'code': error_code,
        }

    def as_dict(self):
        rv = dict(self.data or ())
        rv['message'] = self.message
        return rv
