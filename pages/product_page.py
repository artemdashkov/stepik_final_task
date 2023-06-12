import time

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_in_basket(self):
        product_page_link = self.browser.find_element(*ProductPageLocators.ADD_IN_BASKET_LINK)
        product_page_link.click()
        self.solve_quiz_and_get_code()
        #time.sleep(1000)

    def checking_name_product_after_ordering(self):
        assert self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text in self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_ADDED_IN_BASKET).text,\
            "Name product in basket don't corresponds real name product"
        print("Name product in basket corresponds real name product")

    def checking_price_product_after_ordering(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text in self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_ADDED_IN_BASKET).text,\
            "Price product in basket don't corresponds real price product"
        print("Price product in basket corresponds real name product")