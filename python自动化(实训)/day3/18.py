"""
将base包下的 hm_testcase01和hm_testcase02的测试用例进行执行
"""

import unittest

from base import hm_testcase01
from base import hm_testcase02
from base import hm_testcase03
from base import hm_testcase04
from base import hm_testcase05
from base import hm_testcase06

a = unittest.TestSuite()
a.addTest(hm_testcase01.TestDemo1('test_001'))
a.addTest(hm_testcase01.TestDemo1('test_002'))
a.addTest(hm_testcase02.TestDemo2('test_003'))
a.addTest(hm_testcase02.TestDemo2('test_004'))
a.addTest(hm_testcase03.TestDemo3('test_005'))
a.addTest(hm_testcase04.TestDemo4('test_006'))
a.addTest(hm_testcase05.TestDemo5('test_007'))
a.addTest(hm_testcase06.TestDemo6('test_007'))

runner = unittest.TextTestRunner()  # 创建一个执行器
runner.run(a)
