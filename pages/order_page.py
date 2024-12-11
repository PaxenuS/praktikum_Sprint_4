from .base_page import BasePage
from .locators import OrderPageLocators, MainPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(BasePage):
    def go_to_order(self, metod, locator):
        order = self.browser.find_element(metod, locator)
        order.click()

    def fill_out_the_order(
            self, name, last_name, address, metro_station,phone_number,
            when_to_deliver, rental_period
            ):
        field_name = self.browser.find_element(*OrderPageLocators.NAME)
        field_name.send_keys(name)
        field_last_name = self.browser.find_element(*OrderPageLocators.LAST_NAME)
        field_last_name.send_keys(last_name)
        field_address = self.browser.find_element(*OrderPageLocators.ADDRESS)
        field_address.send_keys(address)
        field_metro_station = self.browser.find_element(*OrderPageLocators.METRO_STATION)
        field_metro_station.click()
        field_metro_station.send_keys(metro_station)
        metro_station_accept = self.browser.find_element(*OrderPageLocators.METRO_STATION_SELECT)
        metro_station_accept.click()
        field_phone_number = self.browser.find_element(*OrderPageLocators.PHONE_NUMBER)
        field_phone_number.send_keys(phone_number)
        botton_1 = self.browser.find_element(*OrderPageLocators.BOTTON_PAGE_1)
        botton_1.click()
        field_when_to_deliver = self.browser.find_element(*OrderPageLocators.WHEN_TO_DELIVER)
        field_when_to_deliver.click()
        field_when_to_deliver.send_keys(when_to_deliver)
        field_when_to_deliver.send_keys(Keys.RETURN)
        field_rental_period = self.browser.find_element(*OrderPageLocators.RENTAL_PERIOD)
        field_rental_period.click()
        options = self.browser.find_elements(*OrderPageLocators.RENTAL_PERIOD_OPTIONS)
        for option in options:
            if option.text == rental_period:
                option.click()
                break
        selection_color = self.browser.find_element(*OrderPageLocators.COLOR_SELECTION_1)
        selection_color.click()
        botton_2 = self.browser.find_element(*OrderPageLocators.BOTTON_PAGE_2)
        botton_2.click()
        botton_accepted = self.browser.find_element(*OrderPageLocators.BOTTON_ACCEPTED)
        botton_accepted.click()

    def check_order_accepted(self):
        accept = self.browser.find_element(*OrderPageLocators.ORDER_ACCEPTED).text
        print(f"Текст заголовка: {accept}")
        assert 'Заказ оформлен' in accept, 'Заказ не принят'
