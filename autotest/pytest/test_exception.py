import pytest


def div(a, b):
    print('div...')
    return a / b


def test_div():
    with pytest.raises(ZeroDivisionError):
        ret = div(1, 0)
        print('ret=', ret)


if __name__ == '__main__':
    pytest.main(['test_exception.py', '-s'])