from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
time.sleep(10)

src_ele = driver.find_element(By.XPATH, "//*[@id='box3']")
dest_ele = driver.find_element(By.XPATH, "//*[@id='box103']")

# performing drag and drop
action = ActionChains(driver)
action.drag_and_drop(src_ele, dest_ele).perform()