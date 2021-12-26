'''
assertIn 
This method verifies whether the first element is present in the second selement, if the first element is present in second element then thest is passed otherwise test is failed.

asserNotIn 
This method verifies whether the first element is not present in the second element or not, if first element is present then test will be failed otherwise test is passed.

These two methods will be helpful when you want to verify presence of a value in a list, tuple, set and dictionary
'''
import unittest

class Test(unittest.TestCase):
 def testName(self):
  list = ['python', 'selenium', 'django']
  self.assertIn('python', list)

  # self.assertNotIn('Google', list)  # this is a true statement

if __name__ == "__main__":
 unittest.main()
