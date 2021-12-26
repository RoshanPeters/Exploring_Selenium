'''
Assertion is nothing but the check point or you can say it as verfication for the test cast to evaluate some item on the execution.

If we do not provide any assertion insided a test case then there is no way to know whether a test case is failed or not.

Assertion helps in report generation, based on the assertions the test execution report will be generated.

There are few assertion which will accept all the values and few assertions will accept only numeric values.

asserEqual
it compares the first parameter with the second parameter, if both matches the unittest will continue with the remaining execution but both the values are different then unit test fails the testcase.

asserNotEqual
this method compares the given two parameters, if both parameter are not same then unittest passes the test case but if both parameter are same then unittest fails the test case.
'''
import unittest
from selenium import webdriver

class Test(unittest.TestCase):
 def testName(self):
  self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
  self.driver.get("https://www.google.com/")
  titleofwebpage = self.driver.title

  # assertEqual() is used to compare the actual title and the expected title
  self.assertEqual("Google", titleofwebpage, "3rd parameter: both are the same ")
  # self.assertNotEqual("Google123", titleofwebpage, "3rd parameter: both are not the same") # this is a true statement

if __name__ == "__main__":
 unittest.main()