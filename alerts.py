'''
Alert is a pop up. If we want to perform any actions on them, we can not directly identify them.
Alert window has two buttons: OK button and the Cancel Button.
'''
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
time.sleep(5)

# performing actions on the alert window
driver.switch_to_alert().accept()  # closes the alert window using the OK button
time.sleep(5)

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
time.sleep(5)

driver.switch_to_alert().dismiss()  # closes the alert window using the Cancel button
time.sleep(5)
