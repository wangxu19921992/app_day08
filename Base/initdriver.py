from appium import webdriver


# 定义一个driver驱动对象的方法并返回
def get_driver(package, activity):
    # server 启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    # desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # app的信息
    desired_caps['appPackage'] = package
    desired_caps['appActivity'] = activity
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 返回我们声明的driver驱动对象
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)