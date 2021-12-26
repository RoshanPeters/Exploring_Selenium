'''
There are some common operations in every DDT:
 finding number of rows
 finding number of columns
 reading the data
 writing data

If we write the code that interacts with the application and also the code that interacts with the excel file then there is no scope for the reusability of the excel code and also the code gets really big. For this reason we add the code that interacts with excel into another module called XLUtils.py. This module will contain functions for finding the number of rows, columns, and reading and writing data.

So now every test case can reuse the same function.
'''
from XLUtils import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="chromedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")
driver.maximize_window()
time.sleep(10)

path= r"C:\Users\ADMIN\Desktop\sel_testing.xlsx"
sheetname = "sheet"

rows = getRowCount(path, sheetname)

for r in range(2, rows+1):
 username = readData(path, sheetname, r, 1)
 password = readData(path, sheetname, r, 2)

 driver.find_element(
     By.XPATH, "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/input").send_keys(username)

 driver.find_element(
     By.XPATH, "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[3]/td[2]/input").send_keys(password)

 driver.find_element(
     By.XPATH, "/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[4]/td[2]/div/input").click()
 time.sleep(5)
 
 if driver.title == "Login: Mercury Tours":
  print("login successful")
  writeData(path, sheetname, r, 3, "login successful")
 else:
  print('login not successful')
  writeData(path, sheetname, r, 3, "login failed")

 # now we have to do this for the other users, for that we have to go back to the home page
 driver.find_element(
     By.LINK_TEXT, "SIGN-OFF").click()
