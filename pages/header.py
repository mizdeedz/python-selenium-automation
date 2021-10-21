from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    SIGN_IN_POPUP_BTTN = (By.CSS_SELECTOR, "#nav-signin-tooltip a[data-nav-role='signin']")
    CART_ICON = (By.CSS_SELECTOR, "a[href*='/gp/cart/view']")

    def input_search(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_sign_in_popup(self):
        self.wait_for_element_click(*self.SIGN_IN_POPUP_BTTN)

    def click_cart_icon(self):
        self.click(*self.CART_ICON)