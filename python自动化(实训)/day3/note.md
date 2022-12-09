### 函数

- 用于存代码

```
def 函数名(参数):
	代码1
	代码2
	代码3
	return 返回值
	
函数名()  调用函数	
```

### 模块和包

- 使用import关键字导入

  ```python
  import random
  
  # 导入模块
  
  print(random.randint(1, 10))
  # 产生1-10随机数
  ```

- from关键字

  ```python
  #会按需,从模块中导入需要的东西
  
  from random import randint
  
  print(randint(1, 10))
  ```

  - 如果导入的名字比较长则可以重命名 as关键字
	```
	import 模块名 as  新名字
	from 模块名 import 方法名 as 新名字
	```
	
	

​      模块名不能和内置模块重名



- 包

  ```
  包是一个文件夹,包含py文件
  需要有一个__init__.py文件,文件可以不写，但必须有
  ```



### 面向对象

- 语法

  ```
  class 类名
  	def 方法1(self):
  		代码
      def 方法1(self):
          代码
          
  对象1=类名()
  对象2=类名()
  对象3=类名()
  ```

  对象增加属性

  ​	对象变量.属性=值

  ```python
  def  __init__(self,属性1,属性2)
  	self.属性1=属性1
      self.属性2=属性2
  
  #...就这样吧，不想写了
  ```

  



### 继承

面向对象三大特点

- 继承

  ```python
  解决代码重复
  
  class 类别1:
  	def 方法1(self):
          print("方法1")
  
  class 类别2(类别1):
      def 方法2(self):
          print("方法2")
  ```

  

- 封装

  ```
  通过class定义  通过def添加方法
  ```

  

- 多态

  ```
  pass     # 懒得写了
  ```

  ### unittest
  
  ```
  python自带的单元测试框架
  
  pythontest 第三方测试框架,需要额外安装
  ```
  
  `unittest`组成
  
  ```
  TestCase	测试用例代码
  TestSuite	测试套件
  TestRunner	测试用例的执行器
  TestLoader	测试用例的加载器
  Fixture
  ```
  
  
  
  ### `unittest` 基本使用
  
  ```
  1.写一个类,以test开头,继承unittest.TestCase
  2.定义方法以test开头
  3.执行代码
  ```
  
  