from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .locators import BasePageLocators


class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser: webdriver.Chrome = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def go_to_basket(self):
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def find_field_and_send_keys(self, element_locating_method, locator, keys):
        field = self.browser.find_element(element_locating_method, locator)
        field.send_keys(keys)

    def click_button(self, element_locating_method, locator):
        button = self.browser.find_element(element_locating_method, locator)
        button.click()

    def open(self):
        self.browser.get(self.url)

    def is_element_disappeared(self, element_locating_method, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((element_locating_method, locator)))
        except TimeoutException:
            return False
        return True

    def is_element_present_on_page(self, element_locating_method, locator):
        try:
            self.browser.find_element(element_locating_method, locator)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present_on_page(self, element_locating_method, locator, timeout=4):
        # explicitly waits, returns True is found before timeout
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((element_locating_method, locator)))
        except TimeoutException:
            return True
        return False

    def is_user_authorized(self):
        assert self.is_element_present_on_page(*BasePageLocators.LOGOUT_LINK), \
            "No user is authorized in this session (unable to find the 'Logout' button)"

    def should_be_login_link(self):
        assert self.is_element_present_on_page(*BasePageLocators.LOGIN_LINK), \
            "Unable to locate the login link"
