"""Mail Page Module"""
from .base_page import BasePage
from locators import MailPageLocators


class MailPage(BasePage):
    """class for work with mail page"""

    def send_mail(self, address: str, text: str):
        """sending new mail to """
        self.click_btn(*MailPageLocators.PROMO_CONT)
        self.click_btn_new_mail()
        self.enter_text_to_input(address, *MailPageLocators.ADDR_MAIL)
        self.enter_text_to_input(text, *MailPageLocators.TOPIC)
        self.enter_text_to_input(text, *MailPageLocators.MESSAGE)
        self.click_btn(*MailPageLocators.BTN_SEND)

    def click_btn_new_mail(self):
        """clicking button Enter"""
        if self.is_element_present(*MailPageLocators.BTN_NEW_MAIL):
            btn_log = self.browser.find_element(*MailPageLocators.BTN_NEW_MAIL)
        else:
            btn_log = self.browser.find_element(*MailPageLocators.BTN_NEW_MAIL_LINK)
        btn_log.click()

    def check_sending(self) -> bool:
        """check sending mail"""
        self.wait(*MailPageLocators.SENT_PAGE)
        message = self.browser.find_element(*MailPageLocators.SENDING_TEXT)
        if message.text == 'Письмо отправлено':
            return True
        return False
