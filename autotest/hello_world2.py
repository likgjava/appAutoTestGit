# 1.导包
from appium import webdriver

# 启动参数
cap = {
    "platformName": "Android",  # 手机操作系统，Android，iOS
    "deviceName": "emulator",  # 设备名称，参数必须要有，但是内容不空就行，MI 6，OPPO　R11
    "appPackage": "com.android.settings",  # app包名
    "appActivity": ".Settings",  # 启动Activity名称
}

# 2.启动APP，创建驱动对象
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", cap)

# 3.向上滑动屏幕
driver.swipe(200, 680, 200, 180, 3000)

# 4.退出驱动
driver.quit()
