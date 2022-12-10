'''
使用xpath路径定位策略完成下面操作
需求：
打开注册A.html页面，完成以下操作
1).使用绝对路径定位用户名输入框，并输入：admin
2).暂停2s
3).使用相对路径定位用户名输入框，并输入：123
'''

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(
    'file:///C:/Users/25071/Desktop/pythonProject/day04%E8%AF%BE%E5%A0%82%E7%BB%83%E4%B9%A0/work/%E6%B3%A8%E5%86%8CA.html')

# 绝对路径
message1 = driver.find_element_by_xpath('/html/body/form/div/fieldset/center/p/input')
message1.send_keys('admin')

time.sleep(2)
# 相对定位
message2 = driver.find_element_by_xpath('//p/input')
message2.send_keys('123')

time.sleep(5)
driver.quit()