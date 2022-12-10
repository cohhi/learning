'''
使用Link_Text定位方式完成下面操作
需求：
打开注册A.html页面，完成以下操作
1).使用link_text定位(访问 新浪 网站)超链接，并点击
2).3秒后关闭浏览器窗口
'''

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(
    'file:///C:/Users/25071/Desktop/pythonProject/day04%E8%AF%BE%E5%A0%82%E7%BB%83%E4%B9%A0/work/%E6%B3%A8%E5%86%8CA.html')

message = driver.find_element_by_link_text('访问 新浪 网站')


message.click()

time.sleep(3)

driver.quit()
