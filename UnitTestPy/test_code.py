import unittest
from selenium import webdriver

class SearchEnginesTest(unittest.TestCase):
 def test_Google(self):
  self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
  self.driver.get("https://www.google.com/")
  print('title of the page: ', self.driver.title)
 
 def test_Bing(self):
  self.driver = webdriver.Chrome(executable_path='chromedriver.exe')
  self.driver.get("https://bing.com")
  print('title of the page is: ', self.driver.title)

if __name__=='__main__':
 unittest.main()
