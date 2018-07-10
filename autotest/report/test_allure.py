import allure
import pytest

@allure.severity("critical")
def test_a():
    print('test_a')


def test_b():
    print('test_b')
    assert 1 == 2


def test_foo():
    print('test_foo')
    allure.step("开始输入用户名")
    allure.attach('参数', 'Hello World 1234')


@allure.step("加法操作: num1={0} num2={1}")
def add(num1, num2):
    return num1 + num2


@allure.step("加法测试")
@allure.severity("critical")
def test_add():
    result = add(1, 2)
    allure.attach("add方法返回结果：", str(result))
    print("result=", result)


if __name__ == '__main__':
    pytest.main(['test_allure.py', '-s', '--alluredir=allure-result'])
