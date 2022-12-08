'''
需求：
1. 定义一个整数变量记录年龄
2. 判断是否满 18 岁 （>=）
3. 如果满 18 岁，允许进网吧嗨皮
'''

age = int(input("please enter age:"))

if age >= 18:
    print("可以进入网吧")
elif age < 18:
    print("未成年")
