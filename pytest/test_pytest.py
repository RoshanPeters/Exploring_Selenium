'''
The pytest frameword makes it easy to write small tests implemented on top of unittest.

pip install pytest

Run Pytest in terminal: pytest -v -s modulename
To execute the code for pytest we have to use the terminal

'test' keyword must be present in both the file name and the method name.
'''
import pytest

def testMethod1():
 print('this is test method1')

def testMethod2():
 print('this is test method2')

