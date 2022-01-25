import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Select a browser: 'chrome' or 'firefox'. Chrome is used by default")
    parser.addoption('--language', action='store', default='en',
                     help="Specify the language of a browser. English is used by default")
    parser.addoption('--headless', action='store', default='false',
                     help="Open a browser invisible, without GUI is used by default")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption('language')
    headless = request.config.getoption('headless')
    browser = None

    if browser_name == 'chrome':
        print("\nStarting a Chrome browser for tests... ")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept-languages': language})
        if headless == 'true':
            options.add_argument('headless')
        browser = webdriver.Chrome(options=options)
        print("The Chrome browser has been successfully started!")

    elif browser_name == 'firefox':
        print("\nStarting a Firefox browser for tests... ")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)

    else:
        raise pytest.UsageError("--browser_name should be 'chrome' or 'firefox'")

    yield browser
    print("\nKilling the browser...")
    browser.quit()
    print("The browser has been successfully killed. R.I.P.")

