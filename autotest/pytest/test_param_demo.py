import pytest


# 求和
def add(x, y):
    return x + y


def test_add_01():
    result = add(1, 1)
    assert result == 2


def test_add_02():
    result = add(1, 0)
    assert result == 1


def test_add_03():
    result = add(0, 0)
    assert result == 0


def test_add():
    test_data = [(1, 1, 2), (1, 0, 1), (0, 0, 0)]
    for x, y, expect in test_data:
        print("x={} y={} expect={}".format(x, y, expect))
        result = add(x, y)
        assert expect == result


if __name__ == '__main__':
    pytest.main(["test_param_demo.py"])
