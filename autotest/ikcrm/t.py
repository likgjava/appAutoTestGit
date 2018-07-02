import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

cap = {'platformName': 'Android', 'deviceName': 'emulator', 'appPackage': 'com.vcooline.aike',
       'appActivity': '.activity.LoginActivity', 'automationName': 'Uiautomator2'}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)


def teardown():
    print('teardown...')
    driver.quit()


def tttt():
    driver.start_activity('com.vcooline.aike', '.activity.MainActivity')


tttt()
teardown()
