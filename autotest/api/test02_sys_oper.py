import base64
import time

from appium import webdriver

cap = {
    'platformName': 'Android',
    'deviceName': 'emulator',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)

# 获取设备时间
# device_time = driver.device_time
# print('device_time=', device_time)

# 获取屏幕宽高
# window_size = driver.get_window_size()
# print(window_size)

# 获取设备当前的网络类型
# network_connection = driver.network_connection
# print(network_connection)

# 设置网络类型
# 设置网络类型为飞行模式
# driver.set_network_connection(1)


# 打开通知栏
# driver.open_notifications()
# time.sleep(3)

# 操作手机按键
# 调大音量
# driver.keyevent(24)
# time.sleep(3)

# 横竖屏切换
# 获取屏幕朝向
# orientation = driver.orientation
# print('orientation=', orientation)
# 切换成横屏
# driver.orientation = 'landscape'
# time.sleep(3)
# 切换成竖屏
# driver.orientation = 'portrait'
# time.sleep(3)

# 截屏操作
# driver.get_screenshot_as_file('./image/img.png')


# 文件操作
# 上传文件
# 将字符串转换为base64格式的数据，并写到设备的指定文件中
# data = base64.b64encode("python中国666".encode()).decode()
# driver.push_file("/sdcard/t1.txt", data)

# 下载文件
data = driver.pull_file("/sdcard/t1.txt")
print('data=', base64.b64decode(data).decode())


# 关闭驱动对象
driver.quit()
