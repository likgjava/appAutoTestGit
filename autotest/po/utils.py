from appium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait


def is_exist_toast(text):
    """
    判断toast元素是否存在
    :param text: toast内容
    :return: 存在返回True，不存在返回False
    """
    try:
        xpath = "//*[contains(@text, '{}')]".format(text)
        ele = WebDriverWait(DriverUtil.get_driver(), 10, 0.1).until(lambda x: x.find_element_by_xpath(xpath))
        print("ele=====", ele)
        return ele is not None
    except TimeoutException:
        print("not find toast={}".format(text))
        return False

class DriverUtil:
    """
    驱动工具类
    """

    _driver = None

    @staticmethod
    def get_driver():
        print('get_driver...')
        if DriverUtil._driver is None:
            cap = {
                'platformName': 'Android',
                'deviceName': 'emulator',
                'appPackage': 'net.csdn.csdnplus',
                'appActivity': '.activity.SplashActivity',
                'automationName': 'Uiautomator2',
                # 'noReset': 'true',
            }
            DriverUtil._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)
            DriverUtil._driver.implicitly_wait(10)
        return DriverUtil._driver

    @staticmethod
    def quit_driver():
        print('quit_driver...')
        DriverUtil.get_driver().quit()
