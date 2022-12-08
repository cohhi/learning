"""
需求：
1. 编写一个函数get_sum, 这个函数的作用是来计算1到100之间的累加和,将结果打印出来
2. 编写完之后, 调用这个函数
3. 如何让函数内部的功能更加灵活, 可以计算任意两个数之间的累加和
"""


def get_sum(num1, num2):
    sum = 0
    for i in range(num1, num2 + 1):
        sum += i

    return sum


print(get_sum(1, 100))
