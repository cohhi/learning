# 需求：打开注册drop.html页面，完成以下操作
# 找到#div1和#div2
# 将div1拖拽到div2上去
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('file:///C:/Users/25071/Desktop/pythonProject/day05/drop.html')
# 托起元素1放入元素2
message1 = driver.find_element_by_id('div1')
message2 = driver.find_element_by_id('div2')
message3 = ActionChains(driver)
message3.drag_and_drop(message1, message2)
message3.perform()

time.sleep(3)
driver.quit()
