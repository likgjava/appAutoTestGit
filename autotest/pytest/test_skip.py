import pytest


def test_a():
    print('test_a')


@pytest.mark.skip('代码未完成')
def test_b():
    print('test_b')


# 环境
environment = "Android"


@pytest.mark.skipif(environment == 'Android', reason='Android设备跳过')
def test_c():
    print('test_c')


if __name__ == '__main__':
    pytest.main(['test_skip.py', '--html=report/a.html'])
