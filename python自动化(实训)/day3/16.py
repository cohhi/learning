import unittest
import TestCase16

a = unittest.TestSuite()

a.addTest(TestCase16.TestAdd('test_002'))
a.addTest(TestCase16.TestAdd('test_003'))
a.addTest(TestCase16.TestAdd('test_004'))

run = unittest.TextTestRunner()
run.run(a)
