from pages.order_page import OrderPage
from pages.locators import MainPageLocators
import pytest


order = [
    'ыфвфывфаф', 'ывфвыфвфывфыв',
    'выфаыфваываы', 'Черкизовская',
    '34245254352', '30.12.2024',
    'сутки'
]
@pytest.mark.parametrize('names', [order])                    
def test_placing_an_order(browser, names,):
    name, last_name, address, metro_station, phone_number,\
    when_to_deliver, rental_period = names
    link = 'https://qa-scooter.praktikum-services.ru/'
    page = OrderPage(browser, link)
    page.open()
    page.go_to_order(*MainPageLocators.ORDER_1)
    page.fill_out_the_order(name, last_name, address, metro_station,phone_number,
            when_to_deliver, rental_period
            )
    page.check_order_accepted()

def test_logo_scooter_go_to_main_page(browser):
    url = 'https://qa-scooter.praktikum-services.ru/order'
    page = OrderPage(browser, url)
    page.open()
    page.go_to_main_page()
    page.current_main_page()

def test_logo_yandex_go_to_yandex_page(browser):
    url = 'https://qa-scooter.praktikum-services.ru/order'
    page = OrderPage(browser, url)
    page.open()
    page.go_to_yandex_page()
    page.current_yandex_page()