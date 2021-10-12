from selenium.webdriver.common.by import By
from behave import given, when, then


FIRST_RESULT = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")


@when('Click on first product')
def click_first_product(context):
    context.driver.find_element(*FIRST_RESULT).click()


@then('Verify {expected_result} text is shown')
def verify_text_shown(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert actual_result == expected_result, f'Error! Actual {actual_result} does not match expected {expected_result}'