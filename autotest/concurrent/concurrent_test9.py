import time

import pytest
from appium import webdriver


def param():
    data = [("tom", "123", "192.168.218.101:5555", 4723), ("java", "666", "192.168.218.102:5555", 4733)]
    return data


@pytest.mark.parametrize('username,password,udid,port', param())
def test(username, password, udid, port):
    print('username={} password={} udid={} port={}'.format(username, password, udid, port))

    for i in range(15):
        f = open(username + '.txt', 'a', encoding='utf-8')
        f.write(username + str(i) + '\n')
        f.close()
        time.sleep(1)


if __name__ == '__main__':
    print('main=======================')
    pytest.main(['concurrent_test9.py', '-s', '-n=auto'])
