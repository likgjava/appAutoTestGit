import time

import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from autotest.po.utils import DriverUtil
from autotest.po.v5.login2 import LoginProxy


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


class TestLogin:

    def setup_class(self):
        print('setup_class')
        self.driver = DriverUtil.get_driver()

        self.login_proxy = LoginProxy()

    def teardown_class(self):
        print('teardown_class')
        DriverUtil.quit_driver()

    def teardown(self):
        print('teardown')
        time.sleep(3)
        DriverUtil.get_driver().reset()

    def test_login(self):
        print('test_login')
        self.login_proxy.login("likg_java", "csdn12345678")

        assert is_exist_text(self.driver, "已有新的版本")

    def test_login_username_is_null(self):
        print('test_login_username_is_null')
        self.login_proxy.login("", "123")

        assert is_exist_toast(self.driver, "用户名密码不能为空")

    def test_login_password_is_error(self):
        print('test_login_password_is_error')
        self.login_proxy.login("likg_java", "error")

        assert is_exist_toast(self.driver, "用户名或密码错误")


if __name__ == '__main__':
    pytest.main(['test_login2.py', '-s'])
