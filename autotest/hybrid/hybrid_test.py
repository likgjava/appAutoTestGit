import time

from appium import webdriver

cap = {'platformName': 'Android', 'deviceName': 'emulator', 'appPackage': 'net.csdn.csdnplus',
       'appActivity': '.activity.SplashActivity'}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)
driver.implicitly_wait(10)


def teardown():
    print('teardown...')
    driver.quit()


def test():
    print('test...')
    driver.find_element_by_id("net.csdn.csdnplus:id/editTextUserName").send_keys("likg_java")
    driver.find_element_by_id("net.csdn.csdnplus:id/password").send_keys("meimima")
    driver.find_element_by_id("net.csdn.csdnplus:id/csdnsign_in_button").click()
    driver.find_element_by_xpath("//android.widget.Button[@text='关闭']").click()

    xpath = "//android.widget.ListView[@resource-id='android:id/list']//android.widget.LinearLayout[@index=0]"
    driver.find_element_by_xpath(xpath).click()
    time.sleep(5)

    context = driver.current_context
    print('context=', context)
    contexts = driver.contexts
    print('contexts=', contexts)

    page_source = driver.page_source
    print('page_source=', page_source)

    driver.switch_to.context(contexts[1])
    print('context=', driver.context)

    page_source = driver.page_source
    print('page_source=', page_source)
    print('----------------------------------------------------')

    time.sleep(3)

    img_list = driver.find_elements_by_tag_name('img')
    for img in img_list:
        print('src=', img.get_attribute('src'))

    time.sleep(5)


test()
teardown()
