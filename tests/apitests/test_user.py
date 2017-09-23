# -*- coding: utf-8 -*-

import json
from flask import url_for

def test_get_credits(app, red_packet, share_getter, packet_creator):
    with app.test_client() as c:

        share = red_packet.get_next_share(packet_creator)

        res = c.get(
            url_for('api.v1.me.credits'),
            content_type='application/json',
            headers={
                'Authorization': packet_creator.api_key
            }
        )

        assert res.status_code == 200
        resp = json.loads(res.data)
        assert resp['credits'] == share.amount

        share = red_packet.get_next_share(share_getter)

        res = c.get(
            url_for('api.v1.me.credits'),
            content_type='application/json',
            headers={
                'Authorization': share_getter.api_key
            }
        )

        assert res.status_code == 200
        resp = json.loads(res.data)
        assert resp['credits'] == share.amount

def test_get_share_got(app, red_packet, share_getter, packet_creator):
    with app.test_client() as c:

        share = red_packet.get_next_share(packet_creator)

        res = c.get(
            url_for('api.v1.me.shares_got'),
            content_type='application/json',
            headers={
                'Authorization': packet_creator.api_key
            }
        )

        assert res.status_code == 200
        resp = json.loads(res.data)
        assert share.as_dict() in resp['shares']

        share = red_packet.get_next_share(share_getter)

        res = c.get(
            url_for('api.v1.me.shares_got'),
            content_type='application/json',
            headers={
                'Authorization': share_getter.api_key
            }
        )

        assert res.status_code == 200
        resp = json.loads(res.data)
        assert share.as_dict() in resp['shares']
