"""Login Page Module"""
from .base_page import BasePage
from locators import LoginPageLocators


class LoginPage(BasePage):
    """class for work with login page"""

    def authorized_user(self, login: str, password: str):
        """user authorization """
        self.go_to_new_window()
        self.enter_text_to_input(login, *LoginPageLocators.EMAIL)
        self.click_btn(*LoginPageLocators.BTN_NEXT)
        self.enter_text_to_input(password, *LoginPageLocators.PASS)
        self.click_btn(*LoginPageLocators.BTN_ENTER)
