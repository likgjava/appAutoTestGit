import allure
import pytest


def test_a():
    print('test_a')


def test_b():
    print('test_b')
    assert 1 == 2


def test_foo():
    print('test_foo')
    allure.step("开始输入用户名")
    allure.attach('参数', 'Hello World 1234')


if __name__ == '__main__':
    pytest.main(['test_allure.py', '-s', '--alluredir=report'])
