import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage


def test_guest_can_see_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_main_page_ru(browser):
    url = "https://selenium1py.pythonanywhere.com/ru/"
    page = MainPage(browser, url)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, url)
    basket_page.should_not_be_products_in_basket()
    basket_page.should_be_message_that_basket_is_empty_ru()


@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-girl-who-played-with-non-fire_203/"
    page = ProductPage(browser, url)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, url)
    basket_page.should_not_be_products_in_basket()
    basket_page.should_be_message_that_basket_is_empty_ru()
