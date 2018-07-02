import pytest


@pytest.fixture()
def data():
    return 1


def test_a(data):
    print('test_a data=', data)


@pytest.fixture(params=[1, 2, 3])
def data2(request):
    return request.param


def test_b(data2):
    print('test_b data2=', data2)


if __name__ == '__main__':
    pytest.main(['test_fixture_param.py'])
