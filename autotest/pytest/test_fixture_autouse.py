import pytest


@pytest.fixture(autouse=True)
def before():
    print('before')


def test_a():
    print('test_a')


def test_b():
    print('test_b')


if __name__ == '__main__':
    pytest.main(['test_fixture_autouse.py'])
