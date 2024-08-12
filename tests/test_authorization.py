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
from src.pages.fault_tolerance import fault_tolerance as FT


def test_base_authorization(browser: Remote):
    """Авторизация и выход"""
    AP(browser=browser).authorization()
    AP(browser=browser).logout_base_account()

def test_authorization_with_incorrect_login(browser: Remote):
    """Авторизация с некорректным логином"""
    AP(browser=browser).authorization_with_incorrect_login()

def test_authorization_with_incorrect_password(browser: Remote):
    """Авторизация с некорректным паролем"""
    AP(browser=browser).authorization_with_incorrect_password()

def test_authorization_with_incorrect_all_data(browser: Remote):
    """Авторизация с некорректными данными"""
    AP(browser=browser).authorization_with_incorrect_all_data()

def test_authorization_and_exit_via_profile(browser: Remote):
    """Авторизация с последующим логаутом через профиль"""
    AP(browser=browser).authorization()
    AP(browser=browser).authorization_and_exit_via_profile()

def test_authorization_for_administrator_fault_tolerance(browser: Remote):
    """Авторизация под администратором отказоустойчивости и выход"""
    FT(browser=browser).authorization_for_administrator_fault_tolerance()
    AP(browser=browser).logout_base_account()