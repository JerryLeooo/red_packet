# -*- coding: utf-8 -*-

import json
from flask import url_for

def test_get_share(app, red_packet, red_packet_2, share_getter, packet_creator):

    with app.test_client() as c:
        res = c.post(
            url_for('api.v1.share.get', token=red_packet.token),
            content_type='application/json',
        )

        assert res.status_code == 401

        res = c.post(
            url_for('api.v1.share.get', token=red_packet.token),
            content_type='application/json',
            headers={
                'Authorization': packet_creator.api_key
            }
        )

        assert res.status_code == 201

        res = c.post(
            url_for('api.v1.share.get', token=red_packet.token),
            content_type='application/json',
            headers={
                'Authorization': share_getter.api_key
            }
        )

        assert res.status_code == 201

        res = c.post(
            url_for('api.v1.share.get', token=red_packet.token),
            content_type='application/json',
            headers={
                'Authorization': share_getter.api_key
            }
        )

        assert res.status_code == 403

        res = c.post(
            url_for('api.v1.share.get', token=red_packet_2.token),
            content_type='application/json',
            headers={
                'Authorization': packet_creator.api_key
            }
        )

        assert res.status_code == 201
        resp = json.loads(res.data)
        amount_1 = int(resp['amount'])

        res = c.post(
            url_for('api.v1.share.get', token=red_packet_2.token),
            content_type='application/json',
            headers={
                'Authorization': share_getter.api_key
            }
        )

        assert res.status_code == 201
        resp = json.loads(res.data)
        amount_2 = int(resp['amount'])

        assert amount_1 + amount_2 == red_packet_2.amount
