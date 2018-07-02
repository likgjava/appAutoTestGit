import time

from appium import webdriver

cap = {'deviceName': 'emulator', 'platformName': 'Android', 'appPackage': 'net.csdn.csdnplus',
       'appActivity': '.activity.SplashActivity', 'unicodeKeyboard': 'true', 'resetKeyboard': 'true'}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)

time.sleep(5)

context = driver.context
print('context=', context)

contexts = driver.contexts
print('contexts=', contexts)

driver.find_element_by_id('net.csdn.csdnplus:id/editTextUserName').send_keys('likg_java')
driver.find_element_by_id('net.csdn.csdnplus:id/password').send_keys('meimima')
driver.find_element_by_id('net.csdn.csdnplus:id/csdnsign_in_button').click()

time.sleep(5)
driver.quit()
