import time

import pytest

from autotest.po.utils import DriverUtil, is_exist_toast
from autotest.po.v5.login import LoginProxy


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

        assert is_exist_toast("用户名密码不能为空")

    def test_login_password_is_error(self):
        print('test_login_password_is_error')
        time.sleep(5)

        self.login_proxy.login("likg_java", "error")

        assert is_exist_toast("用户名或密码错误")


if __name__ == '__main__':
    pytest.main(['test_login.py', '-s'])
