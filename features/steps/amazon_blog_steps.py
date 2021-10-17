from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@then('Verify blog is opened')
def verify_blog_opened(context):
    assert 'https://www.aboutamazon.com/' in context.driver.current_url, \
        f'Error, https://www.aboutamazon.com/ not opened'


@then('Close blog')
def close_blog_page(context):
    context.driver.close()


@then('Return to original window')
def switch_to_original_window(context):
    context.driver.switch_to.window(context.original_window)