import time

from appium import webdriver

cap = {
    'platformName': 'Android',
    'deviceName': 'emulator',
    'browserName': 'browser'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)
driver.implicitly_wait(10)

# 打开百度网站
driver.get("http://m.baidu.com")

# 输入搜索关键字
driver.find_element_by_xpath("//*[@id='index-kw']").send_keys("Python")

# 点击搜索按钮
driver.find_element_by_id("index-bn").click()
time.sleep(5)

# 关闭驱动
driver.quit()
