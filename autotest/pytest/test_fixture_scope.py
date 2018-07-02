import pytest


@pytest.fixture(scope='class')
def before():
    print('before')


class TestScope:
    def test_a(self, before):
        print('test_a')

    def test_b(self, before):
        print('test_b')


if __name__ == '__main__':
    pytest.main(['test_fixture_scope.py'])
