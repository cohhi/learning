# 测试类
import unittest
import time


class TestLogin(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("\n")
        print("setUp...")
        start_time = time.time()
        self.start_time = start_time

    def tearDown(self):
        print("tearDown...")
        end_time = time.time()
        print("total time: " + str(end_time - self.start_time))

    @classmethod
    def setUpClass(cls) -> None:
        print("setupClass...")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass...")

    def test01(self):
        print('test01...')

    def test02(self):
        print('test02...')

    def test03(self):
        print('test03...')


class TestRegister(unittest.TestCase):
    def test04(self):
        print('test04...')

    def test05(self):
        print('test05...')

    def test06(self):
        print('test06...')
