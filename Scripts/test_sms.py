import os, sys
sys.path.append(os.getcwd())
import pytest, allure

from Base.page import Page
from Base.initdriver import get_driver


class Test_Send_Sms:
    @allure.step(title="第一步:初始化数据")
    def setup_class(self):
        # 导入driver
        self.driver = get_driver("com.android.mms", ".ui.ConversationList")
        # 实例化统一入口类
        self.page_obj = Page(self.driver)
    @allure.step(title="第四步:退出驱动对象")
    def teardown_class(self):
        # 退出驱动对象
        self.driver.quit()
    @allure.step(title="第二步:点击新建短信,输入联系人")
    @pytest.fixture(scope="class", autouse=True)  # 作为条件依赖 只执行一次
    def test_click_sms_btn(self):
        # 点击新建短信
        self.page_obj.get_sms_page_obj().click_sms_btn()
        # 输入联系人
        self.page_obj.get_new_sms_page_obj().send_receiver(13212341234)
    @allure.step(title="第三步:输入短信内容123,王旭,abcdefg")
    @pytest.mark.parametrize("sms_data", ["123", "王旭", "abcdefg"])
    def test_send_sms_text(self, sms_data):
        # 输入内容 # 点击发送
        self.page_obj.get_new_sms_page_obj().send_sms(sms_data)
        # 获取结果列表断言
        assert sms_data in self.page_obj.get_new_sms_page_obj().get_result()
