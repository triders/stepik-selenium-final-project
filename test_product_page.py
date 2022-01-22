import pytest
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators

base_url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
url_list = [base_url + "?promo=offer" + str(n) for n in range(0, 10)]  # promo=offer7 has bug, will mark it as xfail
url_list_7th_is_xfail = [pytest.param(url, marks=pytest.mark.xfail) if url[-1] == "7" else url for url in url_list]


@pytest.mark.skip
@pytest.mark.parametrize('url', url_list_7th_is_xfail)
def test_guest_can_add_product_to_basket(browser, url):
    page = ProductPage(browser, url)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_product_name_in_added_to_cart_success_message()
    page.should_be_cart_value_equal_to_product_price()


@pytest.mark.skip
def test_no_success_message_before_product_added_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    # page.add_to_cart()  # to make test red
    page.should_not_be_success_message_before_product_added_to_cart()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    url = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message_before_product_added_to_cart()


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    url = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    page.should_not_be_success_message_before_product_added_to_cart()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    url = "https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_cart()
    page.should_success_message_disappear_after_a_while()


def test_guest_should_see_login_link_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, url)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, url)
    page.open()
    page.go_to_login_page()
