"""fixtures for work with browser Chrome"""
import pytest
from selenium.webdriver import Chrome


@pytest.fixture(scope="function")
def browser():
    """default browser -> GoogleChrome"""
    browser = Chrome()
    browser.set_window_size(1920, 1080)
    yield browser
    browser.quit()