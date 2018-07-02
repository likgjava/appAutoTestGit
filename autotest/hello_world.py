# 导入appium库
from appium import webdriver

# 启动参数
cap = {
    'platformName': 'Android',  # 手机操作系统，Android、iOS、FirefoxOS
    'deviceName': 'emulator',  # 设备名称，该参数必须有，内容不为空就行。例如：emulator、MI6、OPPO R11
    'appPackage': 'com.android.settings',  # APP的包名
    'appActivity': '.Settings'  # APP的启动Activity名
}
# 创建驱动对象
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', cap)

# 向上滑动屏幕
driver.swipe(200, 700, 200, 200, 3000)

# 关闭驱动对象
driver.quit()
