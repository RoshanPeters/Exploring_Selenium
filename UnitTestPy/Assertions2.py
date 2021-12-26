'''
assertTrue
 when we have only two parameter we can use assertEqual method to check whether both are same or not, but if we have more than two parameters, comparing values with assertEqual method become more difficult.
 assertTrue method checks whether given parameter is true or not, if value is true then test is passed otherwise thest is failed.

assertFalse
 assertFalse method compares whether given value or expression results in false or not.
 If the result or value is False then unittest passes the testcase but if the result or value is True then unittest fails the test case.
'''

import unittest
from selenium import webdriver

class Test(unittest.TestCase):
 def testName(self):
  self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
  self.driver.get("https://www.google.com/")
  titleofwebpage = self.driver.title
  self.assertTrue(titleofwebpage == "Google")
  # self.assertFalse(titleofwebpage == "Google123") # this statement is true
 
if __name__ == "__main__":
 unittest.main()

