# 需求：打开注册B.html页面，完成以下操作
# 方式1: 使用常规点击的方式实现下拉框选中
# 点击广州
# 点击上海
# 点击北京
import time

# 方式2: 使用Select类来实现
# 2、实例化Select对象
# 3、使用下标定位广州
# 使用value定位上海
# 使用文本定位 北京


from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('file:///C:/Users/25071/Desktop/pythonProject/day05/%E6%B3%A8%E5%86%8CB.html')

# 方法1
message1 = driver.find_element_by_css_selector('option[value="gz"]')
message1.click()
time.sleep(2)

message2 = driver.find_element_by_css_selector('option[value="sh"]')
message2.click()
time.sleep(2)
message3 = driver.find_element_by_css_selector('option[value="bj"]')
message3.click()


# 方法2
message1 = driver.find_element_by_css_selector('#selectA')
message2 = Select(message1)
message2.select_by_index(1)
time.sleep(2)
message2.select_by_index(2)
time.sleep(2)
message2.select_by_index(3)
# 根据索引选择

message2.select_by_value('bj')
time.sleep(2)
message2.select_by_value('sh')
time.sleep(2)
message2.select_by_value('gz')
time.sleep(2)
message2.select_by_value('cq')
# 根据value值选择

time.sleep(5)
driver.quit()
