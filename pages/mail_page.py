"""Mail Page Module"""
from .base_page import BasePage
from .locators import MailPageLocators


class MailPage(BasePage):
    """class for work with mail page"""

    def send_mail(self, addres, text):
        """sending new mail to """
        self.click_btn_new_mail()

    def click_btn_new_mail(self):
        """clicking button Enter"""
        btn_log = self.browser.find_element(*MailPageLocators.BTN_NEW_MAIL)
        btn_log.click()

