import unittest

from base.hm_testcase01 import TestDemo1
from base.hm_testcase02 import TestDemo2
from base.hm_testcase03 import TestDemo3
from base.hm_testcase04 import TestDemo4
from base.hm_testcase05 import TestDemo5
from base.hm_testcase06 import TestDemo6

message1 = unittest.makeSuite(TestDemo1)
message2 = unittest.makeSuite(TestDemo2)
message3 = unittest.makeSuite(TestDemo3)
message4 = unittest.makeSuite(TestDemo4)
message5 = unittest.makeSuite(TestDemo5)
message6 = unittest.makeSuite(TestDemo6)


