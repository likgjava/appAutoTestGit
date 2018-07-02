import time

from appium import webdriver

cap = {'deviceName': 'emulator', 'platformName': 'Android', 'browserName': 'browser'}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)
driver.implicitly_wait(10)


def teardown():
    print('teardown...')
    driver.quit()


def test_search():
    print('test_search...')
    driver.get("http://m.baidu.com")
    print('start...')

    driver.find_element_by_xpath("//*[@id='index-kw']").send_keys("java")
    driver.find_element_by_id("index-bn").click()

    time.sleep(5)


test_search()
teardown()
