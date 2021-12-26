from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver1 = webdriver.Chrome(executable_path= "chromedriver.exe")
# driver2 = webdriver.Ie(executable_path="IEDriverServer.exe")

# with this driver object we can access all the methods.

# this method will open url on a browser
driver1.get("https://www.youtube.com/")
print('this is the title of the browser you have opened: ')
print(driver1.title)  # to get the title of the page
print(driver1.current_url)  # return the url of the page
print(driver1.page_source)  # returns the html code forthe page
driver1.close()  # to close the browser

