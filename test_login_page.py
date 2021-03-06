from pages.login_page import LoginPage


def test_guest_should_see_login_fields(browser):
    url = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, url, 3)
    page.open()
    page.should_be_login_url()
    page.should_be_login_form()


def test_guest_should_see_register_fields(browser):
    url = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, url, 3)
    page.open()
    page.should_be_login_url()
    page.should_be_register_form()
