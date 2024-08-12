"""Тестирование страницы <Отказоустойчивость>"""
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

