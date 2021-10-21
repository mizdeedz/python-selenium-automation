from pages.main_page import MainPage
from pages.header import Header
from pages.search_results_page import SearchResults
from pages.amazon_prime_page import AmazonPrimePage
from pages.sign_in_page import SignInPage
from pages.cart_page import Cart

class Application():

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.search_results_page = SearchResults(self.driver)
        self.amazon_prime_page = AmazonPrimePage(self.driver)
        self.sign_in_page = SignInPage(self.driver)
        self.cart_page = Cart(self.driver)