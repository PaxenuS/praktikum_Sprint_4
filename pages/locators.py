from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGO_SAMOKAT = (By.CSS_SELECTOR, '.Header_LogoScooter__3lsAR')
    LOGO_YANDEX = (By.CSS_SELECTOR, '.Header_LogoYandex__3TSOI')
    LOGO_DZEN = (By.CSS_SELECTOR, '#stella_logo_3464--react > path:nth-child(2)')

class MainPageLocators():
    ORDER_1 = (By.CSS_SELECTOR, '.Header_Nav__AGCXC > button:nth-child(1)')
    ORDER_2 = (By.CSS_SELECTOR, '.Button_Middle__1CSJM')
    SUB_HEADER = (By.CSS_SELECTOR, '.Home_FourPart__1uthg > div:nth-child(1)')
    FAQ_1_= (By.CSS_SELECTOR, '#accordion__heading-0')
    FAQ_2 = (By.CSS_SELECTOR, '#accordion__heading-1')
    FAQ_3 = (By.CSS_SELECTOR, '#accordion__heading-2')
    FAQ_4 = (By.CSS_SELECTOR, '#accordion__heading-3')
    FAQ_5 = (By.CSS_SELECTOR, '#accordion__heading-4')
    FAQ_6 = (By.CSS_SELECTOR, '#accordion__heading-5')
    FAQ_7 = (By.CSS_SELECTOR, '#accordion__heading-6')
    FAQ_8 = (By.CSS_SELECTOR, '#accordion__heading-7')

class OrderPageLocators():
    NAME = (By.CSS_SELECTOR, '.Order_Form__17u6u > div:nth-child(1) > input:nth-child(1)')
    LAST_NAME = (By.CSS_SELECTOR, 'div.Input_InputContainer__3NykH:nth-child(2) > input:nth-child(1)')
    ADDRESS = (By.CSS_SELECTOR, 'div.Input_InputContainer__3NykH:nth-child(3) > input:nth-child(1)')
    METRO_STATION = (By.CSS_SELECTOR, '.select-search__input')
    METRO_STATION_SELECT = (By.XPATH, '//div[2]/div[4]/div/div[2]')
    PHONE_NUMBER = (By.CSS_SELECTOR, 'div.Input_InputContainer__3NykH:nth-child(5) > input:nth-child(1)')
    BOTTON_PAGE_1 = (By.CSS_SELECTOR, '.Button_Middle__1CSJM')
    WHEN_TO_DELIVER = (By.XPATH, '//div[2]/div[2]/div[1]/div[1]/div/input')
    RENTAL_PERIOD = (By.CSS_SELECTOR, '.Dropdown-placeholder')
    RENTAL_PERIOD_OPTIONS = (By.CSS_SELECTOR, '.Dropdown-menu>div')
    COLOR_SELECTION_1 = (By.CSS_SELECTOR, '#black')
    COLOR_SELECTION_2 = (By.CSS_SELECTOR, '#grey')
    BOTTON_PAGE_2 = (By.CSS_SELECTOR, 'button.Button_Middle__1CSJM:nth-child(2)')
    BOTTON_ACCEPTED = (By.CSS_SELECTOR, 'div.Order_Buttons__1xGrp:nth-child(2) > button:nth-child(2)')
    ORDER_ACCEPTED = (By.CSS_SELECTOR,'.Order_Modal__YZ-d3>div:nth-child(1)')

