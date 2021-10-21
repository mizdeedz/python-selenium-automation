from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):


    def verify_sign_in_opens(self):
        self.verify_url_contains_query('ap/signin')