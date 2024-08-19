"""Тестирование страницы <Авторизация>"""
import time
import pytest
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
from src.pages.settings_page import roles_pages as RP
from src.pages.settings_page import logging as LP
from src.pages.settings_page import services as SP

# -------------------------------------------- Система ----------------------------------------------------
@allure.feature("Настройки Системы")
@allure.story('Редактирование настроек Система --> Технический')
def test_editing_technical_settings_on_settings_page(browser: Remote):
    AP(browser=browser).authorization()
    SS(browser=browser).go_to_settings_page()
    SS(browser=browser).editing_technical_settings()

@allure.feature("Настройки Системы")
@allure.story('Редактирование настроек Система --> Получение поставок')
def test_editing_receiving_supplies_on_settings_page(browser: Remote):
    AP(browser=browser).authorization()
    SS(browser=browser).go_to_settings_page()
    SS(browser=browser).editing_receiving_supplies()

@allure.feature("Настройки Системы")
@allure.story('Редактирование настроек Система --> Криптографическая обработка данных')
def test_editing_cryptographic_data_processing(browser: Remote):
    AP(browser=browser).authorization()
    SS(browser=browser).go_to_settings_page()
    SS(browser=browser).cryptographic_data_processing()

@allure.feature("Настройки Системы")
@allure.story('Редактирование настроек Система --> Распаковки поставок')
def test_editing_unpacking_supplies(browser: Remote):
    AP(browser=browser).authorization()
    SS(browser=browser).go_to_settings_page()
    SS(browser=browser).unpacking_supplies()

@allure.feature("Настройки Системы")
@allure.story('Редактирование настроек Система --> валидация поставок')
def test_editing_validation_of_deliveries(browser: Remote):
    AP(browser=browser).authorization()
    SS(browser=browser).go_to_settings_page()
    SS(browser=browser).validation_of_deliveries()

@allure.feature("Настройки Системы")
@allure.story('Редактирование настроек Система --> Антивирусная проверка')
def test_editing_antivirus_check(browser: Remote):
    AP(browser=browser).authorization()
    SS(browser=browser).go_to_settings_page()
    SS(browser=browser).аntivirus_check()

@allure.feature("Настройки Системы")
@allure.story('Редактирование настроек Система --> Расчет контрольных сумм')
def test_editing_calculation_of_checksums(browser: Remote):
    AP(browser=browser).authorization()
    SS(browser=browser).go_to_settings_page()
    SS(browser=browser).calculation_of_checksums()

@allure.feature("Настройки Системы")
@allure.story('Редактирование настроек Система --> Публикация данных')
def test_editing_publishing_data(browser: Remote):
    AP(browser=browser).authorization()
    SS(browser=browser).go_to_settings_page()
    SS(browser=browser).publishing_data()

@allure.feature("Настройки Системы")
@allure.story('Редактирование настроек Система --> Очистка каталога поставок')
def test_editing_cleaning_the_supply_catalog(browser: Remote):
    AP(browser=browser).authorization()
    SS(browser=browser).go_to_settings_page()
    SS(browser=browser).cleaning_the_supply_catalog()

@allure.feature("Настройки Системы")
@allure.story('Редактирование настроек Система --> API')
def test_editing_application_programming_interface(browser: Remote):
    AP(browser=browser).authorization()
    SS(browser=browser).go_to_settings_page()
    SS(browser=browser).application_programming_interface()

@allure.feature("Настройки Системы")
@allure.story('Редактирование настроек Система --> Уведомления')
def test_editing_notifications_settings(browser: Remote):
    AP(browser=browser).authorization()
    SS(browser=browser).go_to_settings_page()
    SS(browser=browser).notifications_settings()

@allure.feature("Настройки Системы")
@allure.story('КРУД Места публикаций')
def test_editing_activemq_message_broker(browser: Remote):
    """Редактирование настроек Система --> Брокер сообщений ActiveMQ"""
    AP(browser=browser).authorization()
    SS(browser=browser).go_to_settings_page()
    SS(browser=browser).activemq_message_broker()


