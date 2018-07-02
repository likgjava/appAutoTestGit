import time

from appium import webdriver

cap = {
    'platformName': 'Android',
    'deviceName': 'emulator',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)
time.sleep(5)

# 获取元素属性信息
element = driver.find_element_by_id("com.android.settings:id/search")
# 获取标签名称
tag_name = element.tag_name
print('tag_name=', tag_name)
# 获取text的属性值
text = element.text
print('text=', text)
# 获取content-desc或text的属性值
name = element.get_attribute('name')
print('name=', name)
# 获取class的属性值
class_name = element.get_attribute('className')
print('class_name=', class_name)
# 获取resource-id的属性值
resource_id = element.get_attribute('resourceId')
print('resource_id=', resource_id)

# 获取元素的坐标信息
location = element.location
print('location=', location)
# 获取元素的宽高
size = element.size
print("size=", size)

time.sleep(5)

# 关闭驱动对象
driver.quit()
