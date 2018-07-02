import pytest


@pytest.mark.parametrize('a', [1, 2, 3])
def test_a(a):
    print('test_a...a=', a)


@pytest.mark.parametrize('a,b', [(1, 2), (3, 4), (5, 6)])
def test_b(a, b):
    print('test_b...a={} b={}'.format(a, b))


data = [(1, 1), (2, 2), (3, 3)]


@pytest.mark.parametrize('a,b', data)
def test_c(a, b):
    print('test_c...a={} b={}'.format(a, b))


def build_data():
    return [(11, 22), (33, 44), (55, 66)]


@pytest.mark.parametrize('a,b', build_data())
def test_d(a, b):
    print('test_d...a={} b={}'.format(a, b))


if __name__ == '__main__':
    pytest.main(['test_parametrize.py', '--html=report/a.html'])
