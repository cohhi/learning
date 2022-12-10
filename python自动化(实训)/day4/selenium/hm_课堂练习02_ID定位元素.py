'''
使用ID定位方式完成下面操作
需求：
打开注册A.html页面，完成以下操作
1).使用id定位，输入用户名：admin
2).使用id定位，输入密码：123456
3).3秒后关闭浏览器窗口
'''
import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('file:///C:/Users/25071/Desktop/pythonProject/day04/work/selenium/%E6%B3%A8%E5%86%8CA.html')
time.sleep(2)
message1 = driver.find_element_by_id('userA')
message1.send_keys('admin')
time.sleep(1)
message2 = driver.find_element_by_id('passwordA')
message2.send_keys('123456')
time.sleep(3)
driver.quit()
