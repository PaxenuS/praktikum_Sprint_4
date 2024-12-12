from pages.main_page import MainPage
import pytest


class TestMainPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = 'https://qa-scooter.praktikum-services.ru/'
        self.page = MainPage(browser, link)
        self.page.open()
        self.page.go_to_sub_header()

    def test_faq_1(self):
        self.page.faq_1()
    
    def test_faq_2(self):
        self.page.faq_2()

    def test_faq_3(self):
        self.page.faq_3()
    
    def test_faq_4(self):
        self.page.faq_4()

    def test_faq_5(self):
        self.page.faq_5()

    def test_faq_6(self):
        self.page.faq_6()

    def test_faq_7(self):
        self.page.faq_7()

    def test_faq_8(self):
        self.page.faq_8()