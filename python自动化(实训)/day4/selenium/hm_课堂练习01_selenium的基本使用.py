'''
使用selenium打开浏览器, 跳转到 百度 网站, 过3s后关闭浏览器
'''
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
time.sleep(5)
driver.quit()
