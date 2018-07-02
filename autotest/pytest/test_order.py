import pytest


def test_a():
    print('aaa')


@pytest.mark.run(order=2)
def test_b():
    print('bbb')


@pytest.mark.run(order=1)
def test_c():
    print('ccc')


if __name__ == '__main__':
    pytest.main(['test_order.py'])
