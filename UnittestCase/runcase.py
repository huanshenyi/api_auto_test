import sys
import os
sys.path.append(r"D:\program\automation_test\api_test")
import unittest

case_path = os.getcwd()
print(case_path)
# from UnittestCase.test_case01 import TestCase01
# from UnittestCase.test_case02 import TestCase02
# from UnittestCase.test_case03 import TestCase03
#
# case_01 = unittest.TestLoader().loadTestsFromTestCase(TestCase01)
# case_02 = unittest.TestLoader().loadTestsFromTestCase(TestCase02)
# case_03 = unittest.TestLoader().loadTestsFromTestCase(TestCase03)
# suote = unittest.TestSuite([case_01])
# unittest.TextTestRunner().run(suote)

# testの統合使用
discover = unittest.defaultTestLoader.discover(case_path)
unittest.TextTestRunner().run(discover)