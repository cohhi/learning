'''
使用元素定位的通用写法完成下面的操作
需求：打开注册A.html页面，完成以下操作
1).使用id定位用户名输入框，并输入：admin
2).使用name定位密码输入框，并输入：123456
3).使用class定位电话号码输入框，并输入：18600000000
4).使用标签名定位注册按钮，并点击
'''
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('file:///C:/Users/25071/Desktop/pythonProject/day04/work/selenium/%E6%B3%A8%E5%86%8CA.html')
message1 = driver.find_element_by_id('userA')
message1.send_keys('admin')
message1.send_keys('123456')

message2 = driver.find_element_by_name('passwordA')
message2.send_keys('123456')

message3 = driver.find_element_by_class_name('telA')
message3.send_keys('18600000000')
time.sleep(3)
message4 = driver.find_element_by_tag_name('button')
message4.click()
time.sleep(5)
driver.quit()
