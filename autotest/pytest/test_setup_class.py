import pytest


class TestSetupClass:

    @classmethod
    def setup_class(cls):
        print('setup_class')

    @classmethod
    def teardown_class(cls):
        print('teardown_class')

    def test_a(self):
        print('---->test_a')

    def test_b(self):
        print('---->test_b')

    if __name__ == '__main__':
        pytest.main(['test_setup_class.py'])
