"""Локальный запуск автотестов"""
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser", default="ch", choices=["ya", "ch", "ff"]
    )
    parser.addoption(
        "--headless", action="store_true", default = False
    )
    parser.addoption(
        "--yadriver", action="store_true", default="ссылка на yandex driver"
    )
    parser.addoption(
        "--url", default="https://mpp-tst-mr1.star.lanit.ru/"
    )


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless_mode = request.config.getoption("--headless")
    yadriver = request.config.getoption("--yadriver")
    url = request.config.getoption("--url")

    options = None
    if browser_name == "ya":
        options = Options()
        if headless_mode:
            options.add_argument("headless=new")
        options.binary_location = "/usr/bin/yandex-browser"
        service = Service(executable_path=yadriver)
        browser = webdriver.Chrome(service=service, options=options)
    elif browser_name == "ch":
        options = Options()
        if headless_mode:
            options.add_argument("headless=new")
        browser = webdriver.Chrome(service=Service(), options=options)
    elif browser_name == "ff":
        options = FFOptions()
        if headless_mode:
            options.add_argument("--headless")
        browser = webdriver.Firefox(service=FFService(), options=options)
    else:
        raise ValueError(f"Browser {browser_name} not supported")


    browser.maximize_window()
    browser.get(url)

    yield browser

    browser.close()
