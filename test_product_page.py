from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_product_name_in_added_to_cart_success_message()
    page.should_be_cart_value_equal_to_product_price()