# -------------------------------------------- Типы публикаций --------------------------------------------
@allure.feature("Настройки Места публикаций")
@allure.story('КРУД Места публикаций')
def test_crud_places_of_publication(browser: Remote):
    AP(browser=browser).authorization()
    TP(browser=browser).switch_to_publication_type()
    TP(browser=browser).crud_places_of_publication()


# -------------------------------------------- Маршруты ---------------------------------------------------



# -------------------------------------------- Сервисы ----------------------------------------------------
@allure.feature("Сервисы")
@allure.story('Отключение и включение каждого сервиса')
@pytest.mark.parametrize("service_check, xpath_stop_service, xpath_start_service",
	[("//*[@id='receiver-service-card-select-checkbox']/..", 
    "//*[@id='receiver-inactive-service-status-chip']/span", 
    "//*[@id='receiver-service-start-button']"),
    ("//*[@id='decryption-service-card-select-checkbox']/..",
    "//*[@id='decryption-inactive-service-status-chip']/span",
    "//*[@id='decryption-service-start-button']"),
    ("//*[@id='unzip-service-card-select-checkbox']/..",
    "//*[@id='unzip-inactive-service-status-chip']/span",
    "//*[@id='unzip-service-start-button']"),
    ("//*[@id='validator-service-card-select-checkbox']/..",
    "//*[@id='validator-inactive-service-status-chip']/span",
    "//*[@id='validator-service-start-button']"),
    ("//*[@id='antivir-service-card-select-checkbox']/..",
    "//*[@id='antivir-inactive-service-status-chip']/span",
    "//*[@id='antivir-service-start-button']"),
    ("//*[@id='checkSum-service-card-select-checkbox']/..",
    "//*[@id='checkSum-inactive-service-status-chip']/span",
    "//*[@id='checkSum-service-start-button']"),
    ("//*[@id='publisher-service-card-select-checkbox']/..",
    "//*[@id='publisher-inactive-service-status-chip']/span",
    "//*[@id='publisher-service-start-button']"),
    ("//*[@id='cleaner-service-card-select-checkbox']/..",
    "//*[@id='cleaner-inactive-service-status-chip']/span", 
    "//*[@id='cleaner-service-start-button']"),
    ( "//*[@id='notification-service-card-select-checkbox']/..",
    "//*[@id='notification-inactive-service-status-chip']/span",
    "//*[@id='notification-service-start-button']"),
    ("//*[@id='activemq-service-card-select-checkbox']/..",
    "//*[@id='activemq-inactive-service-status-chip']/span",
    "//*[@id='activemq-service-start-button']")])
def test_disabling_and_enabling_services(browser: Remote, service_check, xpath_stop_service, xpath_start_service):
    AP(browser=browser).authorization()
    SP(browser=browser).go_to_services_page()
    SP(browser=browser).disabling_and_enabling_services(service_check, xpath_stop_service, xpath_start_service)


# -------------------------------------------- Логирование ------------------------------------------------
@allure.feature("Настройки Логирование")
@allure.story('Проверка логирования')
def test_check_logging(browser: Remote):
    AP(browser=browser).authorization()
    LP(browser=browser).go_to_logging_page()
    LP(browser=browser).check_logging()


# -------------------------------------------- Разработчики -----------------------------------------------
@allure.feature("Настройки Разработчики")
@allure.story('Создание, проверка, редактирование и удаление разработчика')
def test_crud_developers(browser: Remote):
    AP(browser=browser).authorization()
    DP(browser=browser).go_to_developers_page()
    DP(browser=browser).crud_developers()


# -------------------------------------------- Пользователи -----------------------------------------------



# -------------------------------------------- Роли -------------------------------------------------------
@allure.feature("Роли")
@allure.story('КРУД Роли')
def test_crud_roles(browser: Remote):
    AP(browser=browser).authorization()
    RP(browser=browser).go_to_roles_page()
    RP(browser=browser).crud_roles()

# -------------------------------------------- Привелегии -------------------------------------------------


