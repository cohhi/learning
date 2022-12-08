"""
需求：
1. 提示用户输入两个数字
2. 使用获取到的数据进行数学加法运算
3. 在控制台输出计算结果，格式要求：xx + xx = xx
"""

num1 = int(input("please enter one numbers:"))
num2 = int(input("please enter two numbers:"))

print("{}+{}={}".format(num1, num2, num1 + num2))
