"""
需求：
1. 编写一个函数get_sum, 这个函数的作用是来计算1和100这两个数的和, 并将结果打印出来
2. 编写完之后, 调用这个函数
3. 再调用这个函数
4. 再调用这个函数
"""


def get_sum(num1, num2):
    sum = 0
    for i in range(num1, num2 + 1):
        sum += i

    return sum


print(get_sum(1, 100))
