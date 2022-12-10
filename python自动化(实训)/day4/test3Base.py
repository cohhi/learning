import unittest
from base import hm_testcase01
from base import hm_testcase02

message1 = unittest.makeSuite(hm_testcase01.TestDemo1)
message2 = unittest.makeSuite(hm_testcase02.TestDemo2)

message1.addTest(message2)

runner = unittest.TextTestRunner()

runner.run(message1)
