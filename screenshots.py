'''
WebDriver offers API's to take screenshot of a webpage
 save_screenshot('filename')
 get_screenshot_as_file('filename')
'''
from selenium import webdriver

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://demo.guru99.com/test/newtours/")

# driver.save_screenshot(r'C:\Users\ADMIN\Desktop\first_capture.png')  # it will accept any type of extension

driver.get_screenshot_as_file(r'C:\Users\ADMIN\Desktop\first_capture_file.png')  # it will accept only .png extension

