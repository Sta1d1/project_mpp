"""Тестирование страницы <Авторизация>"""
import time
import pyautogui
import allure
from selenium.webdriver import Remote
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Импорты методов и элементов
from src.methods.base_methods import BaseMethods as BM
from src.pages.authorization_page import AuthorizationPage as AP
from src.pages.settings_page import system_settings as SS
from src.pages.settings_page import developers as DP
from src.pages.settings_page import types_of_publications as TP

# -------------------------------------------- Система ----------------------------------------------------
def test_editing_technical_settings_on_settings_page(browser: Remote):
    """Редактирование настроек Система --> Технический"""
    AP(browser=browser).authorization()
    SS(browser=browser).go_to_settings_page()
    SS(browser=browser).editing_technical_settings()

def test_editing_receiving_supplies_on_settings_page(browser: Remote):
    """Редактирование настроек Система --> Получение поставок"""
    AP(browser=browser).authorization()
    SS(browser=browser).go_to_settings_page()
    SS(browser=browser).editing_receiving_supplies()

def test_editing_cryptographic_data_processing(browser: Remote):
    """Редактирование настроек Система --> Криптографическая обработка данных"""
    AP(browser=browser).authorization()
    SS(browser=browser).go_to_settings_page()
    SS(browser=browser).cryptographic_data_processing()

def test_editing_unpacking_supplies(browser: Remote):
    """Редактирование настроек Система --> Распаковки поставок"""
    AP(browser=browser).authorization()
    SS(browser=browser).go_to_settings_page()
    SS(browser=browser).unpacking_supplies()

def test_editing_validation_of_deliveries(browser: Remote):
    """Редактирование настроек Система --> валидация поставок"""
    AP(browser=browser).authorization()
    SS(browser=browser).go_to_settings_page()
    SS(browser=browser).validation_of_deliveries()

def test_editing_antivirus_check(browser: Remote):
    """Редактирование настроек Система --> Антивирусная проверка"""
    AP(browser=browser).authorization()
    SS(browser=browser).go_to_settings_page()
    SS(browser=browser).аntivirus_check()

def test_editing_calculation_of_checksums(browser: Remote):
    """Редактирование настроек Система --> Расчет контрольных сумм"""
    AP(browser=browser).authorization()
    SS(browser=browser).go_to_settings_page()
    SS(browser=browser).calculation_of_checksums()

def test_editing_publishing_data(browser: Remote):
    """Редактирование настроек Система --> Публикация данных"""
    AP(browser=browser).authorization()
    SS(browser=browser).go_to_settings_page()
    SS(browser=browser).publishing_data()

def test_editing_cleaning_the_supply_catalog(browser: Remote):
    """Редактирование настроек Система --> Очистка каталога поставок"""
    AP(browser=browser).authorization()
    SS(browser=browser).go_to_settings_page()
    SS(browser=browser).cleaning_the_supply_catalog()

def test_editing_application_programming_interface(browser: Remote):
    """Редактирование настроек Система --> API"""
    AP(browser=browser).authorization()
    SS(browser=browser).go_to_settings_page()
    SS(browser=browser).application_programming_interface()

def test_editing_notifications_settings(browser: Remote):
    """Редактирование настроек Система --> Уведомления"""
    AP(browser=browser).authorization()
    SS(browser=browser).go_to_settings_page()
    SS(browser=browser).notifications_settings()

def test_editing_activemq_message_broker(browser: Remote):
    """Редактирование настроек Система --> Брокер сообщений ActiveMQ"""
    AP(browser=browser).authorization()
    SS(browser=browser).go_to_settings_page()
    SS(browser=browser).activemq_message_broker()


# -------------------------------------------- Типы публикаций --------------------------------------------
def test_crud_places_of_publication(browser: Remote):
    """КРУД Места публикаций"""
    AP(browser=browser).authorization()
    TP(browser=browser).switch_to_publication_type()
    TP(browser=browser).crud_places_of_publication()


# -------------------------------------------- Маршруты ---------------------------------------------------



# -------------------------------------------- Сервисы ----------------------------------------------------



# -------------------------------------------- Логирование ------------------------------------------------



# -------------------------------------------- Разработчики -----------------------------------------------
def test_crud_developers(browser: Remote):
    """Создание, проверка, редактирование и удаление разработчика"""
    AP(browser=browser).authorization()
    DP(browser=browser).go_to_developers_page()
    DP(browser=browser).crud_developers()


# -------------------------------------------- Пользователи -----------------------------------------------



# -------------------------------------------- Роли -------------------------------------------------------



# -------------------------------------------- Привелегии -------------------------------------------------


