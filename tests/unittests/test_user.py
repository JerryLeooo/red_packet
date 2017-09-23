# -*- coding: utf-8 -*-

def test_get_shares(red_packet, share_getter):
    share = red_packet.get_next_share(share_getter)
    assert share.as_dict() in share_getter.get_own_shares()

def test_own_credits(share_getter, red_packet):
    share = red_packet.get_next_share(share_getter)
    assert share_getter.get_own_credits() == share.amount
