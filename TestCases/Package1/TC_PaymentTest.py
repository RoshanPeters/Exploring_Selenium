import unittest

class PaymentTest(unittest.TestCase):
 def test_Paymentindollar(self):
  print('Payment has been done in dollar')
  self.assertTrue(True)
 
 def test_Paymentinrupees(self):
  print('Payment has been done in rupees')
  self.assertTrue(True)

if __name__ == "__main__":
 unittest.main()