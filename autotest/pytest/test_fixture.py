import pytest


@pytest.fixture()
def before():
    print('before')


def test_a(before):
    print('test_a')


@pytest.mark.usefixtures('before')
def test_b():
    print('test_b')


if __name__ == '__main__':
    pytest.main(['test_fixture.py'])
