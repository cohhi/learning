'''
使用css定位完成下面操作
需求：打开注册A.html页面，完成以下操作
1). 使用CSS定位方式定位用户名输入框，并输入：admin
2). 使用CSS定位方式定位密码输入框输入:123456
'''

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('file:///C:/Users/25071/Desktop/pythonProject/day04/work/selenium/%E6%B3%A8%E5%86%8CA.html')

message1 = driver.find_element_by_css_selector('input')
message1.send_keys('admin')

message2=driver.find_element_by_css_selector('input[type=password]')
message2.send_keys('123456')
time.sleep(5)

driver.quit()