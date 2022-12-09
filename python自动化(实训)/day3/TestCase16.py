"""
书写TestCase最基本的使用, 测试tools中的add方法是否正确,完成3条测试用例,并执行
"""
import unittest
import tools


class TestAdd(unittest.TestCase):
    def test_001(self):
        print('aaa')

    def test_002(self):
        result = tools.add(1,2)
        if result == 3:
            print('成功')
        else:
            print("失败")

    def test_003(self):
        result = tools.get_sum(1, 2)
        if result == 3:
            print('成功')
        else:
            print("失败")

    def test_004(self):
        result = tools.age(4)
        if result == 4:
            print('成功')
        else:
            print("失败")
