import unittest

from script import test_login

message = unittest.makeSuite(test_login.TestLogin)
runner = unittest.TextTestRunner()
runner.run(message)
