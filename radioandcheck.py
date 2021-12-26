'''
Only one radio button can be selected at a time.
Multiple check boxed can be selected at a time.

Operations:
1) Verify whether the radio or check is selected or not
2) click 
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# working with radio button
status = driver.find_element_by_id("RESULT_RadioButton-8_0").is_selected()
print(status)
driver.find_element_by_id("RESULT_RadioButton-8_0").click()
status = driver.find_element_by_id("RESULT_RadioButton-8_0").is_selected()
print(status)

# working with checkboxes
driver.find_element_by_id("RESULT_CheckBox-9_0").click()
driver.find_element_by_id("RESULT_CheckBox-9_6").click()
status = driver.find_element_by_id("RESULT_CheckBox-9_0").is_selected()
print(status)
