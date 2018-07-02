import pytest


def test_a():
    print('test_a')


@pytest.mark.xfail(1 == 1, reason='标记为错误')
def test_b():
    print('test_b')


if __name__ == '__main__':
    pytest.main(['test_xfail.py', '--html=report/a.html'])
