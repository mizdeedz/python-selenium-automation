from selenium.webdriver.common.by import By
from behave import given, when, then


BEST_LINKS = (By.CSS_SELECTOR, '#zg_header a')
HEADER = (By.ID, 'zg_banner_text')


@given('Open Amazon Best Sellers page')
def open_amazon_bestsellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
    context.driver.refresh()


@then('Verify {expected_amount} best sellers links are present')
def verify_best_links_present(context, expected_amount):
    links = context.driver.find_elements(*BEST_LINKS)
    assert len(links) == int(expected_amount), f'Error! Actual count {len(links)} but expected {expected_amount}'


@then('User can click through top links and verify correct page opens')
def click_thru_top(context):
    top_links = context.driver.find_elements(*BEST_LINKS)

    for x in range(len(top_links)):
        link = context.driver.find_elements(*BEST_LINKS)[x]

        link_text = link.text
        link.click()

        header_text = context.driver.find_element(*HEADER).text
        assert link_text in header_text, f'Expected {link_text} not in {header_text}'