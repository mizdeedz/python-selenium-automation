from selenium.webdriver.common.by import By
from pages.base_page import Page

class Cart(Page):
    cart_count = (By.ID, "nav-cart-count")
    cart_text = (By.CSS_SELECTOR, 'div#sc-empty-cart-message h2')

    def cart_item_count(self, expected_count):
        cart_items = self.find_element(*self.cart_count).text
        assert cart_items == expected_count, f'Expected {expected_count} items, but got {cart_items}'

    def cart_empty_message(self, expected_text):
        cart_message = self.find_element(*self.cart_text).text
        assert cart_message == expected_text, f'Expected {expected_text}, but got {cart_message}'