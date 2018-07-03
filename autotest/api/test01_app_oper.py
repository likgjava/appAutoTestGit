import time

from appium import webdriver

cap = {
    'platformName': 'Android',
    'deviceName': 'emulator',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)
time.sleep(5)

# 安装app
# driver.install_app("D://apk/zhihu.apk")

# 卸载app
# driver.remove_app("com.zhihu.android")

# 判断该应用是否已经安装
# installed = driver.is_app_installed("com.zhihu.android")
# print('installed=', installed)

# 关闭app
# driver.close_app()
# time.sleep(5)

# 启动app
# driver.launch_app()
# time.sleep(3)

# 让app在后台运行指定的秒数
# print('background_app start...')
# driver.background_app(5)
# print('background_app end...')

# 重置应用
# driver.reset()
# time.sleep(5)

# 获取当前包名和activity名
# current_package = driver.current_package
# current_activity = driver.current_activity
# print('current_package=', current_package)
# print('current_activity=', current_activity)

# 关闭驱动对象
driver.quit()
