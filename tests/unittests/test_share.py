# -*- coding: utf-8 -*-

import pytest
from red_packet.models.packet import RedPacket
from red_packet.core.errors import ApiError

def test_share(red_packet, share_getter):
    share = red_packet.get_next_share(share_getter)
    assert share.owner_id == share_getter.id
    assert share.red_packet_token == red_packet.token

def test_get_more_share(packet_creator, share_getter):
    packet = RedPacket.create(amount=2, count=2, creator_id=packet_creator.id)
    packet.get_next_share(share_getter)
    with pytest.raises(ApiError):
        packet.get_next_share(share_getter)
