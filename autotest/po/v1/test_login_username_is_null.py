from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

"""
登录模块-用户名为空
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

driver.find_element_by_id('net.csdn.csdnplus:id/password').send_keys('123')
driver.find_element_by_id('net.csdn.csdnplus:id/csdnsign_in_button').click()

xpath = "//*[contains(@text,'{}')]".format('用户名密码不能为空')
element = WebDriverWait(driver, 10, 0.1).until(lambda x: x.find_element_by_xpath(xpath))
print("toast=", element.text)

driver.quit()
