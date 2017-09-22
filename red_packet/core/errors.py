# -*- coding: utf-8 -*-

from flask import request


class ApiError(Exception):

    user_not_found             = (1001, "User not found.", 404)
    bad_parameter              = (1002, "Bad parameters.", 400)
    not_login                  = (1003, "Not login.", 401)

    answer_not_viewable        = (1004, "You can not view this answer.", 403)

    order_created_failed       = (1005, "Order created failed.", 500)
    order_not_found            = (1006, "Order not found.", 404)

    question_not_found         = (1007, "Question not found.", 404)
    question_not_viewable      = (1008, "You can not view this question.", 403)
    question_created_failed    = (1009, "Question created failed.", 500)

    settings_created_failed    = (1010, "Settings created or updated failed.", 500)
    not_supported_login_method = (1011, "Not supported login method.", 400)
    duplicated_order           = (1012, "Order has been success", 400)
    already_listener           = (1013, "Already listener", 400)

    not_your_question          = (1014, "Not your question", 403)
    unknown_error              = (1015, "Unknown error", 500)
    verify_failed              = (1016, "Verify failed", 400)
    credit_not_enough          = (1017, "Credit not enough", 403)
    iap_failed                 = (1018, "IAP failed", 500)

    def __init__(self, error_msg, extra_msg=None):
        Exception.__init__(self)
        error_code, msg, status_code = error_msg
        is_api = request and request.path.startswith("/api/")
        self.status_code = status_code if is_api else 200
        self.message = "%s (%s)" % (msg, extra_msg) if extra_msg else msg
        self.data = {
            'code': error_code,
        }

    def to_dict(self):
        rv = dict(self.data or ())
        rv['message'] = self.message
        return rv
