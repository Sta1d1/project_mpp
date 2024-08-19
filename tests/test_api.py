"""Тестирование API"""
import time
import allure
import requests
from selenium.webdriver import Remote
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Импорты методов и элементов
from src.pages.api import API as AP


@allure.feature("Авторизация API")
@allure.story('Авторизовация')
def test_login():
    url = "https://mpp-tst-mr1.star.lanit.ru/api/login"
    payload = 'username=admin&password=Topaz123%24'
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert response.ok == True

@allure.feature("Авторизация API")
@allure.story('Логаут')
def test_logout():
    url = "https://mpp-tst-mr1.star.lanit.ru/api/logout"
    headers = {
    'Authorization': f'Bearer {AP.login()}',
    'Cookie': 'refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTcyNDA5MjExNX0.EqmfBa4w6ewdqqwAIdlHQHbbfH35sHGWR9wk-vU5BKw'
    }
    print(headers)
    response = requests.get(url, headers=headers)
    assert response.ok == True

@allure.feature("Авторизация API")
@allure.story('Рефреш токен')
def test_refresh_token():
    url = "https://mpp-tst-mr1.star.lanit.ru/api/refresh"
    payload = {}
    headers = {
    'Authorization': f'Bearer {AP.login()}',
    'Cookie': 'refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTcyNDA5MjExNX0.EqmfBa4w6ewdqqwAIdlHQHbbfH35sHGWR9wk-vU5BKw'
    }
    response = requests.post(url, headers=headers, data=payload)
    assert response.ok == True

@allure.feature("Авторизация API")
@allure.story('Проверка эндпоинта')
def test_check_token_endpoint():
    test_token = AP.login()
    url = f"https://mpp-tst-mr1.star.lanit.ru/api/check-token?token={test_token}"
    payload = {}
    headers = {
    'Authorization': f'Bearer {test_token}',
    'Cookie': 'refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTcyNDA5MjExNX0.EqmfBa4w6ewdqqwAIdlHQHbbfH35sHGWR9wk-vU5BKw'
    }
    response = requests.get(url, headers=headers, data=payload).json()
    assert response['username'] == 'admin'

@allure.feature("Авторизация API")
@allure.story('Проверка профиля')
def test_profile():
    url = "https://mpp-tst-mr1.star.lanit.ru/api/profile"
    payload = {}
    headers = {
    'Authorization': f'Bearer {AP.login()}',
    'Cookie': 'refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTcyNDA5MjExNX0.EqmfBa4w6ewdqqwAIdlHQHbbfH35sHGWR9wk-vU5BKw'
    }
    response = requests.get(url, headers=headers, data=payload).json()
    assert response['userFullName'] == 'Администратор НШР'

@allure.feature("Versions")
@allure.story('Проверка версий')
def test_api_version():
    url = "https://mpp-tst-mr1.star.lanit.ru/api/versions"
    headers = {
    'Authorization': f'Bearer {AP.login()}',
    'Cookie': 'refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTcyNDA5MjExNX0.EqmfBa4w6ewdqqwAIdlHQHbbfH35sHGWR9wk-vU5BKw'
    }
    response = requests.get(url, headers=headers).json()
    assert response['API'] == '4.0.21'
    assert response['Backend'] == '4.0.20'

@allure.feature("Config")
@allure.story('Проверка конфига')
def test_config_groups():
    url = "https://mpp-tst-mr1.star.lanit.ru/api/modules"
    headers = {
    'Authorization': f'Bearer {AP.login()}',
    'Cookie': 'refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTcyNDA5MjExNX0.EqmfBa4w6ewdqqwAIdlHQHbbfH35sHGWR9wk-vU5BKw'
    }
    response = requests.get(url, headers=headers).json()
    assert response[0]['id'] == 0
    assert response[0]['name'] == 'tech'

@allure.feature("Supply Types")
@allure.story('Получение статусов поставок')
def test_get_operation_status():
    url = "https://mpp-tst-mr1.star.lanit.ru/api/operation-status"
    headers = {
    'Authorization': f'Bearer {AP.login()}',
    'Cookie': 'refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTcyNDA5MjExNX0.EqmfBa4w6ewdqqwAIdlHQHbbfH35sHGWR9wk-vU5BKw'
    }
    response = requests.get(url, headers=headers).json()
    assert response[0]['description'] == 'В обработке'
    assert response[1]['name'] == 'OPERATION_STATUS_OK'

@allure.feature("Supply Types")
@allure.story('Получение информации о поставке A01')
def test_get_supply_type():
    url = "https://mpp-tst-mr1.star.lanit.ru/api/supply-type/A01"
    headers = {
    'Authorization': f'Bearer {AP.login()}',
    'Cookie': 'refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTcyNDA5MjExNX0.EqmfBa4w6ewdqqwAIdlHQHbbfH35sHGWR9wk-vU5BKw'
    }
    response = requests.get(url, headers=headers).json()
    assert response['description'] == 'A01'
    assert response['shortDesc'] == 'Arifactory'

@allure.feature("Supply Types")
@allure.story('Получение информации о типах поставок')
def test_get_supply_types():
    url = "https://mpp-tst-mr1.star.lanit.ru/api/supply-types"
    headers = {
    'Authorization': f'Bearer {AP.login()}',
    'Cookie': 'refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTcyNDA5MjExNX0.EqmfBa4w6ewdqqwAIdlHQHbbfH35sHGWR9wk-vU5BKw'
    }
    response = requests.get(url, headers=headers).json()
    assert response[0]['description'] == 'A01'
    assert response[1]['description'] == 'A11'
    assert response[2]['description'] == 'A21'
    assert response[3]['description'] == 'Bundle'

