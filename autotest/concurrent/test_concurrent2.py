import time
import traceback

import pytest
from appium import webdriver

from itcast.autotest.concurrent.utils import AdbUtil, SystemUtil, AppiumUtil


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


def get_user_list(size):
    users = []
    for i in range(size):
        users.append(User('user' + str(i), 'pwd' + str(i)))
    return users


def build_data():
    print('build_data...')
    # 获取设备列表
    devices = AdbUtil.get_devices()
    print('devices=', devices)

    # 获取可用的端口
    ports = SystemUtil.get_unused_port(4723, len(devices))
    print('ports=', ports)

    # 获取用户数据
    users = get_user_list(len(devices))
    print('users=', users)

    # 组装数据
    data = []
    for i in range(len(devices)):
        user = users[i]
        data.append((user.username, user.password, devices[i], ports[i]))
    print('data=', data)
    return data


@pytest.mark.parametrize('username,password,udid,port', build_data())
def test(username, password, udid, port):
    print('username={} password={} udid={} port={}'.format(username, password, udid, port))

    # 启动appium服务
    AppiumUtil.start_server(port)

    driver = get_driver(udid, port)
    time.sleep(10)
    print('start.................................username=', username)

    try:
        driver.find_element_by_id("net.csdn.csdnplus:id/editTextUserName").send_keys(username)
        driver.find_element_by_id("net.csdn.csdnplus:id/password").send_keys(password)
        driver.find_element_by_id("net.csdn.csdnplus:id/csdnsign_in_button").click()
    except:
        traceback.print_exc()
    finally:
        time.sleep(5)
        driver.quit()
        quit_appium_server(port)


def quit_appium_server(port):
    pid = SystemUtil.get_pid_by_port(port)
    SystemUtil.kill_with_pid(pid)


def get_driver(udid, port):
    cap = {'deviceName': udid, 'udid': udid, 'platformName': 'Android', 'appPackage': 'net.csdn.csdnplus',
           'appActivity': '.activity.SplashActivity'}
    driver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(port), cap)
    driver.implicitly_wait(10)
    return driver


if __name__ == '__main__':
    pytest.main(['test_concurrent2.py', '-s', '-n=auto'])
