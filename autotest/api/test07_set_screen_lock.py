import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

cap = {
    'platformName': 'Android',
    'deviceName': 'emulator',
    'appPackage': 'com.android.settings',
    'appActivity': '.ChooseLockPattern', # .Settings
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)
time.sleep(3)


def get_element_by_swipe_page(location_type, location_value):
    width = driver.get_window_size()['width']
    height = driver.get_window_size()['height']
    while True:
        ele = get_element(location_type, location_value)
        if ele:
            print("找到了...")
            return ele
        else:
            print("这一屏中没找到...")
        # 向上滑动屏幕
        driver.swipe(width / 2, height * 9 / 10, width / 2, height / 10, 3000)


def get_element(location_type, location_value):
    ele = None
    try:
        if location_type == "id":
            ele = driver.find_element_by_id(location_value)
        elif location_type == "xpath":
            ele = driver.find_element_by_xpath(location_value)
    except Exception as e:
        print("get element error.", e)
    return ele


# 设置锁屏手势密码
# 1. 向上滑动页面找到‘安全’选项，并点击
# element = get_element_by_swipe_page("xpath", "//*[@text='安全']")
# element.click()
# time.sleep(3)

# 2. 点击‘屏幕锁定方式’
# driver.find_element_by_xpath("//*[@text='屏幕锁定方式']").click()
# time.sleep(3)

# 3. 点击‘图案’选项
# driver.find_element_by_xpath("//*[@text='图案']").click()
# time.sleep(3)

# 绘制锁屏密码
# 80    290
# 240   290
# 240   450
# 400   450
TouchAction(driver).press(x=80, y=290).wait(500).move_to(x=240, y=290).wait(500) \
    .move_to(x=240, y=450).wait(500).move_to(x=400, y=450).release().perform()
time.sleep(3)

# 关闭驱动对象
driver.quit()
