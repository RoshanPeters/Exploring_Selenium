'''
Commands:

Run all tests in a module/file
 pytest -v -s test_Login.py
 pytest -v -s test_SignUp.py

Run all tests(from all modules) in a path
 pytest -v -s C:\Users\admin\PycharmProjects\SeleniumwithPython\myPack\

Run specific test method from a module
 pytest -v -s test_Login.py::test_loginbyfacebook  # here test_Login is the test case and test_loginbyfacebook is a testmethod in the testcase

test case = test modules
'''