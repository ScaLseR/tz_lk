"""fixtures for work with browser Chrome"""
import pytest
import chromedriver_autoinstaller
from selenium.webdriver import Chrome
from selenium.common.exceptions import WebDriverException


@pytest.fixture(scope="function")
def browser():
    """default browser -> GoogleChrome"""
    try:
        browser = Chrome()
    except WebDriverException:
        chromedriver_autoinstaller.install()
        browser = Chrome()
    browser.set_window_size(1920, 1080)
    yield browser
    browser.quit()
