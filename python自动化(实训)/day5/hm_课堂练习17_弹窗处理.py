# 需求：打开注册B.html页面，完成以下操作
# 点击alerta弹窗
# 获取弹窗对象
# 处理弹窗 同意/取消
# 找到#userA输入用户名


from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('file:///C:/Users/25071/Desktop/pythonProject/day05/%E6%B3%A8%E5%86%8CB.html')
time.sleep(2)
message1 = driver.find_element_by_id('confirma')
message1.click()
message2 = driver.switch_to.alert  # 弹出框对象
time.sleep(2)

message2.accept()  # 点击确认按钮
time.sleep(2)
message1 = driver.find_element_by_id('confirma')
message1.click()
message2 = driver.switch_to.alert  # 弹出框
message2.dismiss()  #点击取消
