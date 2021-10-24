from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from pages.base_page import Page


class ProductDetailPage(Page):
    NEW_ARRIVALS = (By.CSS_SELECTOR, "#nav-subnav a[href*='ref=sr_hi_2'] span.nav-a-content")
    CATEGORY_WOMEN = (By.XPATH, "//div[@class='mm-column']//img[contains(@src, 'NA_Women.jpg')]")
    CATEGORY_WOMEN_TEXT = (By.XPATH, "//a[@class='mm-merch-panel']//h3[contains(text(), 'Women')]")

    def hover_over_new_arrivals_link(self):
        link = self.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(link)
        actions.perform()

    def verify_women_category_present(self):
        self.wait_for_element_appear(*self.CATEGORY_WOMEN)
        self.find_element(*self.CATEGORY_WOMEN_TEXT)


