# 1.打开注册A.html
# 2.开启全局的隐式等待
# 3、使用显示等待找到#userA, 输入文字admin
# 4、关闭浏览器


from selenium import webdriver
import time

driver= webdriver.Chrome()
driver.get('file:///C:/Users/25071/Desktop/pythonProject/day05/%E6%B3%A8%E5%86%8CB.html')
driver.implicitly_wait(5)
message1=driver.find_element_by_id('userA')
message1.send_keys('admin')
time.sleep(2)
driver.quit()