@allure.feature("Developers")
@allure.story('Получение информации о разработчиках')
def test_get_developers():
    url = "https://mpp-tst-mr1.star.lanit.ru/api/developers"
    headers = {
    'Authorization': f'Bearer {AP.login()}',
    'Cookie': 'refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTcyNDA5MjExNX0.EqmfBa4w6ewdqqwAIdlHQHbbfH35sHGWR9wk-vU5BKw'
    }
    response = requests.get(url, headers=headers).json()
    assert response[0]['devName'] == 'Lanit'
    assert response[1]['devName'] == 'Admin'

@allure.feature("Dictionaries")
@allure.story('Получение информации о cтенде')
def test_get_dictionaries():
    url = "https://mpp-tst-mr1.star.lanit.ru/api/places"
    headers = {
    'Authorization': f'Bearer {AP.login()}',
    'Cookie': 'refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTcyNDA5MjExNX0.EqmfBa4w6ewdqqwAIdlHQHbbfH35sHGWR9wk-vU5BKw'
    }
    response = requests.get(url, headers=headers).json()
    assert response[0]['host'] == 'mpp-tst-mr1.star.lanit.ru'
    assert response[0]['name'] == 'Стенд МПП'

@allure.feature("Publications")
@allure.story('Получение информации о публикациях')
def test_get_publications():
    url = "https://mpp-tst-mr1.star.lanit.ru/api/publications"
    headers = {
    'Authorization': f'Bearer {AP.login()}',
    'Cookie': 'refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTcyNDA5MjExNX0.EqmfBa4w6ewdqqwAIdlHQHbbfH35sHGWR9wk-vU5BKw'
    }
    response = requests.get(url, headers=headers)
    assert response.ok == True

@allure.feature("Publications")
@allure.story('Получение информации о конкретной публикации')
def test_get_publication():
    test_id = 1695
    url = f"https://mpp-tst-mr1.star.lanit.ru/api/publications/{test_id}"
    headers = {
    'Authorization': f'Bearer {AP.login()}',
    'Cookie': 'refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTcyNDA5MjExNX0.EqmfBa4w6ewdqqwAIdlHQHbbfH35sHGWR9wk-vU5BKw'
    }
    response = requests.get(url, headers=headers).json()
    assert response['id'] == test_id
    assert response['supplyTypeName'] == 'B01'

@allure.feature("Replication")
@allure.story('Проверка невозможности получить список сервисов')
def test_get_services_list():
    url = "https://mpp-tst-mr1.star.lanit.ru/api/services-list"
    headers = {
    'Authorization': f'Bearer {AP.login()}',
    'Cookie': 'refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTcyNDA5MjExNX0.EqmfBa4w6ewdqqwAIdlHQHbbfH35sHGWR9wk-vU5BKw'
    }
    response = requests.get(url, headers=headers)
    assert response.ok == False

@allure.feature("Replication")
@allure.story('Проверка невозможности получить места')
def test_get_dr_places():
    url = "https://mpp-tst-mr1.star.lanit.ru/api/dr-places"
    headers = {
    'Authorization': f'Bearer {AP.login()}',
    'Cookie': 'refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTcyNDA5MjExNX0.EqmfBa4w6ewdqqwAIdlHQHbbfH35sHGWR9wk-vU5BKw'
    }
    response = requests.get(url, headers=headers)
    assert response.ok == False

@allure.feature("Replication")
@allure.story('Проверка невозможности получить информацию о сервисе')
def test_get_dr_services():
    url = "https://mpp-tst-mr1.star.lanit.ru/api/dr-services/1"
    headers = {
    'Authorization': f'Bearer {AP.login()}',
    'Cookie': 'refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTcyNDA5MjExNX0.EqmfBa4w6ewdqqwAIdlHQHbbfH35sHGWR9wk-vU5BKw'
    }
    response = requests.get(url, headers=headers)
    assert response.ok == False

@allure.feature("Roles")
@allure.story('Проверка возожности получить ldap группы')
def test_get_ldap_groups():
    url = "https://mpp-tst-mr1.star.lanit.ru/api/ldap-groups"
    headers = {
    'Authorization': f'Bearer {AP.login()}',
    'Cookie': 'refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTcyNDA5MjExNX0.EqmfBa4w6ewdqqwAIdlHQHbbfH35sHGWR9wk-vU5BKw'
    }
    response = requests.get(url, headers=headers)
    assert response.ok == True

@allure.feature("Roles")
@allure.story('Проверка возожности получить ldap роли')
def test_get_ldap_roles():
    url = "https://mpp-tst-mr1.star.lanit.ru/api/roles"
    headers = {
    'Authorization': f'Bearer {AP.login()}',
    'Cookie': 'refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTcyNDA5MjExNX0.EqmfBa4w6ewdqqwAIdlHQHbbfH35sHGWR9wk-vU5BKw'
    }
    response = requests.get(url, headers=headers)
    assert response.ok == True

@allure.feature("Role Permission")
@allure.story('Проверка доступа к пермишенам ролей')
def test_get_role_permission():
    url = "https://mpp-tst-mr1.star.lanit.ru/api/role-permissions"
    headers = {
    'Authorization': f'Bearer {AP.login()}',
    'Cookie': 'refresh_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTcyNDA5MjExNX0.EqmfBa4w6ewdqqwAIdlHQHbbfH35sHGWR9wk-vU5BKw'
    }
    response = requests.get(url, headers=headers)
    assert response.ok == True