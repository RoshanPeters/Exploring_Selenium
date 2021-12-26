'''
assertIsNone
this method verifies whether given values or expression results in None or not, if the result is none then python unittest will pass the test case otherwise fails the testcase.

assertIsNotNone
this method verifies whether given values is not None, if the value is None then the test case will be failed.
'''
import unittest
from selenium import webdriver

class Test(unittest.TestCase):
 def testName(self):
  self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
  # check whether driver variable is initiated or not
  self.assertIsNone(self.driver)  # this will verify whether the driver variable contains some value or not
  
  # self.assertIsNotNone(self.driver)
  
if __name__ == "__main__":
 unittest.main()
