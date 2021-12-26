import unittest

from TC_LoginTest import LoginTest
from TC_SignupTest import SignupTest

from TC_PaymentTest import PaymentTest
from TC_PaymentReturns import PaymentReturnsTest

# Get all tests from LoginTest, SignUpTest, PaymentTest and PaymentReturnsTests
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

'''
Sanity test suite only contains login and signup test cases
Functional test suite contains payment test cases
master test suite contains all test cases
'''
# creating test suites

# sanity test suites
sanityTestSuite = unittest.TestSuite([tc1, tc2])
# unittest.TextTestRunner().run(sanityTestSuite)  # this command will make sure that only sanity test suite is executed

# functional test suite
functionaltestsuite = unittest.TestSuite([tc3, tc4])
# unittest.TextTestRunner().run(functionaltestsuite)

# master test suite
mastertestsuite = unittest.TestSuite([tc1, tc2, tc3, tc4])
unittest.TextTestRunner(verbosity=2).run(mastertestsuite)  # verbosity will give detailed information in the console window
