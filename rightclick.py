from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
element = driver.find_element(By.XPATH, "/html/body/div/section/div/div/div/p/span")

# performing the right click action
action = ActionChains(driver)
action.context_click(element).perform()
