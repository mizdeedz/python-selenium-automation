from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_notice_opened(context):
    assert 'https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ' in \
           context.driver.current_url, f'Error, Privacy Notice not opened'


@then('User can close new window and switch back to original')
def close_new_page_switch_to_original(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)

