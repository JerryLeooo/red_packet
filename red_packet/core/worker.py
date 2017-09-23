# -*- coding: utf-8 -*-

import os
from red_packet.core.extensions import make_celery, redis_store
from red_packet.models.packet import RedPacket
from red_packet.models.user import User
from red_packet.core.helpers import gen_sequence_key
from red_packet.app import create_app

app = create_app()
Mode = 'Development'
if os.getenv('RED_PACKET_PRODUCTION'):
    Mode = 'Production'
app.config.from_object('red_packet.settings.%sConfig' % Mode)
celery = make_celery(app)

@celery.task()
def return_shares(token):
    packet = RedPacket.get_by_token(token)
    key = gen_sequence_key(token)
    shares = redis_store.lrange(key, 0, -1)
    s = sum([int(share) for share in shares])
    redis_store.lrem(key, 0, -1)
    creator = User.get_by_id(packet.creator_id)
    original_returned_credits = creator.returned_credits or 0
    creator.update(returned_credits=s+original_returned_credits)