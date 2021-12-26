'''
Relational comparison:

assertGreater
it verifies whether first values is greater than second value or not.

assertGreaterEqual verifies whether first parameter is greater or equal to the second parameter.

assertLess 
verifies whether fist parameter is lesser than second paramter or not.

asserLessEqual 
verifies whether first parameter is lesser or equal to the second parameter.
'''
import unittest

class Test(unittest.TestCase):
 def testName(self):
  #assertGreater
  self.assertGreater(100,10)  # the test case will be passed if the first value is greater than the second value

  self.assertGreaterEqual(100, 100)  # the test case will be passed if the first value is greater than or equal to the second value
  
  self.assertLess(10, 100)  # the test case will be passed if the first value is lesser than or equal to the second value

  self.assertLessEqual(100, 100)  # the test case will be passed if the first value is lesser than or equal to the second value

if __name__ == "__main__":
 unittest.main()