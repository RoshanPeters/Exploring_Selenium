'''
The different operations with mouse:
1)Mouse Hover
2)Double Click
3)Right Click
4)Drag and Drop
'''
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

driver.find_element(By.ID, "txtUsername").send_keys("Admin")
driver.find_element(By.ID, "txtPassword").send_keys("admin123")
driver.find_element(By.ID, "btnLogin").click()

# HOVERING 
# first find the elements you want to hover over using the mouse
admin = driver.find_element(By.XPATH, "//*[@id='menu_admin_viewAdminModule']")
usr_mgmt = driver.find_element(By.ID, "menu_admin_UserManagement")
usrs = driver.find_element(By.ID, "menu_admin_viewSystemUsers")
# to hover(mouser related actions) we create an object of actionchains class
actions = ActionChains(driver)
actions.move_to_element(admin).move_to_element(usr_mgmt).move_to_element(usrs).click().perform()  # to complete the action of click we have to use the perform method

time.sleep(10)
driver.quit()

# DOUBLE CLICK
driver1 = webdriver.Chrome(executable_path="chromedriver.exe")
driver1.get("https://testautomationpractice.blogspot.com")
driver.maximize_window()
time.sleep(8)
# find the element to be double clicked
element = driver1.find_element(By.XPATH, "//*[@id='HTML10']/div[1]/button")
action2 = ActionChains(driver1)
action2.double_click(element).perform()  # double click the element

# RIGHT CLICK