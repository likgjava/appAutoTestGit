import time
import traceback
import threading

from appium import webdriver


def test(udid, port):
    print("udid={} port={}".format(udid, port))
    driver = get_driver(udid, port)

    try:
        driver.find_element_by_xpath("//*[@text='显示']").click()
        time.sleep(3)
    except:
        traceback.print_exc()
    finally:
        driver.quit()


def get_driver(udid, port):
    print('get_driver udid={} port={}'.format(udid, port))
    cap = {
        'platformName': 'Android',
        'deviceName': 'e',
        'udid': udid,
        'appPackage': 'com.android.settings',
        'appActivity': '.Settings'
    }
    driver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(port), cap)
    driver.implicitly_wait(10)
    return driver


t1 = threading.Thread(target=test, args=("192.168.192.101:5555", 4723))
t2 = threading.Thread(target=test, args=("192.168.192.102:5555", 4733))
t1.start()
t2.start()
