'''
explicit wait:
looks for the elements available on the page. It is not time based and it is completely based on the condition.

selenium.common.exceptions.ElementNotInteractableException: Message: element not interactable

A possibility is that the element is currently unclickable because it is not visible. Reasons for this may be that another element is covering it up or it is not in view, i.e. it is outside the currently view-able area.

explicit wait works upon some conditions: for that you need to import a library.
from selenium.webdriver.support import expected_conditions 
we also need the object of WebDriverWait and this is imported
from selenium.webdriver.support.ui import WebDriverWait

wait = WebDriverWait(driver,10)
eventhough explicit wait is condition based we provide the time and it is the wait time (maximum time out).
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path="chromedriver.exe")

driver.implicitly_wait(5)

driver.get("http://advantageonlineshopping.com/#/")
time.sleep(6)

driver.maximize_window()
time.sleep(6)

driver.find_element(By.ID, "hrefUserIcon").click()
time.sleep(6)

# if anything is filled in the box by default we have to clear it first
driver.find_element(
    By.XPATH, "/html/body/login-modal/div/div/div[3]/sec-form/sec-view[1]/div/input").clear()

driver.find_element(
    By.XPATH, "/html/body/login-modal/div/div/div[3]/sec-form/sec-view[1]/div/input").send_keys('selenium_trial@gmail.com')
time.sleep(6)

driver.find_element(
    By.XPATH, "/html/body/login-modal/div/div/div[3]/sec-form/sec-view[2]/div/input").send_keys('seleniumpassword')
time.sleep(6)

driver.find_element(
    By.XPATH, "/html/body/login-modal/div/div/div[3]/sec-form/div/input").click()

time.sleep(4)

driver.find_element(By.XPATH, "//*[@id='sign_in_btnundefined']").click()

time.sleep(5)

# explicit wait
wait = WebDriverWait(driver, 10)

# placing the conditions (there are many other conditions possible, it is available in the selenium python documentation)
# here we wait till the button becomes found on the screen/page
# As soon as element(click button) is found the click action is performed
# we dont need to type in find_element, that is happening internally because of the condition function, all we have to do is add the locater(By.XPATH).
ele = wait.until(EC.element_to_be_clickable((By.XPATH, "")))
ele.click()

driver.close()
