# 打开 百度
# 点击新闻
# 在新闻页面中的输入框, 输入内容
# 回到百度的页面上, 在输入框输入内容


from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.implicitly_wait(3)
message = driver.find_element_by_link_text('新闻')
message.click()
sleep(2)

driver.switch_to.window(driver.window_handles[1])
message1=driver.find_element_by_id('ww')
message1.send_keys('鸡你太美')
message2=driver.find_element_by_id('s_btn_wr')
message2.click()

sleep(5)

driver.quit()



'''

'''
