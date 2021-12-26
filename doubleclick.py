from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

# DOUBLE CLICK
driver1 = webdriver.Chrome(executable_path="chromedriver.exe")
driver1.get("https://testautomationpractice.blogspot.com")
driver1.maximize_window()
time.sleep(8)
# find the element to be double clicked
element = driver1.find_element(By.XPATH, "//*[@id='HTML10']/div[1]/button")
action2 = ActionChains(driver1)
action2.double_click(element).perform()  # double click the element
