import base64

import pytest
import time


# print(int(time.time()))
# 123 456


# t = time.strftime("%Y%m%d-%H%M%S", time.localtime())
# print(t)

class LoginP:
    def login(self):
        print('csdn....')


class TestScene:
    loginProxy = LoginP()

    @classmethod
    def setup_class(cls):
        print('setup_class...')

    @classmethod
    def teardown_class(cls):
        print('teardown_class...')

    def test_login(self):
        print('test_login...')
        self.loginProxy.login()


if __name__ == '__main__':
    # pytest.main(['T.py', '-s'])
    # pytest.main(['T.py'])
    pass

content = "python中国123"
byte = content.encode()
print('byte=', byte)
print('byte type=', type(byte))

b64 = base64.b64encode(byte)
print('b64=', b64)
print('b64 type=', type(b64))

b64str = b64.decode()
print('b64str=', b64str)
print('b64str type=', type(b64str))
print('-----------------------------------')

d = base64.b64decode(b64str)
print('d=', d)
print('d type=', type(d))

dstr = d.decode()
print('dstr=', dstr)
print('dstr type=', type(dstr))

