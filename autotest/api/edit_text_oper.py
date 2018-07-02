import time

from appium import webdriver

cap = {'deviceName': 'emulator', 'platformName': 'Android', 'appPackage': 'com.android.settings',
       'appActivity': '.Settings', 'unicodeKeyboard': 'true', 'resetKeyboard': 'true'}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)

# 点击搜索按钮
driver.find_element_by_id('com.android.settings:id/search').click()
time.sleep(3)

search_view = driver.find_element_by_id('android:id/search_src_text')
search_view.send_keys('123456')
# search_view.send_keys('abc中国')

# 清空
search_view.clear()

# 字母a
driver.keyevent(29)
driver.keyevent(115)
driver.keyevent(30)
driver.keyevent(29)

time.sleep(5)
driver.quit()
