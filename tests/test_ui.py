"""Test Cases Module"""
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.mail_page import MailPage


_URL = 'https://mail.ru'
_LOGIN = 'tz_lk'
_PASSWORD = '123qazqwe!@#'
_EMAIL = 'tz_lk@mail.ru'
_TEXT = 'Выполнение ТЗ Скорик А.С.'


def test_send_email(browser) -> None:
    """test case"""
    page = MainPage(browser, _URL)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.authorized_user(_LOGIN, _PASSWORD)
    mail_page = MailPage(browser, browser.current_url)
    mail_page.send_mail(_EMAIL, _TEXT)

