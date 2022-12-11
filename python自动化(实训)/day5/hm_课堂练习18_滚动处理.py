# 需求：打开注册B.html页面，完成以下操作
# 设置窗口大小 100 300
# js -> 向下滚动 0 5000
# 动态执行滑倒底部 document.body.scrollHeight
# 执行js方法
# js—> 向上 回到 0,0
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('file:///C:/Users/25071/Desktop/pythonProject/day05/%E6%B3%A8%E5%86%8CB.html')
driver.set_window_size(100, 300)
time.sleep(1)
driver.execute_script('window.scrollTo(0, 5000);')
time.sleep(1)
driver.execute_script('window.scrollTo(0, 0);')
time.sleep(1)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

time.sleep(5)
driver.quit()
