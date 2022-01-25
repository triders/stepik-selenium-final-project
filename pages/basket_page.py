from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_message_that_basket_is_empty(self):
        message = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE).text
        assert message == "Your basket is empty. Continue shopping", \
            f"Expected 'Your basket is empty. Continue shopping', got: '{message}'"

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present_on_page(*BasketPageLocators.FIRST_PRODUCT_IN_BASKET), \
            "Expected to see no products in basket, but seems like found some o_0"

    def should_be_products_in_basket(self):
        assert self.is_element_present_on_page(*BasketPageLocators.FIRST_PRODUCT_IN_BASKET), \
            "Expected to see some products in basket, but there is nothing in it o_0"
