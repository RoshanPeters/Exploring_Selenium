'''
All the links have the common attribute- anchor tag
We can use this tag name as a locator.

operations:
1) how many link present
2) Capture all the links in a webpage
3) click on the link (LINK_TEXT and PARTIAL_LINK_TEXT)
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="chromedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/")
time.sleep(15)

lnks = driver.find_elements(By.TAG_NAME, "a")  # the variable lnks contains all the links in the webpage.

# NUMBER OF LINKS IN WEBPAGE
print('The number of links present in a page: ', len(lnks))

# CAPTURING ALL THE LINKS IN THE PAGE
for l in lnks:
 print('This is a link: ', l.text)  # we are extracting the text from l

# CLICKING THE LINK
# if you are using LINK_TEXT we have to provide the entire link text and if you are using PARTIAL we can just provide the substring of the link text
ln = driver.find_element(By.LINK_TEXT, "REGISTER")  
ln.click()
time.sleep(10)

driver.find_element(By.PARTIAL_LINK_TEXT, "Fligh").click()  # LINK_TEXT = "Flights"
time.sleep(10)

driver.close()

