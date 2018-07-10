import time

import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from autotest.po.utils import DriverUtil
from autotest.po.v4.login import LoginProxy


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


class TestLogin:

    def setup_class(self):
        print('setup_class...')
        self.driver = DriverUtil.get_driver()

        self.login_proxy = LoginProxy()

    def teardown_class(self):
        print('teardown_class')
        DriverUtil.quit_driver()

    def teardown(self):
        print('teardown')
        time.sleep(10)
        self.driver.reset()

    def test_login(self):
        print('test_login')
        self.login_proxy.login("likg_java", "123")

        title = self.driver.find_element_by_id('net.csdn.csdnplus:id/tvtitle')
        assert title.text == '头条'

    def test_login_username_is_null(self):
        print('test_login_username_is_null')
        time.sleep(5)

        self.login_proxy.login("", "123")

        assert is_exist_toast(self.driver, "用户名密码不能为空")

    def test_login_password_is_error(self):
        print('test_login_password_is_error')
        time.sleep(5)

        self.login_proxy.login("likg_java", "error")

        assert is_exist_toast(self.driver, "用户名或密码错误")


if __name__ == '__main__':
    pytest.main(['test_login.py', '-s'])
