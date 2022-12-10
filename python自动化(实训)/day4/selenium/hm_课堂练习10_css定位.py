'''
使用css定位完成下面操作
需求：打开注册A.html页面，完成以下操作
1).使用CSS定位方式中id选择器定位用户名输入框，并输入：admin
2).使用CSS定位方式中属性选择器定位密码输入框，并输入：123456
3).使用CSS定位方式中class选择器定位电话号码输入框，并输入：18600000000
4).使用CSS定位方式中元素选择器定位注册按钮，并点击
'''


from selenium import webdriver
import time

driver= webdriver.Chrome()
driver.get('file:///C:/Users/25071/Desktop/pythonProject/day04/work/selenium/%E6%B3%A8%E5%86%8CA.html')

message1=driver.find_element_by_css_selector('input[id="userA"]')
message1.send_keys('admin')
message2=driver.find_element_by_css_selector('input[type="password"]')
message2.send_keys('123456')
message3=driver.find_element_by_css_selector('input[class="telA"]')
message3.send_keys('18600000000')
time.sleep(2)
message4=driver.find_element_by_css_selector('button')
message4.click()

time.sleep(3)
driver.quit()