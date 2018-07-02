import base64
import logging

# logging.basicConfig(level=logging.DEBUG)
from itcast.autotest.conf import log2

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s')


def test():
    print('111111')

    logging.info('hello....')

    logging.error('error...')

    log2.a()


test()


s = "abc中".encode()
print(s)

b = base64.b64encode(s)
print(b)

ss = bytes.decode(b)
print(ss)

b2 = base64.b64decode(ss)
print('b2=', b2)

s2 = bytes.decode(b2)
print('s2=', s2)

