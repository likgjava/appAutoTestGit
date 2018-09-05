import os
import time

import pytest
import yaml
from selenium.common.exceptions import TimeoutException

from autotest.datadriven.csdn.page.login_page import LoginProxy
from autotest.datadriven.csdn.utils import DriverUtil, is_exist_toast


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
    data_file = os.getcwd() + "/../data/login.yaml"
    print("data_file=", data_file)
    with open(data_file, encoding='UTF-8') as f:
        test_data = yaml.load(f)
        for data in test_data.get("test_login").values():
            test_data.append((data["username"], data["password"], data["toast"], data["is_success"]))
    print("test_data=", test_data)
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

    @pytest.mark.parametrize("username,password,toast,is_success", load_data())
    def test_login(self, username, password, toast, is_success):
        print("test_login username={} password={} toast={} is_success={}", username, password, toast, is_success)
        self.loginProxy.login(username, password)

        if is_success:
            assert is_exist_text(self.driver, toast)
        else:
            assert is_exist_toast(toast)


if __name__ == '__main__':
    pytest.main(['test_login.py', '-s'])
