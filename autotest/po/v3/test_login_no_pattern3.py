import time

import pytest
from appium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from autotest.po.utils import DriverUtil


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

    def teardown_class(self):
        print('teardown_class...')
        self.driver.quit()

    def teardown(self):
        print('teardown...')
        time.sleep(5)
        self.driver.reset()

    @pytest.mark.skip()
    def test_login(self):
        print('test_login...')
        time.sleep(5)

        self.driver.find_element_by_id('net.csdn.csdnplus:id/editTextUserName').send_keys('likg_java')
        self.driver.find_element_by_id('net.csdn.csdnplus:id/password').send_keys('123')
        self.driver.find_element_by_id('net.csdn.csdnplus:id/csdnsign_in_button').click()

        title = self.driver.find_element_by_id('net.csdn.csdnplus:id/tvtitle')
        assert title.text == '头条'

    def test_login_username_is_null(self):
        print('test_login_username_is_null...')
        time.sleep(5)

        self.driver.find_element_by_id('net.csdn.csdnplus:id/password').send_keys('123')
        self.driver.find_element_by_id('net.csdn.csdnplus:id/csdnsign_in_button').click()

        assert is_exist_toast(self.driver, "用户名密码不能为空")

    def test_login_password_is_error(self):
        print('test_login_username_is_null...')
        time.sleep(5)

        self.driver.find_element_by_id('net.csdn.csdnplus:id/editTextUserName').send_keys('likg_java')
        self.driver.find_element_by_id('net.csdn.csdnplus:id/password').send_keys('123')
        self.driver.find_element_by_id('net.csdn.csdnplus:id/csdnsign_in_button').click()

        assert is_exist_toast(self.driver, "用户名或密码错误")


if __name__ == '__main__':
    pytest.main(['test_login_no_pattern2.py', '-s'])
    pass
