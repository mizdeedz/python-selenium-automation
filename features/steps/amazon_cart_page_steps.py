from selenium.webdriver.common.by import By
from behave import given, when, then


cart_name = (By.CSS_SELECTOR, '#sc-active-cart li')


@when('Click on the cart icon')
def click_cart(context):
    context.app.header.click_cart_icon()


@then('Verify cart has {expected_result} items')
def cart_item_count(context, expected_result):
    context.app.cart_page.cart_item_count(expected_result)


@then('Verify {expected_text} text present')
def cart_empty_text(context, expected_text):
    context.app.cart_page.cart_empty_message(expected_text)


@then('Verify correct product is in cart')
def cart_product_name(context):
    actual_result = context.driver.find_element(*cart_name).text
    print(f'Cart Product Name is {actual_result}')
    assert actual_result == context.current_product, f'Error! Actual {actual_result} '\
                                                     f'does not match Expected {context.current_product}'