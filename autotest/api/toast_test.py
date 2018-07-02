import time
import traceback
from datetime import datetime

from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

cap = {'deviceName': 'emulator', 'platformName': 'Android', 'appPackage': 'net.csdn.csdnplus',
       'appActivity': '.activity.SplashActivity', 'automationName': 'Uiautomator2'}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)
time.sleep(5)

try:
    # 直接点击登录按钮
    driver.find_element_by_id('net.csdn.csdnplus:id/csdnsign_in_button').click()

    # 获取toast
    print('start time=', datetime.now())
    toast = "用户名密码不能为空"
    xpath = "//*[contains(@text,'{}')]".format(toast)
    element = WebDriverWait(driver, 10, 0.2).until(lambda x: x.find_element_by_xpath(xpath))
    print('element=', element)
    print('element.text=', element.text)
except Exception:
    print('not find toast!')
    traceback.print_exc()
finally:
    print('end time=', datetime.now())

driver.quit()
