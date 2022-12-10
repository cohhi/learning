### UI自动化



```
web 自动化 库  selenium
app 自动化 库  appium
```

cmd中 执行   安装selenium库

```shell
pip install selenium==3.14.0  #指定为版本

修改源 C:\user\用户名\pip\pip.ini 
没有文件就手动新建一个

pip list 查看所有安装的包信息
如果版本不一致则,卸载 pip uninstall selenium
```



下载浏览器驱动 `https://npm.taobao.org/mirrors/chromedriver`

PS:浏览器版本和驱动版本需一致(尽可能一致)

将下载的驱动放到python路径下

 

```python
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://bing.com')
time.sleep(5)
driver.quit()
```



网页中的元素定位

```
find_element_by_id			#id定位
find_element_by_name		#name定位
find_element_by_class_name	#class定位
find_element_by_tag_name	#标签定位
find_element_by_link_text   #根据内容定位

```

