import pytest


def setup():
    print('setup')
#
#
# def teardown():
#     print('teardown')
#

#
# def setup_function():
#     print('setup_function')
#
#
# def teardown_function():
#     print('teardown_function')


def test_a():
    print('---->test_a')


def test_b():
    print('---->test_b')



class TestClassMethod:
    # def setup(self):
    #     print('class setup')
    #
    # def teardown(self):
    #     print('class teardown')
    #
    # def setup_method(self):
    #     print('class setup_method')
    #
    # def teardown_method(self):
    #     print('class teardown_method')

    # def test_class_a(self):
    #     print('---->test_class_a')
    #
    # def test_class_b(self):
    #     print('---->test_class_b')

    pass


if __name__ == '__main__':
    pytest.main(['test_setup.py'])
