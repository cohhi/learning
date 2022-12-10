# 计算两个任意累加数之和
def get_sum(start, end):
    total = 0
    for i in range(start, end + 1):
        total += i
    return total


import unittest


# 测试1-100   5050
# 测试1-10    55
# 测试0-0     0
class Test(unittest.TestCase):
    def test_1_100(self):
        result = get_sum(0, 100)
        if result == 5050:
            print("1-100功能正常")
        else:
            print("1-100功能异常")

    def test_1_10(self):
        result = get_sum(1, 10)
        if result == 55:
            print("1-10功能正常")
        else:
            print("1-10功能异常")

    def test_0_0(self):
        result = get_sum(0, 0)
        if result == 0:
            print("0-0功能正常")
        else:
            print("0-0功能异常")
