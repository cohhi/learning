"""
将base包下的 hm_testcase01和hm_testcase02的测试用例使用make_suite的方式进行执行
"""

"""
将base包下的 hm_testcase01和hm_testcase02的测试用例进行执行
"""

import unittest

from hm import m3

a = unittest.TestSuite()
a.addTest(m3.Test('test_001'))

runner = unittest.TextTestRunner()  # 创建一个执行器
runner.run(a)
