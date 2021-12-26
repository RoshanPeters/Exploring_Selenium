from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Chrome webdriver
driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title)
print(driver.current_url)

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()  # clicking on the click button in the website

time.sleep(5)  # waits for 5 seconds before closing it

driver.close()  # this will close the first browser that opened (parent window)
# close command will only close one window at a time

driver.quit()  # closes all the browsers




