from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


@then('Verify Sign In page opens')
def verify_sign_in_is_opened(context):
    context.app.sign_in_page.verify_sign_in_opens()