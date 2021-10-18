from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


privacy_link = (By.CSS_SELECTOR, 'a[href="https://www.amazon.com/privacy"]')


@given('Open Amazon T&C page')
def open_amazon_t_and_c(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/'
                       'ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Click on Amazon Privacy Notice link')
def click_privacy_notice_link(context):
    context.driver.find_element(*privacy_link).click()
    context.driver.wait.until(EC.new_window_is_opened)