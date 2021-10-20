from selenium.webdriver.common.by import By
from pages.base_page import Page

class AmazonPrimePage(Page):
    DELIVERY_BOXES = (By.CSS_SELECTOR, "div.benefit-box")

    def open_amazon_prime(self):
        self.open_page('amazonprime')

    def verify_delivery_benefit_boxes_count(self, expected_amount):
        boxes = self.find_elements(*self.DELIVERY_BOXES)
        assert len(boxes) == int(expected_amount), f'Expected {expected_amount} boxes, but got {len(boxes)}'