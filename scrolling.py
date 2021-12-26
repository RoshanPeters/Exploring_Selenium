'''
there are three different ways in selenium to scroll down a page:
1)scroll down the page by pixel 
2)scroll down the page till element found
3)scroll to end of the page
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()
time.sleep(6)

# SCROLL DOWN THE PAGE BY PIXEL
driver.execute_script("window.scrollBy(0,1000)","")  # scrolling from 0px to 1000px
time.sleep(5)

# SCROLL TILL ELEMENT IS FOUND
flag = driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div[2]/table[2]/tbody/tr[96]/td[1]/img")
driver.execute_script("arguments[0].scrollIntoView();", flag)  # the page will scroll till the element stored in the variable flag is found
time.sleep(6)

# SCROLL TILL END OF PAGE
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)

driver.close()
