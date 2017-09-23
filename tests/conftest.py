# -*- coding: utf-8 -*-

import pytest
from red_packet.app import create_app
from red_packet.core.database import db as _db
from red_packet.models.user import User
from red_packet.models.packet import RedPacket
from red_packet.models.share import Share

@pytest.yield_fixture()
def app():
    _app = create_app('Testing')
    ctx = _app.test_request_context()
    ctx.push()
    assert _app.testing
    yield _app
    ctx.pop()

@pytest.yield_fixture()
def db(app):
    _db.app = app
    with app.app_context():
        _db.create_all()

    yield _db
    _db.drop_all()

@pytest.fixture
def packet_creator(app, db):
    creator = User.create(username='test_packet_creator',
                          api_key='test_packet_creator_apikey')
    return creator

@pytest.fixture
def share_getter(app, db):
    getter = User.create(username='test_share_getter',
                         api_key='share_getter_apikey')
    return getter

@pytest.fixture
def red_packet(app, db, packet_creator):
    packet = RedPacket.create(amount=10000, count=10, creator_id=packet_creator.id)
    return packet

@pytest.fixture
def red_packet_2(app, db, packet_creator):
    packet = RedPacket.create(amount=10000, count=2, creator_id=packet_creator.id)
    return packet

@pytest.fixture
def share(app, db, red_packet, share_getter):
    share = red_packet.get_next_share(share_getter)
    return share
