'''
需求：打开注册B.html页面，完成以下操作
1.最大化浏览器
2.设置窗口大小为500,700
3.点击新浪
4.后退
5.前进
6.刷新
7.关闭浏览器
'''
import time

from selenium import webdriver


driver = webdriver.Chrome()
driver.get('file:///C:/Users/25071/Desktop/pythonProject/day05/%E6%B3%A8%E5%86%8CB.html')

time.sleep(1)
driver.maximize_window()   #最大化浏览器
time.sleep(1)
driver.set_window_size(500, 700)    # 设置大小
time.sleep(1)
message1=driver.find_element_by_css_selector('a')   #获取链接
message1.click()    #点击
time.sleep(1)
driver.back()   #后退
time.sleep(1)
driver.forward()   #前进
driver.refresh()    #刷新
time.sleep(1)
driver.quit()   #关闭浏览器
