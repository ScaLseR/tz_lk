"""locators for all class"""
from selenium.webdriver.common.by import By


class BasePageLocators:
    """locators for BasePage"""
    MAIL_LINK = (By.CSS_SELECTOR, '[data-testid="logged-out-email"]')


class LoginPageLocators:
    """locators for LoginPage"""
    BTN_NEXT = (By.CSS_SELECTOR, '[data-test-id="next-button"]')
    EMAIL = (By.CSS_SELECTOR, '[name="username"]')
    PASS = (By.CSS_SELECTOR, '[name="password"]')
    BTN_ENTER = (By.CSS_SELECTOR, '[data-test-id="submit-button"]')


class MailPageLocators:
    """locators for MailPage"""
    BTN_NEW_MAIL = (By.CSS_SELECTOR, '.compose-button__txt')
