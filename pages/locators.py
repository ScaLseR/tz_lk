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
    BTN_NEW_MAIL_LINK = (By.CSS_SELECTOR, '.ico.ico_16-compose.ico_size_s')
    PROMO_CONT = (By.CSS_SELECTOR, '.ph-project-promo-close-icon__container.svelte-m7oyyo')
    ADDR_MAIL = (By.XPATH, '//input[@class="container--H9L5q size_s--3_M-_"]')
    TOPIC = (By.CSS_SELECTOR, '[name="Subject"]')
    MESSAGE = (By.CSS_SELECTOR, '[role="textbox"]')
    BTN_SEND = (By.CSS_SELECTOR, '[data-test-id="send"]')
    SENT_PAGE = (By.CSS_SELECTOR, '.layer-sent-page')
