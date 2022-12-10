'''
使用TAG_NAME定位方式完成下面操作
需求：
打开注册A.html页面，完成以下操作
1).使用tag_name定位用户名输入框，并输入：admin
2).3秒后关闭浏览器窗口
'''

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(
    'file:///C:/Users/25071/Desktop/pythonProject/day04/work/selenium/%E6%B3%A8%E5%86%8CA.html')
time.sleep(1)
message1 = driver.find_element_by_tag_name('input')
message1.send_keys('admin')
time.sleep(3)
driver.quit()
