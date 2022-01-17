from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser: webdriver.Chrome = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present_on_page(self, element_locating_method, locator):
        try:
            self.browser.find_element(element_locating_method, locator)
        except NoSuchElementException:
            return False
        return True



