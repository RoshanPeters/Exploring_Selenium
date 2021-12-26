from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# # path expecting the download (default path is configured in chrome)
# ChromeOptions = Options()
# ChromeOptions.add_experimental_option("prefs", {"download.default_directory": "....."})
# we need to pass this object with the executable path
# driver = webdriver.Chrome(executable_path="chromedriver.exe",chrome_options=ChromeOptions)

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

# downloading file
driver.find_element(By.XPATH, "//*[@id='textbox']").send_keys("Entering Data for the file to be downloaded.")
driver.find_element(By.ID, "createTxt").click()
driver.find_element(By.ID, "link-to-download").click()


