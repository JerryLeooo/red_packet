# -*- coding: utf-8 -*-

import random

def gen_token(_id):

    alphabet  = '023456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'

    r = []
    _id = int(_id)
    n = len(alphabet)
    c = 0

    while _id != 0 and c < 8:
        _id, i = _id / n, _id % n
        r.append(alphabet[i])
        c += 1

    token = "".join(r)
    return token.zfill(8)

def gen_sequence_key(token):
    return 'share_seq:v1:%s' % token

def gen_share_sequence(token, amount, count):
    from red_packet.core.extensions import redis_store

    key = gen_sequence_key(token) 

    while count > 0:
        cur = random.randint(1, amount - 1 * (count - 1))
        redis_store.rpush(key, cur)
        amount, count = amount - cur, count - 1
