"""Страница Отказоустойчивость"""
# Библиотеки
import time
import pyautogui
from selenium.webdriver import Remote
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

# Импорты методов и элементов
from src.methods.base_methods import BaseMethods as BM



class fault_tolerance:
    # ЭЛЕМЕНТЫ
    basic_login_xpath = '//*[@id="username"]'                                                                                                   # XPATH - Логин
    basic_password_xpath = '//*[@id="password"]'                                                                                                # XPATH - Пароль
    basic_submit_button = '//*[@id="login-button"]'                                                                                             # XPATH - Кнопка входа
    profile_button = '//*[@id="user-header-button"]'                                                                                            # Кнопка раскрытия профиля

    # ЗНАЧЕНИЯ
    url_antifraud_events = 'https://mpp-tst-mr1.star.lanit.ru/login'                                                                            # Страница <Авторизация>
    url_failure_management = 'https://mpp-tst-mr1.star.lanit.ru/failure-management'                                                             # Страница "Отказоустойчивость"
    basic_login = 'dr_adm'                                                                                                                      # Логин Администратора отказоустойчивости
    basic_password = 'Topaz123$'                                                                                                                # Пароль Администратора отказоустойчивости


    def __init__(self, browser) -> None:
        self.browser = browser
    
    def authorization_for_administrator_fault_tolerance(self):
        """Авторизация под администратором отказоустойчивости"""
        assert self.browser.current_url == self.url_antifraud_events        
        BM(browser=self.browser).getting_a_text_element(selector=self.basic_login_xpath) # Проверяю что страница прогрузилась
        BM(browser=self.browser).enter_text_in_the_element(selector=self.basic_login_xpath, input_text=self.basic_login) # Ввожу логин
        BM(browser=self.browser).enter_text_in_the_element(selector=self.basic_password_xpath, input_text=self.basic_password) # Ввожу пароль
        BM(browser=self.browser).click_on_the_element(selector=self.basic_submit_button) # Нажимаю кнопку "Войти"
        BM(browser=self.browser).checking_the_presence_of_an_element_on_the_page(selector=self.profile_button) # Проверяю что страница прогрузилась


