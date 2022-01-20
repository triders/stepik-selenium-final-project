from selenium.webdriver.common.by import By


class MainPageLocators():

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():

    LOGIN_USERNAME = (By.CSS_SELECTOR, "input#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input#id_login-password")
    REGISTER_USERNAME = (By.CSS_SELECTOR, "input#id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "input#id_registration-password2")


class ProductPageLocators():

    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main > p.price_color")

    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ALERT_SUCCESS_MESSAGE_PRODUCT_ADDED_TO_CART = (By.CSS_SELECTOR, "#messages > .alert-success")  # and hope that
    # "added to cart" will be the first by this selector
    ALERT_INFO_MESSAGE_CART_VALUE_AMOUNT = (By.CSS_SELECTOR, "#messages > .alert-info p strong")
