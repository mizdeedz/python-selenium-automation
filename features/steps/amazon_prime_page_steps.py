from selenium.webdriver.common.by import By
from behave import given, when, then


BENEFIT_BOXES = (By.CSS_SELECTOR, "div.benefit-box")


@given('Open Amazon Prime')
def open_amazon_prime(context):
    context.driver.get('https://www.amazon.com/amazonprime')


@then('Verify {expected_amount} benefit boxes are present')
def verify_benefit_boxes_count(context, expected_amount):
    boxes = context.driver.find_elements(*BENEFIT_BOXES)
    assert len(boxes) == int(expected_amount), f'Expected {expected_amount} links, but got {len(boxes)}'