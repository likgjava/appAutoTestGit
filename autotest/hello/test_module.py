import pytest
from _pytest.runner import TestReport


def test_a():
    print('test_a.................')
    assert 1


def test_b():
    # TestReport
    assert 0


if __name__ == '__main__':
    pytest.main(['test_module.py', '-s'])