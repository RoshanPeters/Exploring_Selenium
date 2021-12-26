'''
Working with browser windows:
when you a open a parent window and then when you click on an element that opens another window, Selenium still gives preference to the parent window. 

Handle is kind of an id, and every window will have a unique handle.

To switch between windows in order to perform actions on it: 
1)driver.current_window_handle (will get you the handle value of the current browser)
2)driver.window_handles (returns handle value of all the open browsers)
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")
driver.find_element(By.XPATH, "//*[@id='Tabbed']/a/button").click() # 2 tabs/windows will be opened once this action is performed

# to get the handle value of the current window/browser
print('current handle: ', driver.current_window_handle)

# to get the handle values of all the open tabs/windows
handles = driver.window_handles
for handle in handles:
 driver.switch_to.window(handle)  
 print('The title of the page is: ', driver.title)
 # To close a specific open tab (After finding the handles and titles of all the pages, we switch to the particular page we want to close using its handle and title)
 if driver.title == "Selenium":
  driver.close()

driver.quit()
