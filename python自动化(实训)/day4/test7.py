# 每一条测试用例的时间

import time
import unittest

import hm_课堂练习21_Fixture的引入 as test

message = unittest.makeSuite(test.TestLogin)
runner = unittest.TextTestRunner()
runner.run(message)

