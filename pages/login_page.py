from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage (BasePage):

    def register_new_user(self, email, password):
        print(f"\nRegistering a new user with email: '{email}' and password: '{password}'")
        self.find_field_and_send_keys(*LoginPageLocators.REGISTER_USERNAME, email)
        self.find_field_and_send_keys(*LoginPageLocators.REGISTER_PASSWORD, password)
        self.find_field_and_send_keys(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD, password)
        self.click_button(*LoginPageLocators.REGISTER_BUTTON)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        print(current_url)
        assert "login" in current_url, f"There is no 'login' word in the current URL: {current_url}"

    def should_be_login_form(self):
        assert self.is_element_present_on_page(*LoginPageLocators.LOGIN_USERNAME), \
            "Unable to locate LOGIN_USERNAME field"
        assert self.is_element_present_on_page(*LoginPageLocators.LOGIN_PASSWORD), \
            "Unable to locate LOGIN_PASSWORD field"

    def should_be_register_form(self):
        assert self.is_element_present_on_page(*LoginPageLocators.REGISTER_USERNAME), \
            "Unable to locate REGISTER_USERNAME field"
        assert self.is_element_present_on_page(*LoginPageLocators.REGISTER_PASSWORD), \
            "Unable to locate REGISTER_PASSWORD field"
        assert self.is_element_present_on_page(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD), \
            "Unable to locate REGISTER_CONFIRM_PASSWORD field"
