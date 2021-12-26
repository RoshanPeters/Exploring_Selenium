'''
Navigation commands:
Helps you to navigate back (it will be stored in history) and forth between pages.
driver.back()
driver.forward()
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="chromedriver.exe")

driver.get("http://newtours.demoaut.com/")
time.sleep(5)

print(driver.title)  # print flight reservation page title

# opening a new page in the same browser
driver.get("http://pavantestingtools.blogspot.in/")
time.sleep(5)

print(driver.title)  # print testing tools page title

driver.back()  # it will go back to the flight reservation page
time.sleep(5)

print(driver.title)

driver.forward()  # will go to the testing tools page
time.sleep(5)

print(driver.title)

driver.close()
