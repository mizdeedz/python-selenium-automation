from selenium.webdriver.common.by import By
from behave import given, when, then


HAM_MENU_ICON = (By.ID, "nav-hamburger-menu")
FOOTER_LINKS = (By.CSS_SELECTOR, ".navFooterMoreOnAmazon a.nav_a")

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@when('Input {search_word} into amazon search')
def search_amazon(context, search_word):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(search_word)


@when('Click on amazon search icon')
def click_search(context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@then('Verify hamburger menu icon is present')
def verify_ham_menu(context):
    context.driver.find_element(*HAM_MENU_ICON)


@then('Verify {expected_amount} footer links are present')
def verify_footer_links_count(context, expected_amount):
    links = context.driver.find_elements(*FOOTER_LINKS)
    assert len(links) == int(expected_amount), f'Expected {expected_amount} links, but got {len(links)}'


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
