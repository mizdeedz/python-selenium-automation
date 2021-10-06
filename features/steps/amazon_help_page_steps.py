from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


help_search = (By.ID, 'helpsearch')
search_result = (By.XPATH, "//div[@class='help-content']/h1")


@given('Open Amazon help page')
def open_amazon_help(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@when('Input {search_word} into help library and search')
def search_help(context, search_word):
    context.driver.find_element(*help_search).send_keys(search_word, Keys.ENTER)


@then('Verify {expected_result} result is shown')
def verify_result(context, expected_result):
    actual_result = context.driver.find_element(*search_result).text
    assert actual_result == expected_result, f'Error! Actual {actual_result} does not match expected {expected_result}'
