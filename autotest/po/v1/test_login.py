from appium import webdriver

"""
登录模块-正常登录
"""

cap = {
    'platformName': 'Android',
    'deviceName': 'emulator',
    'appPackage': 'net.csdn.csdnplus',
    'appActivity': '.activity.SplashActivity',
    'automationName': 'Uiautomator2'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)
driver.implicitly_wait(10)

driver.find_element_by_id('net.csdn.csdnplus:id/editTextUserName').input_text('likg_java')
driver.find_element_by_id('net.csdn.csdnplus:id/password').send_keys('123')
driver.find_element_by_id('net.csdn.csdnplus:id/csdnsign_in_button').click()

title = driver.find_element_by_id('net.csdn.csdnplus:id/tvtitle')
print("title.text=", title.text)

driver.quit()
