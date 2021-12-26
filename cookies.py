'''
Cookies are a piece of information from website and saved by your web browser.
Cookies are a way of remembering users and their interaction witht the site by storing information in the cookie file as key value pairs. It stores the login information like user name/ email and password.
HTTP cookie is also known as web cookie, a browser cookie or internet cookie.

Different operations on cookie:
 Capture all cookies from browser
 Count number of cookies
 Read Cookie pairs
 Adding new cookies
 Deleting specific cookie by using name of cookie
 Deleting all the cookies
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.amazon.in/")

# capturing all the cookies created by browser
cookies = driver.get_cookies()
print(cookies)  # information is stored as dictionary
# number of cookies created
print(len(cookies))

# adding new cookie to the browser
cookie = {'name': 'Mycookie', 'value': '1234567890'}
driver.add_cookie(cookie)

cookies = driver.get_cookies()
print(cookies)
print(len(cookies))  # printing number of cookies after adding a cookie

# deleting cookie
driver.delete_cookie("Mycookie")
time.sleep(5)

cookies = driver.get_cookies()
print(cookies)
print(len(cookies))  # printing number of cookies after deleting the cookie

driver.delete_all_cookies()  # deletes all cookies
cookies = driver.get_cookies()  # capture all the cookies after deleting all cookies
print(len(cookies))  # 0 cookies