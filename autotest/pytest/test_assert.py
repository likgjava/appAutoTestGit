import pytest


def add(num1, num2):
    return num1 + num2


def test_a():
    print('test_a')
    ret = add(1, 1)
    assert ret == 2


def test_b():
    print('test_b')
    ret = add(1, 2)
    assert ret == 5


if __name__ == '__main__':
    pytest.main(['test_assert.py'])
