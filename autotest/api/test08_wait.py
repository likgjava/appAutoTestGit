import time
import traceback
from datetime import datetime

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

cap = {
    'deviceName': 'emulator',
    'platformName': 'Android',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings',
    'automationName': 'Uiautomator2',
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)

# 强制等待
# time.sleep(5)

# 设置隐式等待
driver.implicitly_wait(10)
try:
    print('start time=', datetime.now())
    driver.find_element_by_id('com.android.dialer:id/floating_action_button666')
except Exception as e:
    print('not find element!', e)
    traceback.print_exc()
finally:
    print('end time=', datetime.now())

# 显式等待
# 设置超时时间为10秒，轮询频率为2秒
# try:
#     print('start time=', datetime.now())
#     id = 'com.android.dialer:id/floating_action_button666'
#     element = WebDriverWait(driver, 10, 2).until(lambda x: x.find_element_by_id(id))
#     print('element=', element)
# except Exception:
#     print('not find element!!!')
#     traceback.print_exc()
# finally:
#     print('end time=', datetime.now())

driver.quit()
