from .base_page import BasePage
from .locators import BasketPageLocators

from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math, time
from .locators import BasePageLocators

class BasketPage(BasePage):
    def product_in_basket_is_present(self):
        assert not self.is_element_present(*BasketPageLocators.PRODUCT_ITEM), \
            "Products in basket is presented"

    def product_in_basket_is_not_present(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_ITEM), \
            "Products in basket is presented, but should not be"

    def is_message_empty_basket(self):
        message_text = self.browser.find_element(*BasketPageLocators.MESSAGE_EMPTY_BASKET).text
        assert 'Your basket is empty' in message_text, 'Корзина не пуста'