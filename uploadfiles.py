from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://testautomationpractice.blogspot.com")
driver.maximize_window()
time.sleep(10)

# if the id of the frame is not found, we have to do it in 2 steps or we have use the index of the frame
frame = driver.find_element(By.XPATH, '//*[@id="frame-one1434677811"]')
driver.switch_to.frame(frame)  
src_ele = driver.find_element(By.ID, "RESULT_FileUpload-10").send_keys(r"C:\Users\ADMIN\Desktop\seleniumfile.txt")
