# 需求：打开注册B.html页面，完成以下操作
# 练习 1
# 查找注册按钮
# 调用悬停方法
# 练习2
# 查找#userA输入框
# 右击

# 练习3 找到#userA,输入admin
# 双击

from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('file:///C:/Users/25071/Desktop/pythonProject/day05/%E6%B3%A8%E5%86%8CB.html')
sleep(1)
message1 = driver.find_element_by_css_selector('button[value="注册A"]')
message2 = ActionChains(driver)  # 鼠标操作联
message2.move_to_element(message1)
message2.perform()

sleep(3)

message3 = driver.find_element_by_id('userA')
message4 = ActionChains(driver)
message4.context_click(message3)
message4.perform()
sleep(3)


message5=driver.find_element_by_id('userA')
message5.send_keys('admin')
message6=ActionChains(driver)
message6.double_click(message5)
message6.perform()
driver.quit()
