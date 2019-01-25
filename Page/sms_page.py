from Base.base import Base
import Page


class SmsPage(Base):

    # 继承父类的方法
    def __init__(self, driver):
        Base.__init__(self, driver)

    def click_sms_btn(self):
        # 点击新建短信
        self.click_element(Page.new_sms_id)

    def click_search(self):
        # 点击搜索按钮
        self.click_element(Page.search_btn_id)

        # 点击设置页面

    # def send_receiver(self, tel):
    #     # 输入接收者号码
    #     self.send_element(Page.receiver_id, tel)

    # def send_sms(self, content):
    #     # 输入信息内容
    #     self.send_element(Page.send_sms_id, content)
    #     # 点击发送
    #     self.click_element(Page.send_btn_id)
    #
    # def get_result(self, text):
    #     # 获取短信文本内容断言
    #     result_list = self.search_elements(Page.result_list_id)
    #     assert text in [i.text for i in result_list]
