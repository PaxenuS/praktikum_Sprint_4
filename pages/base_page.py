from .locators import BasePageLocators
from selenium.webdriver.support.ui import WebDriverWait


class BasePage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_main_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGO_SAMOKAT)
        link.click()

    def go_to_yandex_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGO_YANDEX)
        link.click()

    def current_yandex_page(self):
        link = 'https://dzen.ru/?yredirect=true'
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.browser.find_element(*BasePageLocators.LOGO_DZEN)
        assert self.browser.current_url == link, 'Мы не на странице яндекса'

    def current_main_page(self):
        link = 'https://qa-scooter.praktikum-services.ru/'
        assert self.browser.current_url == link, 'Мы не на главной странице'