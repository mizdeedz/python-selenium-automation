from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# init driver
driver = webdriver.Chrome(r'C:\Users\jessi\repo\qa_auto\python-selenium-automation\chromedriver_win32\chromedriver.exe')
driver.maximize_window()
driver.wait = WebDriverWait(driver, 10)
# driver.implicity_wait(10)

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

# wait for 4 sec
# sleep(4)
driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnk')), message='Error, Search button is not clickable')

# click search
driver.find_element(By.NAME, 'btnK').click()

# verify
assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
