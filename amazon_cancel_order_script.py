from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome(r'C:\Users\jessi\repo\qa_auto\python-selenium-automation\chromedriver_win32\chromedriver.exe')
driver.maximize_window()

# open the webpage
driver.get('https://www.amazon.com/gp/help/customer/display.html')

# search help library
driver.find_element(By.ID, 'helpsearch').send_keys('Cancel order', Keys.ENTER)

# verify search result
actual_result = driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
expected_result = "Cancel Items or Orders"

assert actual_result == expected_result, f'Actual {actual_result} does not match expected {expected_result}'

# close browser window
driver.quit()