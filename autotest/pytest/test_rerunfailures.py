import pytest


def test_a():
    print('aaa')


def test_b():
    print('bbb')
    assert 0


if __name__ == '__main__':
    pytest.main(['test_rerunfailures.py', '--reruns=2'])
