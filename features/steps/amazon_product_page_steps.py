from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


PRODUCT_NAME = (By.ID, 'productTitle')
ADD_TO_CART = (By. ID, 'add-to-cart-button')


@when('Store product name')
def store_product_name(context):
    context.current_product = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Product Name is {context.current_product}')


@when('Click add to cart')
def add_product_to_cart(context):
    context.driver.find_element(*ADD_TO_CART).click()
    sleep(2)