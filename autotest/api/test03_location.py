import time

from appium import webdriver
from selenium.webdriver.common.by import By

cap = {
    'platformName': 'Android',
    'deviceName': 'emulator',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)

# 获取页面源码
# page_source = driver.page_source
# print('page_source=', page_source)

# 使用id定位方式，定位搜索按钮，并点击
# element = driver.find_element_by_id("com.android.settings:id/search")
# element.click()

# className定位
# element = driver.find_element_by_class_name("android.widget.TextView")
# print('text=', element.text)


# 根据元素name定位，该方式已不支持
# element = driver.find_element_by_name("Search settings")

# accessibility_id定位，根据元素content-desc定位
# element = driver.find_element_by_accessibility_id("搜索设置")
# element.click()

# 根据xpath定位
# 获取指定标签名的元素
# element = driver.find_element_by_xpath("//android.widget.TextView")
# print('name=', element.text)
# 属性等于指定字符
# element = driver.find_element_by_xpath("//android.widget.TextView[@text='WLAN']")
# element.click()
# 属性包含指定字符
# element = driver.find_element_by_xpath("//android.widget.TextView[contains(@text, 'WLA')]")
# element.click()
# 任意标签的属性值包含指定字符
# element = driver.find_element_by_xpath("//*[contains(@text, 'WLAN')]")
# element.click()

# 使用android_uiautomator定位
# text定位
# element = driver.find_element_by_android_uiautomator("new UiSelector().text(\"More\")")
# element.click()
# resourceId定位
# element = driver.find_element_by_android_uiautomator("new UiSelector().resourceId(\"com.android.settings:id/search\")")
# element.click()
# className定位
# element = driver.find_element_by_android_uiautomator("new UiSelector().className(\"android.widget.TextView\")")
# print('text=', element.text)
# description定位
# element = driver.find_element_by_android_uiautomator("new UiSelector().description(\"Search settings\")")
# element.click()
# index定位
# list = driver.find_elements_by_android_uiautomator("new UiSelector().index(1)")
# print('list.len=', len(list))
# 多个属性自由组合
# element = driver.find_element_by_android_uiautomator("new UiSelector().className(\"android.widget.TextView\").index(2)")
# print('text=', element.text)
# 模糊匹配
# element = driver.find_element_by_android_uiautomator("new UiSelector().textContains(\"More\")")
# print('text=', element.text)
# 正则表达式匹配
# element = driver.find_element_by_android_uiautomator("new UiSelector().textMatches(\"^More.*\")")
# print('text=', element.text)

# 获取多个匹配的元素
# elements = driver.find_elements_by_class_name("android.widget.TextView")
# print('elements.len=', len(elements))
# for e in elements:
#     print('text=', e.text)

# 定位元素的另一种写法
# element = driver.find_element(By.ID, "com.android.settings:id/search")


# 暂停
time.sleep(3)

# 关闭驱动对象
driver.quit()
