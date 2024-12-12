from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_sub_header(self):
        sub_header = self.browser.find_element(*MainPageLocators.SUB_HEADER)
        self.browser.execute_script("arguments[0].scrollIntoView();", sub_header) 

    def faq_1(self):
        self.browser.find_element(*MainPageLocators.FAQ_1).click()
        answer = self.browser.find_element(*MainPageLocators.FAQ_1_ANSWER)
        text = answer.text
        correct_answer = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        assert correct_answer == text , f'Ответ {text} не верный'

    def faq_2(self):
        self.browser.find_element(*MainPageLocators.FAQ_2).click()
        answer = self.browser.find_element(*MainPageLocators.FAQ_2_ANSWER)
        text = answer.text
        correct_answer = 'Пока что у нас так: один заказ — один самокат. '
        assert correct_answer in text, f'Ответ {text} не верный'

    def faq_3(self):
        self.browser.find_element(*MainPageLocators.FAQ_3).click()
        answer = self.browser.find_element(*MainPageLocators.FAQ_3_ANSWER)
        text = answer.text
        correct_answer = 'Допустим, вы оформляете заказ на 8 мая.'
        assert correct_answer in text, f'Ответ {text} не верный'

    def faq_4(self):
        self.browser.find_element(*MainPageLocators.FAQ_4).click()
        answer = self.browser.find_element(*MainPageLocators.FAQ_4_ANSWER)
        text = answer.text
        correct_answer = 'Только начиная с завтрашнего дня. '
        assert correct_answer in text, f'Ответ {text} не верный'

    def faq_5(self):
        self.browser.find_element(*MainPageLocators.FAQ_5).click()
        answer = self.browser.find_element(*MainPageLocators.FAQ_5_ANSWER)
        text = answer.text
        correct_answer = 'Пока что нет! Но если что-то срочное'
        assert correct_answer in text, f'Ответ {text} не верный'

    def faq_6(self):
        self.browser.find_element(*MainPageLocators.FAQ_6).click()
        answer = self.browser.find_element(*MainPageLocators.FAQ_6_ANSWER)
        text = answer.text
        correct_answer = 'Самокат приезжает к вам с полной зарядкой.'
        assert correct_answer in text, f'Ответ {text} не верный'

    def faq_7(self):
        self.browser.find_element(*MainPageLocators.FAQ_7).click()
        answer = self.browser.find_element(*MainPageLocators.FAQ_7_ANSWER)
        text = answer.text
        correct_answer = 'Да, пока самокат не привезли. '
        assert correct_answer in text, f'Ответ {text} не верный'

    def faq_8(self):
        self.browser.find_element(*MainPageLocators.FAQ_8).click()
        answer = self.browser.find_element(*MainPageLocators.FAQ_8_ANSWER)
        text = answer.text
        correct_answer = 'Да, обязательно. Всем самокатов!'
        assert correct_answer in text, f'Ответ {text} не верный'

    