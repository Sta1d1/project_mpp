"""Тестирование страницы <Авторизация>"""
import time
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
from src.pages.fault_tolerance import fault_tolerance as FT

@allure.feature("Авторизация")
@allure.story('Авторизовация и выход')
def test_base_authorization(browser: Remote):
    AP(browser=browser).authorization()
    AP(browser=browser).logout_base_account()

@allure.feature("Авторизация")
@allure.story('Авторизация с некорректным логином')
def test_authorization_with_incorrect_login(browser: Remote):
    AP(browser=browser).authorization_with_incorrect_login()

@allure.feature("Авторизация")
@allure.story('Авторизация с некорректным паролем')
def test_authorization_with_incorrect_password(browser: Remote):
    AP(browser=browser).authorization_with_incorrect_password()

@allure.feature("Авторизация")
@allure.story('Авторизация с некорректными данными')
def test_authorization_with_incorrect_all_data(browser: Remote):
    AP(browser=browser).authorization_with_incorrect_all_data()

@allure.feature("Авторизация")
@allure.story('Авторизация с последующим логаутом через профиль')
def test_authorization_and_exit_via_profile(browser: Remote):
    AP(browser=browser).authorization()
    AP(browser=browser).authorization_and_exit_via_profile()

@allure.feature("Авторизация")
@allure.story('Авторизация под администратором отказоустойчивости и выход')
def test_authorization_for_administrator_fault_tolerance(browser: Remote):
    FT(browser=browser).authorization_for_administrator_fault_tolerance()
    AP(browser=browser).logout_base_account()