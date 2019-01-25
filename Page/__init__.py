from selenium.webdriver.common.by import By
"""短信页面元素"""
# 1.点击新建短信页面
new_sms_id = (By.ID, "com.android.mms:id/action_compose_new")
# 1.1.接受者
receiver_id = (By.ID, "com.android.mms:id/recipients_editor")
# 1.2. 返回上级
return_class = (By.CLASS_NAME, "android.widget.LinearLayout")
# 1.3. 附件
attachment_class = (By.CLASS_NAME, "android.widget.TextView")
# 1.4.更多设置按钮
more_btn_class = (By.CLASS_NAME, "android.widget.ImageButton")
# 1.4.1 添加主题
# 1.4.2 舍弃
# 1.4.3 设置
# 1.5 输入信息
send_sms_id = (By.ID, "com.android.mms:id/embedded_text_editor")
# 1.6 点击发送按钮
send_btn_id = (By.ID, "com.android.mms:id/send_button_sms")
# 获取短信发送结果列表
result_list_id = (By.ID, "com.android.mms:id/text_view")

# 2.搜索按钮页面
search_btn_id = (By.ID, "com.android.mms:id/search")
# 2.1 搜索短信
search_sms_id = (By.ID, "android:id/search_src_text")
# 2.2 返回上一级
search_return_class = (By.ID, "android.widget.FrameLayout")

# 3.设置按钮页面
setting_btn_id = (By.ID, "android.widget.ImageButton")
# 3.1 设置
setting_id = (By.XPATH, "//*[contains(@text,设置)]")
