### 最后一天

```
from selenium.webdriver.common.by import By
元素定位    find_element()     通用方法
格式:		(定位方式:值)
find_element(By.ID,'userA')
```

### 浏览器操作

```
driver.close()		#关闭窗口
driver.maximize_window()	#浏览器最大化
driver.set_window_size(长度, 宽度)    #调整窗口大小
driver.set_window_position(x坐标，y坐标)	#设置位置  左上角为0,0
driver.back()	#后退
driver.forward()	#前进
driver.refresh()	#刷新
driver.title		#获取网页标题
```

### 特殊操作

```
select方法  用于解决下拉列表
from selenium.webdriver.support.select import Select
变量1=driver*****("选中")
变量2=Select(变量1)
变量2.select_by_index(数字)		#根据索引选择
变量2.select_by_value('值')		#根据value选择
```

### 网页弹窗

```
变量=driver.switch_to.alert   #弹出框实例对象
变量.message2.accept()	#点击 确定按钮
变量.dismiss()
```

### 浏览器滚动

```js
driver.execute_script('这里放js代码')	#需要字符串类型
```

```javascript
//通过console执行js代码
windows.scrollTo(x移动距离,Y移动距离)
windows.scrollTo(0,0)   //滚动到最顶部
windows.scrollTo(0,document.body.scrollHeight)  //滚动到最底部
```

### 鼠标操作

```python
需先导入：
	from selenium.webdriver import ActionChains
悬停:
	message1=driver.find_element....('值')
	message2=ActionChains(driver)  
	message2.move_to_element(message1)
	message2.perform()
	
右击:
	message1=driver.find_element....('值')
	message2=ActionChains(driver)  
	message2.context_click(message1)
	message2.perform()
	
最后要调用perform()才能产生效果

双击:
	message1=driver.find_element....('值')
	message2=ActionChains(driver)  
	message2.double_click(message1)
	message2.perform()

拖拽:
    message1=driver.find_element...('...')
    message2=driver.find_element...('...')
    message3=ActionChains(driver)
    message3.drag_and_drop(message1,message2)	#拖拽元素1到元素2的位置
    message3.perform()
    
#注意:要添加perform()才有效果	
```

### 高级`API`

- 元素等待

  ```python
  #强制等待：
  	import time
  	time.sleep()
  #隐式等待:
  	driver.implicitly_wait(5)	#5秒
      #全局生效  
      #特点:在等待的元素中，不断获取元素，直到获取成功（规定时间没找到会报错）
  #显示等待
  	from selenium.webdriver.support.wait import WebDriverWait
      
  	#针对某一个元素查找的等待，不断获取元素，直到获取成功（规定时间没找到会报错）
  ```

  

- `iframe`切换

  ```python
  #将driver切换到子网页中
  	iframe = driver.find_element...("值")
  	driver.switch_to.frame(iframe)  # 切换到子网页
      driver.switch_to.default_content()  #切换到主网页
  ```

- 多窗口切换

  ```python
  driver.switch_to.window(driver.window_handles[1])
  #window_handles[1]  获取新窗口第一个元素
  ```

  



### 登录案例自动化测试

