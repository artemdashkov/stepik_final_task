from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators
from selenium import webdriver



class LoginPage(BasePage):
    def register_new_user(self, email, password):

        self.browser.find_element(*LoginPageLocators.NEW_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.NEW_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REPEAT_NEW_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()