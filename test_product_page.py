import pytest
from pages.product_page import ProductPage


base_url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
url_list = [base_url + "?promo=offer" + str(n) for n in range(0, 10)]  # promo=offer7 has bug, will mark it as xfail
url_list_7th_is_xfail = [pytest.param(url, marks=pytest.mark.xfail) if url[-1] == "7" else url for url in url_list]


@pytest.mark.parametrize('url', url_list_7th_is_xfail)
def test_guest_can_add_product_to_basket(browser, url):
    print(url_list)
    page = ProductPage(browser, url)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_product_name_in_added_to_cart_success_message()
    page.should_be_cart_value_equal_to_product_price()
