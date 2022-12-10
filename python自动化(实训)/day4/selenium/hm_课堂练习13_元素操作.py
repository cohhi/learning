'''
使用元素定位的通用写法完成下面的操作
需求：打开注册B.html页面，完成以下操作
1).获取用户名输入框的大小
2).获取第一个a标签的内容
3).获取第一个a标签的href属性
4).判断span标签是否可见
5).判断#btn标签是否可用
6).判断#lyA标签是否被选中
'''

from selenium import webdriver
import time


def sleeps():
    time.sleep(2)


driver = webdriver.Chrome()
driver.get(
    'file:///C:/Users/25071/Desktop/pythonProject/day04/work/selenium/%E6%B3%A8%E5%86%8CB.html')
message1 = driver.find_element_by_id('userA')
print(message1.size)
sleeps()

message2 = driver.find_element_by_tag_name('a')
print(message2.text)
sleeps()

message3 = driver.find_element_by_tag_name('a')
print(message3.get_attribute('href'))
sleeps()

message4 = driver.find_element_by_tag_name('span')
print(message4.is_displayed())
sleeps()

message5=driver.find_element_by_id('btn')
print(message5.is_enabled())
sleeps()

message6=driver.find_element_by_id('lyA')
print(message6.is_selected())

driver.quit()