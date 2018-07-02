import time
import traceback
from datetime import datetime

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

cap = {'deviceName': 'emulator', 'platformName': 'Android', 'appPackage': 'com.tpshop.malls',
       'appActivity': '.SplashActivity', 'automationName': 'Uiautomator2',
       "noReset": "true"}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)
driver.implicitly_wait(10)
print("驱动创建成功。。。")
time.sleep(2)

try:
    # 直接点击登录按钮
    print("click mine ......")
    driver.find_element_by_xpath("//*[@text='我的']").click()
    time.sleep(2)

    print("click login btn...")
    driver.find_element_by_id("com.tpshop.malls:id/nickname_txtv").click()
    time.sleep(3)


    driver.find_element_by_id("com.tpshop.malls:id/edit_phone_num").send_keys("13041092162")
    driver.find_element_by_id("com.tpshop.malls:id/edit_password").send_keys("tpshop12345678")
    time.sleep(3)
    driver.find_element_by_id("com.tpshop.malls:id/btn_login").click()

    # 获取toast
    print('start time=', datetime.now())
    # toast = "账号不存在"
    toast = "登录成功"
    xpath = "//*[contains(@text,'{}')]".format(toast)
    element = WebDriverWait(driver, 20, 0.1).until(lambda x: x.find_element_by_xpath(xpath))
    print('element=', element)
    print('element.text=', element.text)
except Exception as eeee:
    print('not find toast!', eeee)
    traceback.print_exc()
finally:
    print('end time=', datetime.now())

driver.quit()
