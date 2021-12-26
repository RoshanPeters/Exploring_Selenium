'''
Wait commands:
synchronization-> each line gets executed from top to bottom

sometimes a particular line of code is required for an element(eg. submit button) and by that time if the element is not there in the page, it will jump to the next line of the code. This will throw an exception: element is not visible.

Exception might occur also when there is another page that is not open but the code for that is running, hence giving an error.

To fix this problem: one way is to improve the application speed or 'wait' till the element appears/loaded.

There are two types of waits in webdriver: Implicit wait or Explicit wait.

implicit wait is applicable for all the elements of the page. Only one time we have to specify this in the beginning of the code. There is still a chance to get exception if the elemented is not loaded by the time set.
'''

from selenium import webdriver

driver = webdriver.Chrome(executable_path="chromedriver.exe")

driver.get("http://newtours.demoaut.com/")  # opening url takes some time

# wait some time here to make sure that everything is opened.
# in order to wait here we have to use the implicit wait command.
driver.implicitly_wait(10)  # after opening the url it will wait here for 10 seconds

# to verify the title of the page
assert "Welcome: Mercury Tours" in driver.title

# filling in the username and password
driver.find_element_by_name("").send_keys("")
driver.find_element_by_name("").send_keys("")
driver.find_element_by_name("").click()


