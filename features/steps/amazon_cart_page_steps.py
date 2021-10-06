from selenium.webdriver.common.by import By
from behave import given, when, then


cart_icon = (By.CSS_SELECTOR, "a[href*='/gp/cart/view']")
cart_count = (By.ID, "nav-cart-count")


@when('Click on the cart icon')
def click_cart(context):
    context.driver.find_element(*cart_icon).click()


@then('Verify cart has {expected_result} items')
def cart_item_count(context, expected_result):
    actual_result = context.driver.find_element(*cart_count).text
    assert actual_result == expected_result, f'Error! Actual {actual_result} does not match Expected {expected_result}'