from selenium.webdriver.common.by import By
from behave import given, when, then


FIRST_RESULT = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")


@when('Click on first product')
def click_first_product(context):
    context.driver.find_element(*FIRST_RESULT).click()


@then('Verify {expected_result} text is shown')
def verify_text_shown(context, expected_result):
    context.app.search_results_page.verify_search_result_text(expected_result)