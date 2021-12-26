'''
If a webpage has multiple frames we can not do it the normal way. We have to switch between the frames to inspect the required element.
All the frames in the webpage will be present under the html element 'frameset'/'iframe'.
switch_to.frame(*)   *we can either pass name, id, index
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
time.sleep(10)

# to click on an element in a frame we have to switch to that frame to do so
driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT, "org.openqa.selenium.cli").click()
time.sleep(8)

# we can not directly jump to the next frame because the frames in the webpage are available in the page level
# we first need to go back to the page and then again switch to the frame of our choice
driver.switch_to.default_content()
time.sleep(5)

driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT, "CliCommand.Executable").click()
time.sleep(8)




