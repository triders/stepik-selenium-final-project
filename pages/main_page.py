from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage (BasePage):

    def should_be_login_link(self):
        assert self.is_element_present_on_page(By.CSS_SELECTOR, "#login_link"), \
            "Unable to locate the login link"

    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
