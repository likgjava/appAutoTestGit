import json
import os
import time

import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from itcast.autotest.datadriven.csdn.page.login_page import LoginProxy
from itcast.autotest.datadriven.csdn.utils import DriverUtil


def is_exist_toast(driver, text):
    """
    判断toast元素是否存在
    :param driver: 驱动对象
    :param text: toast内容
    :return: 存在返回True，不存在返回False
    """
    try:
        xpath = "//*[contains(@text, '{}')]".format(text)
        ele = WebDriverWait(driver, 10, 0.1).until(lambda x: x.find_element_by_xpath(xpath))
        print("ele=====", ele)
        return ele is not None
    except TimeoutException:
        print("not find toast={}".format(text))
        return False


def is_exist_text(driver, text):
    """
    判断页面中是否存在指定的文本内容
    :param driver: 驱动对象
    :param text: 文本内容
    :return: 存在返回True，不存在返回False
    """
    try:
        xpath = "//*[contains(@text, '{}')]".format(text)
        ele = driver.find_element_by_xpath(xpath)
        print("ele=====", ele)
        return ele is not None
    except TimeoutException:
        print("not find toast={}".format(text))
        return False


def load_data():
    test_data = []
    data_file = os.getcwd() + "/../data/testData.json"
    print("data_file=", data_file)
    with open(data_file, encoding='UTF-8') as f:
        test_data = json.load(f)
    return test_data


class TestLogin:

    def setup_class(self):
        print('setup_class')
        self.driver = DriverUtil.get_driver()
        self.loginProxy = LoginProxy()
        self.testData = load_data()

    def teardown_class(self):
        print('teardown_class')
        DriverUtil.quit_driver()

    def teardown(self):
        print('teardown')
        time.sleep(10)
        self.driver.reset()

    def test_login(self):
        print('test_login')

        data = self.testData['loginSuccess']
        print('data=', data)
        self.loginProxy.login(data['userName'], data['password'])

        assert is_exist_text(self.driver, "已有新的版本")

    def test_login_username_is_null(self):
        print('test_login_username_is_null')
        data = self.testData['loginUserNameIsNull']
        print('data=', data)
        self.loginProxy.login(data['userName'], data['password'])

        assert is_exist_toast(self.driver, "用户名密码不能为空")

    def test_login_password_is_error(self):
        print('test_login_password_is_error')
        data = self.testData['loginPasswordIsError']
        print('data=', data)
        self.loginProxy.login(data['userName'], data['password'])

        assert is_exist_toast(self.driver, "用户名或密码错误")


if __name__ == '__main__':
    pytest.main(['test_login.py', '-s'])
