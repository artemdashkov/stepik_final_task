import time

from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_in_basket(self):
        product_page_link = self.browser.find_element(*ProductPageLocators.ADD_IN_BASKET_LINK)
        product_page_link.click()
        self.solve_quiz_and_get_code()

    def checking_name_product_after_ordering(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        name_product_in_basket = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_ADDED_IN_BASKET).text
        #list_of_words = text_product_in_basket.split(' ')
        #name_product_in_basket = ' '.join(list_of_words[0:3])
        assert name_product == name_product_in_basket,\
            "Name product in basket don't corresponds real name product"
        print("Name product in basket corresponds real name product")

    def checking_price_product_after_ordering(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        price_product_added_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_ADDED_IN_BASKET).text
        assert price_product == price_product_added_in_basket,\
            "Price product in basket don't corresponds real price product"
        print("Price product in basket corresponds real name product")