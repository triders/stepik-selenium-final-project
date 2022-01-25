from selenium.webdriver.common.by import By


class BasePageLocators():

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a.btn.btn-default")
    LOGOUT_LINK = (By.CSS_SELECTOR, "a#logout_link")


class MainPageLocators(BasePageLocators):
    def __init__(self, *args, **kwargs):
        super(BasePageLocators, self).__init__(*args, **kwargs)


class LoginPageLocators():

    LOGIN_USERNAME = (By.CSS_SELECTOR, "input#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input#id_login-password")
    REGISTER_USERNAME = (By.CSS_SELECTOR, "input#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators():

    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main > p.price_color")

    ADD_TO_basket_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ALERT_SUCCESS_MESSAGE_PRODUCT_ADDED_TO_basket = (By.CSS_SELECTOR, "#messages > .alert-success strong")
    ALERT_INFO_MESSAGE_basket_VALUE_AMOUNT = (By.CSS_SELECTOR, "#messages > .alert-info p strong")


class BasketPageLocators():

    BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, "div#content_inner > p")
    FIRST_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "div.basket-items h3 a")
