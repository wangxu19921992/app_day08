from Page.new_sms_page import NewSmsPage
from Page.search_sms_page import SearchSmsPage
from Page.setting_page import SettingPage
from Page.sms_page import SmsPage



class Page:

    def __init__(self, driver):
        self.driver = driver

    def get_sms_page_obj(self):
        # 返回短信页面对象
        return SmsPage(self.driver)

    def get_new_sms_page_obj(self):
        # 返回新信息页面对象
        return NewSmsPage(self.driver)

    def get_search_sms_page_obj(self):
        # 返回搜索短信页面对象
        return SearchSmsPage(self.driver)

    def get_setting_page_obj(self):
        # 返回设置页面对象
        return SettingPage(self.driver)