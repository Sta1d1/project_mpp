import pytest
import os
import random
import time
import allure # type: ignore
import requests


from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options as ChromiumService
from selenium.webdriver.firefox.options import Options as FFService
from selenium.webdriver.edge.options import Options as EdgeService
from selenium.webdriver.safari.options import Options as SafariService
"""
Для запуска теста с allure использовать комманду: pytest -v -s --alluredir results
Для запуска тестов в многопотоке: pytest -n4 где 4 означает количество потоков
"""

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default='https://mpp-tst-mr1.star.lanit.ru/')
    parser.addoption("--drivers", action="store", default=os.path.expanduser("~/drivers"))
    parser.addoption("--executor", action="store", default='http://172.29.39.81:4444/wd/hub')
    parser.addoption("--vnc", action="store_true", default=True)
    parser.addoption("--logs", action="store_true", default=True)
    parser.addoption("--videos", action="store_true", default=True)
    parser.addoption("--bv", default='106.0')

@allure.step("Waiting for availability {url}")
def wait_url_data(url, timeout=10):
    """Метод ожидания доступности урла"""
    while timeout:
        response = requests.get(url)
        if not response.ok:
            time.sleep(1)
            timeout -= 1
        else:
            if "video" in url:
                return response.content
            else:
                return response.text
    return None


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
# https://github.com/pytest-dev/pytest/issues/230#issuecomment-402580536
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != "passed":
        item.status = "failed"
    else:
        item.status = "passed"



@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    driver = request.config.getoption("--drivers")
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bv")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")

    options = None

    if browser == "chrome":
        options = ChromiumService()
        options.default_capabilities
    elif browser == "firefox":
        options = FFService()
    elif browser == 'Edge':
        options = EdgeService()
    else:
        options = SafariService()

    if not options:
        raise Exception("Не установлены настройки для запуска браузера")

    options._caps["selenoid:options"] = {
                            "enableVNC": vnc,
                            "name": request.node.name,
                            "screenResolution": "1920x1080",
                            "enableVideo": videos,
                            "enableLog": logs,
                            "timeZone": "Europe/Moscow",
                            "env": ["LANG=ru_RU.UTF-8", "LANGUAGE=ru:en", "LC_ALL=ru_RU.UTF-8"]
                        }

    driver = webdriver.Remote(
        command_executor=executor,
        options=options
    )

    driver.maximize_window()
    driver.get(url)

    def finalizer():
        video_url = f"http://172.29.39.81:8080/video/{driver.session_id}.mp4"

        if request.node.status == "failed":
            if videos:
                allure.attach(
                    body=wait_url_data(video_url),
                    name="video_for_" + driver.session_id,
                    attachment_type=allure.attachment_type.MP4,
                )

        if videos and wait_url_data(video_url):
            requests.delete(url=video_url)

        driver.quit()

    request.addfinalizer(finalizer)
    yield driver

    driver.close()