import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-gb')



@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
