import time

from appium import webdriver

cap = {
    'platformName': 'Android',
    'deviceName': 'emulator',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings',
    'unicodeKeyboard': True,
    'resetKeyboard': True
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)

# 点击搜索按钮
driver.find_element_by_id('com.android.settings:id/search').click()

# 输入内容
search_view = driver.find_element_by_id('android:id/search_src_text')
search_view.send_keys('123456')

# 清空
search_view.clear()

# 输入中文字符
search_view.send_keys('abc中国')

time.sleep(5)
driver.quit()
