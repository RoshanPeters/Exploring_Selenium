'''
Some of the keywords in python unittest framework are: 
 1)setup
  if multiple testmethods are created in a class using pyunittest, having a setup method in the class, the setup method will be executed before each testmethod is executed.
 2)teardown
  adding a teardown method in the class, it will get executed multiple times after each testmethod is executed.
 3)setUpClass
  this method will be executed only once before executing all the other testmethods.
 4)tearDownClass
  this method will be executed only once after executing all the testmethods.
 5)setUpModule
  will execute only once before the start of your model. It will be executed before executing any class or any method present in the test class.
 6)tearDownModule
  will execute only once after the completion of your module. It will be executed after executing any class or any method present in the test class.
 
'''
import unittest


def setUpModule():
  print("setUpModule")
  print()


def tearDownModule():
  print('tearDownModule')
  print()


class AppTesting(unittest.TestCase):

 @classmethod
 def setUp(self):
  print("This is login test")

 @classmethod
 def setUpClass(cls):
   print('open application')
   print()

 @classmethod
 def tearDownClass(cls):
   print('Thank you')
   print()

 def test_Testcase1(self):
  print("this is the first testcase")

 def test_Testcase2(self):
  print("this is the second testcase")

 def test_Testcase3(self):
  print("this is the Third testcase")

 @classmethod
 def tearDown(self) -> None:
  print('this is logout test')
  print()


if __name__ == '__main__':
 unittest.main()


