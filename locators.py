from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# Lesson 2 locator examples:

# ID

driver.find_element(By.ID, 'nav-search-submit-button')

driver.find_element(By.ID, 'twotabsearchtextbox')

# XPATH

driver.find_element(By.XPATH, "//a[@href='/ref=nav_logo']")

driver.find_element(By.XPATH, "//span[@class='icp-nav-flag icp-nav-flag-us']")

# Search by multiple attributes using 'and'
driver.find_element(By.XPATH, "//a[@data-csa-c-type='link' and @href='/gp/bestsellers/?ref_=nav_cs_bestsellers_8a080d3d7b55497ea1bdd97b7cff8b7b']")

# Search by text using 'text()'
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @data-csa-c-type='link']")

# Search across direct child elements: /
driver.find_element(By.XPATH, "//div[@id='nav-xshop']/a[text()='Best Sellers']")

# Search across multiple child elements and their children: //
driver.find_element(By.XPATH, "//div[@id='nav-xshop-container']//a[text()='Best Sellers']")

# Contains, contains(attribute, 'partial value')
driver.find_element(By.XPATH, "//a[contains(@href, '/gp/bestsellers/?ref_=nav_cs_bestsellers')]")
driver.find_element(By.XPATH, "//div[@id='nav-xshop-container']//a[contains(text(), 'Best Selle')]")
