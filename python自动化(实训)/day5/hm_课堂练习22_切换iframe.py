# 1、获取浏览器
# 2、打开Register.html网页
# 3.能否在当前页面中找到#user的元素
# 4.能否在当前页面中找到#userA的元素
# 5.将注册A网页定位出来
# 6.切换到注册A的网页定位#userA,输入admin
# 7.切回默认网页
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('file:///C:/Users/25071/Desktop/pythonProject/day05/Register.html')
driver.implicitly_wait(3)
message1 = driver.find_element_by_css_selector('#user')
message1.send_keys('admin')
time.sleep(1)
# 找到子网页元素
iframe = driver.find_element_by_css_selector("#idframe1")
driver.switch_to.frame(iframe)  # 切换到子网页
message2 = driver.find_element_by_css_selector('#userA')
message2.send_keys('admin')
time.sleep(1)
driver.switch_to.default_content()  # 切换到主网页

message3 = driver.find_element_by_css_selector('#user')
message3.send_keys('鸡你太美')
time.sleep(5)
driver.quit()
