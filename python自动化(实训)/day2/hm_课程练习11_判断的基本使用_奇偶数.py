"""'''
提示用户输入一个数字，判断这个数字是奇数还是偶数，输出最终结果
"""

number = int(input("please enter numbers"))

if number % 2 == 0:
    print("数字{}为偶数".format(number))
elif number % 2 != 0:
    print("数字{}为奇数".format(number))
