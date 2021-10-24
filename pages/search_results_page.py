from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResults(Page):
    SEARCH_RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    DEPARTMENT_LOCATOR = (By.CSS_SELECTOR, "#nav-subnav[data-cateogry='{CATEGORY}']")

    def _get_expected_category_locator(self, expected_category):
        return [self.DEPARTMENT_LOCATOR[0], self.DEPARTMENT_LOCATOR[1].replace('{CATEGORY}', expected_category)]

    def verify_search_result_text(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT_TEXT)

    def verify_correct_department_selected(self, expected_department: str):
        locator = self._get_expected_category_locator(expected_department)
        self.find_element(*locator)