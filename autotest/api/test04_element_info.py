import time

from appium import webdriver

cap = {
    'platformName': 'Android',
    'deviceName': 'emulator',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)

# 获取元素属性信息
element = driver.find_element_by_id("com.android.settings:id/search")

# 获取标签名称
print('tag_name=', element.tag_name)

# 获取text的属性值
print('text=', element.text)

# 获取content-desc或text的属性值
print('name=', element.get_attribute('name'))

# 获取class的属性值
print('class_name=', element.get_attribute('className'))

# 获取resource-id的属性值
print('resource_id=', element.get_attribute('resourceId'))

# 获取元素的坐标信息
print('location=', element.location)
# 获取元素的宽高
print("size=", element.size)

time.sleep(5)

# 关闭驱动对象
driver.quit()
