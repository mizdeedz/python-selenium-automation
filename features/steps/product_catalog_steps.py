from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify {expected_result} text is shown')
def verify_text_shown(context, expected_result):
    actual_result = context.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text
    assert actual_result == expected_result, f'Error! Actual {actual_result} does not match expected {expected_result}'