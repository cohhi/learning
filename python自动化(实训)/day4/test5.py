import unittest

loader = unittest.TestLoader()
message1 = loader.discover('./base', 'hm*')
runner = unittest.TextTestRunner()
runner.run(message1)
