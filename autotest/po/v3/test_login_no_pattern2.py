import time

import pytest
from appium import webdriver

from autotest.po.utils import is_exist_toast


class TestLogin:

    def setup_class(self):
        print('setup_class...')
        cap = {
            'platformName': 'Android',
            'deviceName': 'emulator',
            'appPackage': 'net.csdn.csdnplus',
            'appActivity': '.activity.SplashActivity',
            'automationName': 'Uiautomator2'
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)
        self.driver.implicitly_wait(10)

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

        assert is_exist_toast("用户名密码不能为空999")

    def test_login_password_is_error(self):
        print('test_login_username_is_null...')
        time.sleep(5)

        self.driver.find_element_by_id('net.csdn.csdnplus:id/editTextUserName').send_keys('likg_java')
        self.driver.find_element_by_id('net.csdn.csdnplus:id/password').send_keys('123')
        self.driver.find_element_by_id('net.csdn.csdnplus:id/csdnsign_in_button').click()

        assert is_exist_toast("用户名或密码错误")


if __name__ == '__main__':
    pytest.main(['test_login_no_pattern2.py', '-s'])
    pass
