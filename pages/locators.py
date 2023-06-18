from selenium.webdriver.common.by import By

class ProductPageLocators:
    ADD_IN_BASKET_LINK = (By.CSS_SELECTOR, '#add_to_basket_form > button')

    NAME_PRODUCT = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    NAME_PRODUCT_ADDED_IN_BASKET = (By.CSS_SELECTOR, '#messages > .alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1) > .alertinner > strong')

    PRICE_PRODUCT = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')
    PRICE_PRODUCT_ADDED_IN_BASKET = (By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner strong')

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages > .alert.alert-safe.alert-noicon.alert-success.fade.in:nth-child(1) > .alertinner')

class BasePageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group > .btn.btn-default:nth-child(1)')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    REGISTER_LINK = (By.CSS_SELECTOR, '#register_form')

class BasketPageLocators:
    PRODUCT_ITEM = (By.CSS_SELECTOR, '.basket-items')
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner')



