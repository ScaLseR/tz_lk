"""Mail Page Module"""
from .base_page import BasePage
from .locators import MailPageLocators
from time import sleep


class MailPage(BasePage):
    """class for work with mail page"""

    def send_mail(self, address, text):
        """sending new mail to """
        self.close_promo()
        self.click_btn_new_mail()
        self.fill_address(address)
        self.fill_topic(text)
        self.fill_message(text)
        self.btn_send()
        sleep(300)

    def click_btn_new_mail(self):
        """clicking button Enter"""
        if self.is_element_present(*MailPageLocators.BTN_NEW_MAIL):
            btn_log = self.browser.find_element(*MailPageLocators.BTN_NEW_MAIL)
        else:
            btn_log = self.browser.find_element(*MailPageLocators.BTN_NEW_MAIL_LINK)
        btn_log.click()

    def close_promo(self):
        """close promo container"""
        btn_close = self.browser.find_element(*MailPageLocators.PROMO_CONT)
        btn_close.click()

    def fill_address(self, address):
        """fill address to"""
        inp_addr = self.browser.find_element(*MailPageLocators.ADDR_MAIL)
        inp_addr.send_keys(address)

    def fill_topic(self, text):
        """fill topic"""
        inp_topic = self.browser.find_element(*MailPageLocators.TOPIC)
        inp_topic.send_keys(text)

    def fill_message(self, text):
        """fill message"""
        inp_mess = self.browser.find_element(*MailPageLocators.MESSAGE)
        inp_mess.send_keys(text)

    def btn_send(self):
        """click send button"""
        btn_send = self.browser.find_element(*MailPageLocators.BTN_SEND)
        btn_send.click()
