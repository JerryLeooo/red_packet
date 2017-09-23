# -*- coding: utf-8 -*-

def test_share(red_packet, share_getter):
    share, code = red_packet.get_next_share(share_getter)
    assert share.owner_id == share_getter.id
    assert share.red_packet_token == red_packet.token