from Base.base import Base
import Page


class NewSmsPage(Base):
    # 继承父类的方法
    def __init__(self, driver):
        Base.__init__(self, driver)

    def send_receiver(self, tel):
        # 输入接收者号码
        self.send_element(Page.receiver_id, tel)

    def send_sms(self, content):
        # 输入信息内容
        self.send_element(Page.send_sms_id, content)
        # 点击发送
        self.click_element(Page.send_btn_id)

    def get_result(self):
        # 获取短信文本内容断言
        result_list = self.search_elements(Page.result_list_id)
        return [i.text for i in result_list]
