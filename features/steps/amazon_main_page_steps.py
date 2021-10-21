from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


HAM_MENU_ICON = (By.ID, "nav-hamburger-menu")
FOOTER_LINKS = (By.CSS_SELECTOR, ".navFooterMoreOnAmazon a.nav_a")
SIGN_IN_POPUP_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip a[data-nav-role='signin']")


@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main_page()


@when('Input {search_word} into amazon search')
def search_amazon(context, search_word):
    context.app.header.input_search(search_word)


@when('Click on amazon search icon')
def click_search(context):
    context.app.header.click_search()


@when('Click Sign In from popup')
def click_sign_in_popup(context):
    context.app.header.click_sign_in_popup()


@when('Sign In pop up appears')
def sign_in_popup_appears(context):
    context.driver.wait.until(EC.element_to_be_clickable((SIGN_IN_POPUP_BTN)), message='Sign in btn not clickable')


@when('Wait for {sec} sec')
def wait_sec(context, sec):
    sleep(int(sec))


@then('Verify hamburger menu icon is present')
def verify_ham_menu(context):
    context.driver.find_element(*HAM_MENU_ICON)


@then('Verify {expected_amount} footer links are present')
def verify_footer_links_count(context, expected_amount):
    links = context.driver.find_elements(*FOOTER_LINKS)
    assert len(links) == int(expected_amount), f'Expected {expected_amount} links, but got {len(links)}'


@then('Verify Sign In pop up disappeared')
def verify_sign_in_disappeared(context):
    context.driver.wait.until(EC.invisibility_of_element_located((SIGN_IN_POPUP_BTN)), message='Sign in btn is visible')

    context.driver.wait.until(EC.url_to_be('https://www.amazon.com'))


# convert str expected_variable to int for assertion

# @then('Verify {expected_amount} footer links are present')
# def verify_footer_links_count(context, expected_amount):
#     print(type(expected_amount)) # expected_amount is a string '40'
#     links = context.driver.find_elements(*FOOTER_LINKS)
#     print(links)
#     print(type(len(links))) # when we count something, it is an int
#     assert len(links) == int(expected_amount), f'Expected {expected_amount} links, but got {len(links)}'
#     # if this is written without converting the str expected_amount to an int,
#     #    the assertion will fail


# find_elements hamburger example

# @then('Verify hamburger menu icon is present')
# def verify_ham_menu(context):
#     expected_count = 1
#     actual_count = len(context.driver.find_elements(*HAM_MENU_ICON))
#     assert expected_count == actual_count, f'Actual elements count {actual_count}, but expected {expected_count}'


# see how selenium returns find_element and find_elements

# @then('Verify hamburger menu icon is present')
# def verify_ham_menu(context):
#     print('\nFIND ELEMENT:\n')
#     element = context.driver.find_element(*HAM_MENU_ICON)
#     print(element)
#     print(type(element))
#
#     print('\nFIND ELEMENTSSSSS:\n')
#     elements = context.driver.find_elements(*HAM_MENU_ICON)
#     print(elements)
#     print(type(elements))


# alternate way of running this function

# @when('Click Sign In from popup')
# def click_sign_in_popup(context):
#     e = context.driver.wait.until(EC.element_to_be_clickable((SIGN_IN_POPUP_BTN)), message='Signin btn not clickable')
#     e.click()