from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="chromedriver.exe")

driver.get("https://www.facebook.com/?stype=lo&jlou=Afcvdi5qyJuwL1JCLrwzhJSFQtapbKAYEcpI8YviP2qBsbu3h30uSnR-Mf7OPahN3RE8J9RNOWbeNhKObDmT-DpUwz3QCyk-svffb63EP5mLwQ&smuh=21224&lh=Ac8rLSnshmp7vUTLHIo")

# to verify whether username and password textbox is displayed or not and also if it is enabled or not
ele = driver.find_element_by_name("email")
print(ele.is_displayed())  # return a true or false based on element status
print(ele.is_enabled())  # return a true or false based on element status
# this can be done using the password element as well

# typing in the password
ele.send_keys("trial@gmail.com")

# checking the status of the radio button
rnd_trip_ele = driver.find_element_by_css_selector("input[value=roundtrip]")
print(rnd_trip_ele.is_selected())  # print status of radio button/ can also be used for checkboxes and sometimes used for dropdown boxes as well



