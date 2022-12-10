'''
使用xpath属性定位策略完成下面操作
需求：打开注册A.html页面。完成以下操作：
1). 利用元素的属性信息精准定位用户名输入框，并输入:admin
2). 利用元素的属性信息精准定位密码输入框，并输入:123456
3). 利用元素的属性信息精准定位电话号码输入框，并输入:13900000002
4). 利用元素的属性信息精准定位电话号码输入框:admin@itcast.cn
'''
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('file:///C:/Users/25071/Desktop/pythonProject/day04%E8%AF%BE%E5%A0%82%E7%BB%83%E4%B9%A0/work/%E6%B3%A8%E5%86%8CA.html')
message1 = driver.find_element_by_xpath('//p/input[@type="textA"]')
message1.send_keys("test")

message2=driver.find_element_by_xpath('//p/input[@type="password"]')
message2.send_keys("123456")

message3=driver.find_element_by_xpath('//p/input[@type="telA"]')
message3.send_keys("13900000002")

message4=driver.find_element_by_xpath('//p/input[@type="emailA"]')
message4.send_keys("admin@itcast.cn")
time.sleep(5)
driver.quit()
