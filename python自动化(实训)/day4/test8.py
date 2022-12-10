import unittest
import hm_21 as test

message = unittest.makeSuite(test.TestLogin)
runner = unittest.TextTestRunner()
runner.run(message)
