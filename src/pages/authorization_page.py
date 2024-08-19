"""Авторизация"""
# Библиотеки
import time
from selenium.webdriver import Remote
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

# Импорты методов и элементов
from src.methods.base_methods import BaseMethods as BM


class AuthorizationPage:


    # ЭЛЕМЕНТЫ
    basic_login_xpath = '//*[@id="username"]'                                                                                                   # XPATH - Логин
    basic_password_xpath = '//*[@id="password"]'                                                                                                # XPATH - Пароль
    basic_submit_button = '//*[@id="login-button"]'                                                                                             # XPATH - Кнопка входа
    profile_button = '//*[@id="user-header-button"]'                                                                                            # Кнопка раскрытия профиля
    profile_profile_button_link = '//*[@id="profile-header-button"]'                                                                            # Кнопка "Профиль" в профиле справа сверху
    logout_button = '//*[@id="logout-header-button"]'                                                                                           # Кнопка выхода (из профиля справа сверху)
    logout_button_via_profile = '//*[@id="profile-logout-button"]'                                                                              # Кнопка выхода со страницы "Профиль"
    basic_allert_incorrect_data = '//*[@id="alert-message"]/div[2]/p'                                                                           # Аллерт о некорректном логине/пароле

    # ЗНАЧЕНИЯ
    url_antifraud_events = 'https://mpp-tst-mr1.star.lanit.ru/login'                                                                            # Страница <Авторизация>
    basic_login = 'admin'                                                                                                                       # Логин аккаунта
    basic_password = 'Topaz123$'                                                                                                                # Пароль аккаунта
    text_allert_incorrect_data = 'Вам запрещён доступ в систему. Проверьте правильность ввода логина или пароля.'                               # Текст о некорректном логине/пароле                  

    def __init__(self, browser) -> None:
        self.browser = browser
    
    def authorization(self):
        """Базовая авторизация"""
        assert self.browser.current_url == self.url_antifraud_events        
        BM(browser=self.browser).getting_a_text_element(selector=self.basic_login_xpath) # Проверяю что страница прогрузилась
        BM(browser=self.browser).enter_text_in_the_element(selector=self.basic_login_xpath, input_text=self.basic_login) # Ввожу логин
        BM(browser=self.browser).enter_text_in_the_element(selector=self.basic_password_xpath, input_text=self.basic_password) # Ввожу пароль
        BM(browser=self.browser).click_on_the_element(selector=self.basic_submit_button) # Нажимаю кнопку "Войти"
        BM(browser=self.browser).checking_the_presence_of_an_element_on_the_page(selector=self.profile_button)
    
    def logout_base_account(self):
        """Выход из аккаунта"""
        BM(browser=self.browser).getting_a_text_element(selector=self.profile_button)
        BM(browser=self.browser).click_on_the_element(selector=self.profile_button)
        BM(browser=self.browser).click_on_the_element(selector=self.logout_button)
        BM(browser=self.browser).getting_a_text_element(selector=self.basic_login_xpath) # Проверяю что страница прогрузилась
        assert self.browser.current_url == self.url_antifraud_events        
        
    def authorization_with_incorrect_login(self):
        """Попытка авторизации с некорректным логином"""
        assert self.browser.current_url == self.url_antifraud_events        
        BM(browser=self.browser).getting_a_text_element(selector=self.basic_login_xpath) # Проверяю что страница прогрузилась
        BM(browser=self.browser).enter_text_in_the_element(selector=self.basic_login_xpath, input_text='u42294ufs') # Ввожу логин
        BM(browser=self.browser).enter_text_in_the_element(selector=self.basic_password_xpath, input_text=self.basic_password) # Ввожу пароль
        BM(browser=self.browser).click_on_the_element(selector=self.basic_submit_button) # Нажимаю кнопку "Войти"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.basic_allert_incorrect_data, second_value=self.text_allert_incorrect_data)

    def authorization_with_incorrect_password(self):
        """Попытка авторизации с некорректным паролем"""
        assert self.browser.current_url == self.url_antifraud_events        
        BM(browser=self.browser).getting_a_text_element(selector=self.basic_login_xpath) # Проверяю что страница прогрузилась
        BM(browser=self.browser).enter_text_in_the_element(selector=self.basic_login_xpath, input_text=self.basic_login) # Ввожу логин
        BM(browser=self.browser).enter_text_in_the_element(selector=self.basic_password_xpath, input_text='hugs4kg8439') # Ввожу пароль
        BM(browser=self.browser).click_on_the_element(selector=self.basic_submit_button) # Нажимаю кнопку "Войти"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.basic_allert_incorrect_data, second_value=self.text_allert_incorrect_data)

    def authorization_with_incorrect_all_data(self):
        """Попытка авторизации с некорректным логином и паролем"""
        assert self.browser.current_url == self.url_antifraud_events        
        BM(browser=self.browser).getting_a_text_element(selector=self.basic_login_xpath) # Проверяю что страница прогрузилась
        BM(browser=self.browser).enter_text_in_the_element(selector=self.basic_login_xpath, input_text='f34higho') # Ввожу логин
        BM(browser=self.browser).enter_text_in_the_element(selector=self.basic_password_xpath, input_text='hugs4kg8439') # Ввожу пароль
        BM(browser=self.browser).click_on_the_element(selector=self.basic_submit_button) # Нажимаю кнопку "Войти"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.basic_allert_incorrect_data, second_value=self.text_allert_incorrect_data)

    def authorization_and_exit_via_profile(self):
        """Выход через профиль из аккаунта"""
        BM(browser=self.browser).checking_the_presence_of_an_element_on_the_page(selector=self.profile_button) 
        BM(browser=self.browser).click_on_the_element(selector=self.profile_button) # Раскрываю профиль
        BM(browser=self.browser).click_on_the_element(selector=self.profile_profile_button_link) # Перехожу в профиль
        BM(browser=self.browser).checking_the_presence_of_an_element_on_the_page(selector=self.logout_button_via_profile)
        BM(browser=self.browser).click_on_the_element(selector=self.logout_button_via_profile) # Нажимаю кнопку "Выйти"
        BM(browser=self.browser).checking_the_presence_of_an_element_on_the_page(selector=self.basic_login_xpath) 
        assert self.browser.current_url == self.url_antifraud_events

