from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_basket_BUTTON)
        add_to_basket_button.click()

    def get_product_name(self):
        product_name_element = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_text = product_name_element.text
        return product_name_text

    def get_product_price(self):
        product_price_element = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_element_text = product_price_element.text
        return product_price_element_text

    def get_added_to_basket_success_message(self):
        added_to_basket_message = self.browser.find_element(
            *ProductPageLocators.ALERT_SUCCESS_MESSAGE_PRODUCT_ADDED_TO_basket)
        added_to_basket_message_text = added_to_basket_message.text
        return added_to_basket_message_text

    def get_basket_value_amount_from_info_message(self):
        basket_value_amount_element = self.browser.find_element(*ProductPageLocators.ALERT_INFO_MESSAGE_basket_VALUE_AMOUNT)
        basket_value_amount_element_text = basket_value_amount_element.text
        return basket_value_amount_element_text

    def should_be_basket_value_equal_to_product_price(self):
        # check that the basket value amount = product price
        product_price = self.get_product_price()
        basket_value_amount = self.get_basket_value_amount_from_info_message()
        assert product_price == basket_value_amount, f"Expected basket value amount ({basket_value_amount}) " \
                                                   f"to be equal to product price ({product_price})"

    def should_be_product_name_in_added_to_basket_success_message(self):
        # check that this exact product has been added to basket (check info message)
        product_name = self.get_product_name()
        success_message = self.get_added_to_basket_success_message()
        assert product_name == success_message, f"Expected {product_name} to be part of {success_message}"

    def should_not_be_success_message_before_product_added_to_basket(self):
        assert self.is_not_element_present_on_page(*ProductPageLocators.ALERT_SUCCESS_MESSAGE_PRODUCT_ADDED_TO_basket), \
            "A success message is present on page, but it shouldn't (because product hasn't been added to basket yet)"

    def should_success_message_disappear_after_a_while(self):
        assert self.is_element_disappeared(*ProductPageLocators.ALERT_SUCCESS_MESSAGE_PRODUCT_ADDED_TO_basket), \
            "A success message didn't disappear after some time, but it should had to"
