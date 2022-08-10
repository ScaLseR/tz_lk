"""Mail Page Module"""
from .base_page import BasePage
from .locators import MailPageLocators
from time import sleep


class MailPage(BasePage):
    """class for work with mail page"""

    def send_mail(self, addres, text):
        """sending new mail to """
        self.click_btn_new_mail()

    def click_btn_new_mail(self):
        """clicking button Enter"""
        if self.is_element_present(*MailPageLocators.BTN_NEW_MAIL):
            btn_log = self.browser.find_element(*MailPageLocators.BTN_NEW_MAIL)
        else:
            btn_log = self.browser.find_element(*MailPageLocators.BTN_NEW_MAIL_LINK)
        btn_log.click()

