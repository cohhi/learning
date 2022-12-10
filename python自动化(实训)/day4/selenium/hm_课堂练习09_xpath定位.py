'''
1. 打开Tpshop首页； http://hmshop-test.itheima.net/Home/Index/index.html
2. 使用 Xpath 定位登陆超链接，并点击；
3. 使用 Xpath 定位用户名输入框，输入：15800000001；
4. 使用 Xpath 定位密码输入框，输入：123456；
5. 使用 Xpath 定位验证码输入框，输入：8888；
6. 使用 Xpath 定位登陆按钮，并点击；
每步操作之后暂停2s
'''

from selenium import webdriver
import time


# 睡眠函数
def sleeps():
    time.sleep(2)


driver = webdriver.Chrome()
driver.get('http://hmshop-test.itheima.net/Home/Index/index.html')
login = driver.find_element_by_xpath('//a[@class="red"]')
login.click()

sleeps()
message1=driver.find_element_by_xpath('//input[@id="username"]')
message1.send_keys('15800000001')
sleeps()
message2=driver.find_element_by_xpath('//input[@id="password"]')
message2.send_keys('123456')
sleeps()
message3=driver.find_element_by_xpath('//input[@id="verify_code"]')
message3.send_keys('8888')
sleeps()

message4=driver.find_element_by_xpath('//a[@name="sbtbutton"]')
sleeps()
message4.click()

time.sleep(5)
driver.quit()
