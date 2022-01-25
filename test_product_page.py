import pytest
from faker import Faker

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        url = "http://selenium1py.pythonanywhere.com/accounts/login/"
        fake = Faker()  # generate data to create an unique user
        self.name = fake.name()  # e.g. 'Jade Taylor'
        self.email = fake.email()  # e.g. 'kreid@example.net'
        self.password = fake.password()  # e.g. '$M4^Xo4xtC'
        login_page = LoginPage(browser, url)
        login_page.open()
        login_page.register_new_user(self.email, self.password)
        login_page.is_user_authorized()

    def test_user_cant_see_success_message(self, browser):
        url = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, url)
        page.open()
        page.should_not_be_success_message_before_product_added_to_basket()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        url = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, url)
        page.open()
        page.add_to_basket()
        page.should_be_product_name_in_added_to_basket_success_message()
        page.should_be_basket_value_equal_to_product_price()
        # and check that basket contains an item
        page.go_to_basket()
        basket_page = BasketPage(browser, url)
        basket_page.should_be_products_in_basket()


def test_guest_cant_see_success_message(browser):
    url = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    page.should_not_be_success_message_before_product_added_to_basket()


base_url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
url_list = [base_url + "?promo=offer" + str(n) for n in range(0, 10)]  # promo=offer7 has bug, will mark it as xfail
url_list_7th_is_xfail = [pytest.param(url, marks=pytest.mark.xfail) if url[-1] == "7" else url for url in url_list]


@pytest.mark.parametrize('url', url_list_7th_is_xfail)
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, url):
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_product_name_in_added_to_basket_success_message()
    page.should_be_basket_value_equal_to_product_price()


def test_no_success_message_before_product_added_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    page.should_not_be_success_message_before_product_added_to_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    url = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message_before_product_added_to_basket()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    url = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket()
    page.should_success_message_disappear_after_a_while()


def test_guest_should_see_login_link_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, url)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, url)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/the-girl-who-played-with-non-fire_203/"
    page = ProductPage(browser, url)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, url)
    basket_page.should_not_be_products_in_basket()
    basket_page.should_be_message_that_basket_is_empty()
