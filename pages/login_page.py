"""Login Page Module"""
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    """class for work with login page"""

    def authorized_user(self, login, password):
        """user authorization """
        self.go_to_new_window()
        self.enter_login(login)
        self.click_btn_nxt()
        self.enter_password(password)
        self.click_btn_ent()

    def enter_login(self, login):
        """entering login into field email"""
        inp_login = self.browser.find_element(*LoginPageLocators.EMAIL)
        inp_login.send_keys(login)

    def click_btn_nxt(self):
        """clicking button Next"""
        btn_log = self.browser.find_element(*LoginPageLocators.BTN_NEXT)
        btn_log.click()

    def click_btn_ent(self):
        """clicking button Enter"""
        btn_log = self.browser.find_element(*LoginPageLocators.BTN_ENTER)
        btn_log.click()

    def enter_password(self, password):
        """entering password into field password"""
        inp_pass = self.browser.find_element(*LoginPageLocators.PASS)
        inp_pass.send_keys(password)
