def aaa():
    return "aaa"


import unittest


class Test(unittest.TestCase):
    def test_001(self):
        if aaa() == 'aaa':
            print("成功")
        else:
            print("失败")
