"""
1. 输入用户年龄
2. 判断是否满 18 岁 （>=）
3. 如果满 18 岁，允许进网吧嗨皮
4. 如果未满 18 岁，提示回家写作业
"""

age = int(input("please enter age:"))
if age >= 18:
    print("进网吧嗨皮")
elif age < 18:
    print("回家写作业")
