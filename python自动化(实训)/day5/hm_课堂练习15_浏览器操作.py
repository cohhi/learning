# 需求：打开注册B.html页面，完成以下操作
# 获取当前窗口标题
# 获取当前窗口url
# 获取 访问 新浪 网站 按钮, 并点击进行页面跳转
# 获取当前窗口标题
# 获取当前窗口url
# 关闭当前窗内口

from selenium import webdriver
import time


def sleep1Second():
    time.sleep(1)


driver = webdriver.Chrome()
driver.get('file:///C:/Users/25071/Desktop/pythonProject/day05/%E6%B3%A8%E5%86%8CB.html')
sleep1Second()
print("标题:{}".format(driver.title))
sleep1Second()
print("url:{}".format(driver.current_url))
sleep1Second()
message1 = driver.find_element_by_css_selector('a')  # 获取链接
message1.click()
sleep1Second()
print("标题:{}".format(driver.title))  # 跳转后的标题
sleep1Second()
print("url:{}".format(driver.current_url))  # 获取url
sleep1Second()
driver.quit()
