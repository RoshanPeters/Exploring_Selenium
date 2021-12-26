'''
If we have a testclass and there is a testmethod that is not completed or having an issue, we have to skip that particular method.
In pyunittest we have three ways to do this:
 skip test
 skip test with reason
 skip test with based on condition
'''
import unittest

class AppTesting(unittest.TestCase):

 def test_Testcase1(self):
  print("this is the first testcase")
 
 @unittest.skip("I am skipping testcase2 because it is not yet ready")
 def test_Testcase2(self):
  print("this is the second testcase")
  print()
 
 @unittest.skipIf(1==1, 'skipping testcase3 because condition not satisfied')
 def test_Testcase3(self):
  print("this is the third testcase")
  print()
 
 @unittest.SkipTest
 def test_Testcase4(self):
  print("this is the fourth testcase")
  print()
 
 def test_Testcase5(self):
  print("this is the fifth testcase")

if __name__ == '__main__':
 unittest.main()
