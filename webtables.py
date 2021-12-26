'''
working with tables:
to read the data in the web table
extract rows and columns from the table
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="chromedriver.exe")

driver.get("https://www.w3schools.com/html/html_tables.asp")

# to read the rows we have to perform for loop
# we have to know the number of rows and columns to know how many times we repeat the loop

tr = driver.find_elements(By.XPATH, "//*[@id='customers']/tbody/tr")  # we have to remove the row number ([1]) to get the general xpath of all the rows of the table

# number of rows
rows = len(tr)
print('the number of rows in the table: ', rows)

# To get the general xpath form of columns of the table we need to remove the  column number from one of the element (//*[@id="customers"]/tbody/tr[1]/th[1]) in table
tc = driver.find_elements(By.XPATH, "//*[@id='customers']/tbody/tr[1]/th")

# number of columns
columns = len(tc)
print('number of columns: ', columns)

# printing the header
print("Company"+"                       " +"Contact"+"                       "+"Country")
# reading the data from the table
# within the for loop you have to pass the row and column number dynamically.
for r in range(2, rows+1):
 for c in range(1, columns+1):
  # we use the text method to extract the value from that location
  value = driver.find_element(By.XPATH, "//*[@id='customers']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text  # text is a property, not a function. Use it without ()
  # for printing it in the same line
  print(value, end="                       ")
 print()  # to jump to the next line

driver.close()

