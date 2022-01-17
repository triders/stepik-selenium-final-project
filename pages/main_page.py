from .base_page import BasePage
from pages.locators import MainPageLocators


class MainPage (BasePage):

    def should_be_login_link(self):
        assert self.is_element_present_on_page(*MainPageLocators.LOGIN_LINK), \
            "Unable to locate the login link"

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
