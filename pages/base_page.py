import math
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators


class BasePage():

    def __init__(self, browser, url, timeout=10):
        self.browser: webdriver.Chrome = browser
        self.url = url
        # self.browser.implicitly_wait(timeout)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def open(self):
        self.browser.get(self.url)

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

    def is_element_disappeared(self, element_locating_method, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((element_locating_method, locator)))
        except TimeoutException:
            return False
        return True

    def should_be_login_link(self):
        assert self.is_element_present_on_page(*BasePageLocators.LOGIN_LINK), \
            "Unable to locate the login link"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")



