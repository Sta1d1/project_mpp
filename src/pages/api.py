"""API"""
# Библиотеки
import time
import requests
from selenium.webdriver import Remote
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException




class API:
    # ЭЛЕМЕНТЫ
    

    # ЗНАЧЕНИЯ


    def __init__(self, browser) -> None:
        self.browser = browser

    def login():
        url = "https://mpp-tst-mr1.star.lanit.ru/api/login"
        payload = 'username=admin&password=Topaz123%24'
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        response = requests.post(url, headers=headers, data=payload).json()
        return response['accessToken']