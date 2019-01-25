from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    def search_element(self, fuc, timeout=15, poll_frequency=1):
        # 定位单个元素
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*fuc))

    def search_elements(self, fuc, timeout=15, poll_frequency=1):
        # 定位多个元素
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_elements(*fuc))

    def click_element(self, fuc, timeout=15, poll_frequency=1):
        # 常用的点击操作
        self.search_element(fuc, timeout, poll_frequency).click()

    def send_element(self, fuc, text, timeout=15, poll_frequency=1):
        # 常用的输入操作
        elements = self.search_element(fuc, timeout, poll_frequency)
        elements.clear()
        elements.send_keys(text)