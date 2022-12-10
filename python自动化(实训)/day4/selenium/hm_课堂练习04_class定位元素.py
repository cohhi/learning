'''
使用CLASS_NAME定位方式完成下面操作
需求：
打开注册A.html页面，完成以下操作
1).通过class_name定位电话号码A，并输入：18611111111
2).通过class_name定位电子邮箱A，并输入：123@qq.com
3).3秒后关闭浏览器窗口
'''

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(
    'file:///C:/Users/25071/Desktop/pythonProject/day04/work/selenium/%E6%B3%A8%E5%86%8CA.html')
time.sleep(1)
message1 = driver.find_element_by_class_name('telA')
message1.send_keys('admin')

message2 = driver.find_element_by_class_name('c1')
message2.send_keys('123@qq.com')
time.sleep(3)
driver.quit()
