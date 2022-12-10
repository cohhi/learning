"""
有如下的测试场景:
1.打开浏览器
2.打开网页, 进行登录功能的测试
3.在页面中输入正确用户名和正确密码之后进行登录
4.关闭当前页面
5.打开网页,进行登录功能的测试
6.在页面中输入错误的用户名和正确的密码之后进行登录
7.关闭当前页面
8.打开页面,进行登录功能的测试
9.在页面中输入正确的用户名和错误的密码之后进行登录
10.关闭当前页面
11.关闭浏览器
根据描述, 完成测试用例代码的编写
"""

import unittest
import time


class Test_Login(unittest.TestCase):
    # 测试用例
    def setUp(self):
        print("打开当前页面")
        startTime = time.time()
        self.startTime = startTime

    def tearDown(self):
        print("关闭当前页面")
        endTime = time.time()
        print("本次用时:{}".format(endTime - self.startTime))

    # 测试类
    @classmethod
    def setUpClass(cls) -> None:
        startTime = time.time()
        cls.startTime = startTime
        print("打开浏览器")

    @classmethod
    def tearDownClass(cls) -> None:
        print("关闭浏览器")

    def test_login_1(self):
        print("输入正确的用户名")

    def test_login_2(self):
        print("输入错误的用户名")

    def test_login_3(self):
        print("输入错误的密码")
