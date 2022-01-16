import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Select a browser: 'chrome' or 'firefox'. Chrome is used by default")
    parser.addoption('--language', action='store', default='en',
                     help="Specify the language of a browser. English is used by default")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption('language')
    browser = None

    if browser_name == 'chrome':
        print("\nStarting a Chrome browser for tests")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept-languages': language})
        browser = webdriver.Chrome(options=options)

    elif browser_name == 'firefox':
        print("\nStarting a Firefox browser for tests")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)

    else:
        raise pytest.UsageError("--browser_name should be 'chrome' or 'firefox'")

    yield browser
    print("\nQuitting the browser")
    browser.quit()
