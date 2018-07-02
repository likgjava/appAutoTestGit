import time
import traceback

import pytest
from appium import webdriver

test_data = [("tom", "123", "192.168.120.101:5555", 4723), ("java", "666", "192.168.120.102:5555", 4733)]


@pytest.mark.parametrize('username,password,udid,port', test_data)
def test(username, password, udid, port):
    print('username={} password={} udid={} port={}'.format(username, password, udid, port))
    driver = get_driver(udid, port)
    time.sleep(5)

    try:
        driver.find_element_by_id("net.csdn.csdnplus:id/editTextUserName").send_keys(username)
        driver.find_element_by_id("net.csdn.csdnplus:id/password").send_keys(password)
        driver.find_element_by_id("net.csdn.csdnplus:id/csdnsign_in_button").click()
        time.sleep(5)
    except:
        traceback.print_exc()
    finally:
        driver.quit()


def get_driver(udid, port):
    print('get_driver udid={} port={}'.format(udid, port))
    cap = {'deviceName': 'e', 'udid': udid, 'platformName': 'Android', 'appPackage': 'net.csdn.csdnplus',
           'appActivity': '.activity.SplashActivity'}
    driver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(port), cap)
    driver.implicitly_wait(10)
    return driver


if __name__ == '__main__':
    pytest.main(['test_concurrent.py', '-s', '-n=auto'])
