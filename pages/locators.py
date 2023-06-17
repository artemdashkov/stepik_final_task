from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators:
    REGISTER_LINK = (By.CSS_SELECTOR, '#register_form')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')

class ProductPageLocators:
    ADD_IN_BASKET_LINK = (By.CSS_SELECTOR, '#add_to_basket_form > button')

    NAME_PRODUCT = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    NAME_PRODUCT_ADDED_IN_BASKET = (By.CSS_SELECTOR, '#messages > .alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1) > .alertinner > strong')

    PRICE_PRODUCT = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')
    PRICE_PRODUCT_ADDED_IN_BASKET = (By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner strong')

