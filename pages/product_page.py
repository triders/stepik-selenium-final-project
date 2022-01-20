from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def get_product_name(self):
        product_name_element = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_text = product_name_element.text
        return product_name_text

    def get_product_price(self):
        product_price_element = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_element_text = product_price_element.text
        return product_price_element_text

    def get_added_to_cart_success_message(self):
        added_to_cart_message = self.browser.find_element(*ProductPageLocators.ALERT_SUCCESS_MESSAGE_PRODUCT_ADDED_TO_CART)
        added_to_cart_message_text = added_to_cart_message.text
        return added_to_cart_message_text

    def get_cart_value_amount_from_info_message(self):
        cart_value_amount_element = self.browser.find_element(*ProductPageLocators.ALERT_INFO_MESSAGE_CART_VALUE_AMOUNT)
        cart_value_amount_element_text = cart_value_amount_element.text
        return cart_value_amount_element_text

    def should_be_cart_value_equal_to_product_price(self):
        # check that the cart value amount = product price
        product_price = self.get_product_price()
        cart_value_amount = self.get_cart_value_amount_from_info_message()
        assert product_price == cart_value_amount, f"Expected cart value amount ({cart_value_amount}) " \
                                                   f"to be equal to product price ({product_price})"

    def should_be_product_name_in_added_to_cart_success_message(self):
        # check that this exact product has been added to cart (check info message)
        product_name = self.get_product_name()
        success_message = self.get_added_to_cart_success_message()
        assert product_name in success_message, f"Expected {product_name} to be part of {success_message}"
