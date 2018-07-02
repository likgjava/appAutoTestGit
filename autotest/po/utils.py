from appium import webdriver


class DriverUtil:
    """
    驱动工具类
    """

    __driver = None

    @staticmethod
    def get_driver():
        print('get_driver...')
        if DriverUtil.__driver is None:
            cap = {
                'platformName': 'Android',
                'deviceName': 'emulator',
                'appPackage': 'net.csdn.csdnplus',
                'appActivity': '.activity.SplashActivity',
                'automationName': 'Uiautomator2',
                # 'noReset': 'true',
            }
            DriverUtil.__driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)
            DriverUtil.__driver.implicitly_wait(10)
        return DriverUtil.__driver

    @staticmethod
    def quit_driver():
        print('quit_driver...')
        DriverUtil.__driver.quit()
