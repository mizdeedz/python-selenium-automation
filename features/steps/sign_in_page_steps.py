from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


@then('Verify Sign In page opens')
def verify_sign_in_is_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'), message='Sign In page did not open')