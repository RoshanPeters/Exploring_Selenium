'''
pytest fixtures:
 The purpose of test fixtures is to provide a fixed baseline upon which tests can reliably and repeatedly execute.

@pytest.fixture()
 Executes specific method before every test method.

@pytest.yield_fixture()
 Executes specific method before and after every test method.
'''
import pytest

@pytest.fixture()
def setup():
 print("once before every method")

@pytest.yield_fixture()
def setup2():
 print('once before every method')
 yield
 print('once after every method')

def testmethod1(setup):
 print('this is test method1')

def testmethod2(setup):
 print('this is test method2')
 print()

def testmethod3(setup2):
 print('this is test method3')