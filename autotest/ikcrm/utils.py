from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class DriverUtil:
    """
    驱动工具类
    """

    __driver = None

    @staticmethod
    def get_driver():
        print('get_driver...')
        if DriverUtil.__driver is None:
            DriverUtil.__init_driver()
        return DriverUtil.__driver

    @staticmethod
    def __init_driver():
        print('__init_driver...')
        cap = {'platformName': 'Android', 'deviceName': 'emulator', 'appPackage': 'com.vcooline.aike',
               'appActivity': '.activity.LoginActivity', 'automationName': 'Uiautomator2'}
        DriverUtil.__driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)
        DriverUtil.__driver.implicitly_wait(10)

    @staticmethod
    def quit_driver():
        print('quit_driver...')
        DriverUtil.__driver.quit()


class ToastUtil:
    @staticmethod
    def get_toast(toast):
        element = None
        try:
            xpath = ".//*[contains(@text,'{}')]".format(toast)
            element = WebDriverWait(DriverUtil.get_driver(), 10, 0.01).until(lambda x: x.find_element_by_xpath(xpath))
            print('success find toast={}'.format(toast))
        except:
            print('not find toast={}'.format(toast))
        return element
