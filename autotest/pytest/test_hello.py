import pytest


def test_hi():
    print('hi pytest')


class TestHello:
    def test_foo(self):
        print("test_foo")


if __name__ == '__main__':
    pytest.main(['test_hello.py'])
