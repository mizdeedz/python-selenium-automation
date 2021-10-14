from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


PRODUCT_NAME = (By.ID, 'productTitle')
ADD_TO_CART = (By. ID, 'add-to-cart-button')
COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
CURRENT_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')


@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}')


@when('Store product name')
def store_product_name(context):
    context.current_product = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Product Name is {context.current_product}')


@when('Click add to cart')
def add_product_to_cart(context):
    context.driver.find_element(*ADD_TO_CART).click()
    sleep(2)


@then('Verify user can click through colors')
def verify_can_click_through_colors(context):
    expected_colors = ['Dark Navy', 'Dusty Rose', 'Black']

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for i in range(len(colors)):
        colors[i].click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        assert current_color == expected_colors[i], f'Error expected {expected_colors[i]} did not match {current_color}'


    # alternate way of solving - gather into list and compare list to list
    # actual_colors = []
    #
    # for color in colors:
    #     color.click()
    #     actual_colors += [context.driver.find_element(*CURRENT_COLOR).text]
    #
    # assert expected_colors == actual_colors, f'Error expected {expected_colors} did not match {actual_colors}'