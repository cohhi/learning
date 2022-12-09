"""
1. 定义⼀个模块 tools.py , 在模块中定义⼀个函数,sum_2_num(), 可以对两个数字求和
2. 新定义⼀个代码⽂件, 调⽤ tools.py ⽂件中的,sum_2_num() 函数, 对 10 和 20 求和
    使用两种方式实现
"""
import tools

print(tools.get_sum(10, 20))

print(tools.age())

"""
1. 生成一个随机数, 范围在1到10之间, 将生成的随机数打印出来
2. 在同个目录下, 创建一个random.py的文件
3. 在此执行本文件, 为什么执行不了了
student: 因为和系统内置模块重复
"""

import random

print(random.randint(1, 10))
