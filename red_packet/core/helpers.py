# -*- coding: utf-8 -*-

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
    return "%08s" % token