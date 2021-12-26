'''
dropdown box is an element, and all the options inside the dropdown menu is also an element.
from selenium.webdriver.support.ui import Select

we will create an object of select class it will take web element as a parameter. And using this object we can select the options in the drop down.
There are 3 different ways to select from the drop down.

Operations:
1) select one option from the drop down
2) capture all the options that exist in drop down
3) count the number of options that is there in the drop down
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")


driver.maximize_window()
time.sleep(10)

element = driver.find_element(By.ID, "RESULT_RadioButton-9")
drp = Select(element)

# COUNT NUMBER OF OPTIONS
opts = drp.options  # options will return all the options in the drop down menu
print('The number of options in the drop down: ', len(opts))  # opts is stored as a list variable

# CAPTURE ALL OPTIONS
# capture all the options and print them as output
for i in opts:
 print('This is an option: ', i.text)

# SELECT BY VISIBLE TEXT
drp.select_by_visible_text('Morning')
time.sleep(5)

# SELECT BY INDEX
# the index numbers start from zero
drp.select_by_index(2)  # selecting afternoon
time.sleep(5)

# SELECT BY VALUE
# the value is extracted from html
drp.select_by_value('Radio-2')  # selecting evening
time.sleep(5)

driver.close()