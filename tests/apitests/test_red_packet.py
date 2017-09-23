# -*- coding: utf-8 -*-

import json
from flask import url_for

def test_create_red_packet(app, packet_creator):

    with app.test_client() as c:
        res = c.post(
            url_for('api.v1.red_packet.create'),
            data=json.dumps({
                'amount': 100,
                'count': 10
            }),
            content_type='application/json',
        )

        assert res.status_code == 401

        res = c.post(
            url_for('api.v1.red_packet.create'),
            data=json.dumps({
                'amount': 100,
                'count': 10
            }),
            content_type='application/json',
            headers={
                'Authorization': packet_creator.api_key
            }
        )

        assert res.status_code == 201
