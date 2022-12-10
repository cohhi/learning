import unittest
import test1

message = unittest.makeSuite(test1.Test)
# 套件

runner = unittest.TextTestRunner()

runner.run(message)
