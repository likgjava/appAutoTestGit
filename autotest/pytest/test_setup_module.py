import pytest


def setup_module():
    print('setup_module')


def teardown_module():
    print('teardown_module')


class TestClass:

    def test_a(self):
        print('---->test_a')


class TestClass2:

    def test_b(self):
        print('---->test_b')


if __name__ == '__main__':
    pytest.main(['test_setup_module.py'])
