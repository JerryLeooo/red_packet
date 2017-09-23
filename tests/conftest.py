# -*- coding: utf-8 -*-

import pytest
from red_packet.app import create_app
from red_packet.core.database import db as _db

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
        db.create_all()

    yield _db
    _db.drop_all()
