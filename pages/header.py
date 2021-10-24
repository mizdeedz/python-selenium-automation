from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    DEPARTMENT_SELECT = (By.ID, 'searchDropdownBox')
    SIGN_IN_POPUP_BTTN = (By.CSS_SELECTOR, "#nav-signin-tooltip a[data-nav-role='signin']")
    CART_ICON = (By.CSS_SELECTOR, "a[href*='/gp/cart/view']")
    FLAG = (By.CSS_SELECTOR, ".icp-nav-flag.icp-nav-flag-us")
    SPANISH_LANG_LINK = (By.CSS_SELECTOR, "a[href='#switch-lang=es_US']")
    ENGLISH_LANG_TEXT = (By.XPATH, "//header[@id='navbar-main']//*[contains(text(), 'English - EN')]")


    def input_search(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_sign_in_popup(self):
        self.wait_for_element_click(*self.SIGN_IN_POPUP_BTTN)

    def click_cart_icon(self):
        self.click(*self.CART_ICON)

    def hover_over_language_options(self):
        lang = self.find_element(*self.FLAG)
        actions = ActionChains(self.driver)
        actions.move_to_element(lang)
        actions.perform()

    def verify_lang_options_present(self):
        self.wait_for_element_appear(*self.SPANISH_LANG_LINK)
        self.find_element(*self.ENGLISH_LANG_TEXT)

    def select_department_by_alias(self, alias):
        select = Select(self.find_element(*self.DEPARTMENT_SELECT))
        select.select_by_value(f'search-alias={alias}')





# alternatively, check the order of options in dropdown:
# DEPARTMENT_OPTIONS = (By.CSS Selector, '#searchDropdownBox option')  # store at the top
# options = [o.text for o in self.find_elements(*self.DEPARTMENT_OPTIONS)]
# print(options)
# assertion line would go here, something like this (fails because of spacing):
# assert options == sorted(options), f'Error, expected {sorted(options)} but got {options}'