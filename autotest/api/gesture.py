import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

cap = {
    'platformName': 'Android',
    'deviceName': 'emulator',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings',
    # 'appPackage': 'com.android.messaging',
    # 'appActivity': '.ui.conversationlist.ConversationListActivity',
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)
time.sleep(3)




# 点击
# 点击搜索按钮
# button = driver.find_element_by_id("com.android.settings:id/search")
# button.click()
# time.sleep(3)
# 使用TouchAction通过tap来实现轻敲屏幕，最后通过perform()方法来提交操作
# TouchAction(driver).tap(button).perform()
# TouchAction(driver).tap(x=440, y=90).perform()


# 按压
# 按压搜索按钮
# button = driver.find_element_by_id("com.android.settings:id/search")
# TouchAction(driver).press(button).release().perform()
# TouchAction(driver).press(x=440, y=90).release().perform()

# 长按
# 长按搜索按钮
# element = driver.find_element_by_id("com.android.settings:id/search")
# TouchAction(driver).long_press(element, duration=3000).release().perform()

# 页面滑动
# 获取屏幕的宽度和高度
# width = driver.get_window_size()['width']
# height = driver.get_window_size()['height']
# print('width={} height={}'.format(width, height))
# 上滑
# driver.swipe(width / 2, height * 9 / 10, width / 2, height / 10, 5000)

# 元素滑动
# element = driver.find_element_by_xpath("//*[contains(@text, 'hello')]/..")
# print(element.location)
# print(element.size)
# start_x = element.location['x'] + element.size['width'] * 9 / 10
# start_y = element.location['y'] + element.size['height'] / 2
# end_x = element.location['x'] + element.size['width'] / 10
# end_y = start_y
# driver.swipe(start_x, start_y, end_x, end_y, 1000)

# 滚动
# destination = driver.find_element_by_xpath("//android.widget.TextView[@text='WLAN']")
# origin = driver.find_element_by_xpath("//android.widget.TextView[@text='显示']")
# driver.scroll(origin, destination)

# 拖拽
destination = driver.find_element_by_xpath("//android.widget.TextView[@text='WLAN']")
origin = driver.find_element_by_xpath("//android.widget.TextView[@text='显示']")
driver.drag_and_drop(origin, destination)

time.sleep(5)

# 关闭驱动对象
driver.quit()
