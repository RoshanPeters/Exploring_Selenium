'''
operations:
1) How to find how many inputboxes are present in web page
2) How to provide value into text box
3) How to get the status
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(executable_path="chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
time.sleep(8)

# TO FIND NUMBER OF INPUT BOXES PRESENT IN WEBPAGE
# first we have to find the common attributes for all the textboxes 
# We can then use this attribute as our locater (find_elements)
inputboxes = driver.find_elements(By.CLASS_NAME, 'text_field')
print(f'there are {len(inputboxes)} input boxes in the webpage')

# TO GET THE STATUS OF THE WEBPAGE
status = driver.find_element(By.ID, 'RESULT_TextField-1').is_displayed()
print('displayed: ', status)  # it will return either true/false
status = driver.find_element(By.ID, 'RESULT_TextField-1').is_enabled()
print('enabled: ', status)  # it will return either true/false

# PROVIDING VALUE INTO THE TEXTBOX
# first we need to identify the element and then send_keys
driver.find_element(By.ID, 'RESULT_TextField-1').send_keys('Donald')
driver.find_element_by_id('RESULT_TextField-3').send_keys('1234567')


