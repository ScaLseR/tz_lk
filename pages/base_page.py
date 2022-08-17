"""Base Page Module"""
from locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    """base class for all pages"""
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """open page"""
        self.browser.get(self.url)

    def go_to_login_page(self):
        """go to authorization page"""
        link = self.browser.find_element(*BasePageLocators.MAIL_LINK)
        link.click()

    def go_to_new_window(self):
        """go to new window in browser"""
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)

    def is_element_present(self, *args) -> bool:
        """find element on page"""
        try:
            self.browser.find_element(*args)
        except NoSuchElementException:
            return False
        return True

    def enter_text_to_input(self, text: str, *args):
        """entering text into field"""
        inp_text = self.browser.find_element(*args)
        inp_text.send_keys(text)

    def click_btn(self, *args):
        """clicking button"""
        btn_log = self.browser.find_element(*args)
        btn_log.click()

    def wait(self, *args):
        """waiting element"""
        self.browser.implicitly_wait(5)
        self.browser.find_element(*args)
