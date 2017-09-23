# -*- coding: utf-8 -*-

from red_packet.core.helpers import gen_token
from red_packet.models.packet import RedPacket

def test_packet(packet_creator, red_packet):
    assert red_packet.creator_id == packet_creator.id
    assert red_packet.token == gen_token(red_packet.id)

def test_get_by_token(red_packet):
    assert RedPacket.get_by_token(red_packet.token) == red_packet

def test_create_packet(packet_creator):
    amount = 10
    RedPacket.create(amount=amount, count=7, creator_id=packet_creator.id)