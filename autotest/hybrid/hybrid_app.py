import time

from appium import webdriver

cap = {
    'platformName': 'Android',
    'deviceName': 'emulator',
    'appPackage': 'com.tencent.news',
    'appActivity': '.activity.SplashActivity',
    'noReset': 'true'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)
driver.implicitly_wait(10)
time.sleep(5)

print("111111111111111111111")
driver.find_element_by_xpath("//*[contains(@text, '关于党员')]").click()
time.sleep(5)

# 获取当前上下文
print('current_context=', driver.current_context)
# 获取所有上下文
print('contexts=', driver.contexts)

print('page_source=', driver.page_source)

# 切换上下文到WEBVIEW
driver.switch_to.context(driver.contexts[1])
print('context=', driver.context)

print('page_source=', driver.page_source)
print('----------------------------------------------------')
time.sleep(3)

# 获取所有img标签
img_list = driver.find_elements_by_tag_name('img')
for img in img_list:
    print('src=', img.get_attribute('data-src'))

# 切换到NATIVE_APP
driver.switch_to.context("NATIVE_APP")

# 点击评一下
driver.find_element_by_id("com.tencent.news:id/btn_input_txt").click()

time.sleep(5)

driver.quit()
