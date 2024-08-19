"""Базовые методы"""
import time
import html
from selenium.webdriver.common.by import By
from selenium.webdriver import Remote
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




class  BaseMethods():
    # selector_allert = '//*[@id="app"]/div/main/div[2]/div'                                                                          # Селектор всплывающего аллерта

    def __init__(self, browser) -> None:
        self.browser = browser

    def click_on_the_element(self, selector, wait_time=3):
        """Проверяет что элемент кликабельный, прокручиват и нажимает на него"""
        WebDriverWait(self.browser, wait_time).until(EC.element_to_be_clickable((By.XPATH, selector)))
        elem = self.browser.find_element(By.XPATH, selector) #Записываем элемент в переменную
        self.browser.execute_script("arguments[0].scrollIntoView(true);", elem) # Прокручиваем к элементу
        WebDriverWait(self.browser, wait_time).until(EC.element_to_be_clickable((By.XPATH, selector))).click()
        return self.browser
    
    def click_on_the_element_no_roll(self, selector, wait_time=3):
        """Проверяет что элемент кликабельный, НЕ прокручиват и нажимает на него"""
        WebDriverWait(self.browser, wait_time).until(EC.element_to_be_clickable((By.XPATH, selector))).click()
        return self.browser

    def page_reload(self):
        """Перезагрузка страницы"""
        self.browser.refresh()

    def go_to_the_page(self, link):
        """Переход по ссылке"""
        self.browser.get(link)
        return self.browser

    def enter_text_in_the_element(self, selector, input_text):
        """Ввести текст в элемент стерев предыдущий"""
        el = self.browser.find_element(By.XPATH, selector)
        # self.browser.execute_script("arguments[0].scrollIntoView(true);" +  "window.scrollBy(0, 100);", el) # Прокручиваем к элементу
        el.send_keys(Keys.CONTROL, 'a')
        el.send_keys(Keys.BACKSPACE)
        el.send_keys(input_text)

    def getting_a_text_element(self, selector, wait_time=3):
        """Возвращает текст элемента по селектору XPATH"""
        return html.unescape(WebDriverWait(self.browser, wait_time).until(EC.presence_of_element_located((By.XPATH, selector))).get_attribute('textContent'))
    
    def getting_a_value_element(self, selector, wait_time=3):
        """Возвращает value элемента по xpath"""
        return html.unescape(WebDriverWait(self.browser, wait_time).until(EC.presence_of_element_located((By.XPATH, selector))).get_attribute('value'))

    def checking_whether_an_element_is_within_the_boundaries(self, first_amount: int, second_amount: int, amount: int):
        """Проверка нахождения значения amount в границах first_amount и second_amount"""
        if int(first_amount) <= int(amount) and int(amount) <= int(second_amount):
            return self.browser
        else:
            raise ValueError(f'Значения не находится в границах: {first_amount} <= {amount} <= {second_amount}')

    def comparing_custom_values(self, first_value, second_value):
        """Сравнивает что значения равны"""
        if first_value == second_value:
            return self.browser
        else:
            raise ValueError(f'Значения не равны: {first_value} != {second_value}')
    
    def get_element_text_and_compare_with_custom_value(self, selector, second_value, wait_time=3, atribut='textContent'):
        """Получить текст элемента и сравнить с пользовательским знчением"""
        first_value = html.unescape(WebDriverWait(self.browser, wait_time).until(EC.presence_of_element_located((By.XPATH, selector))).get_attribute(atribut))
        if first_value == second_value:
            return self.browser
        else:
            raise ValueError(f'Значения не равны: {first_value} != {second_value}')
        
        
    def checking_the_presence_of_an_element_on_the_page(self, selector, wait_time=5):
        """Проверка присутствия элемента на странице"""
        if WebDriverWait(self.browser, wait_time).until(EC.presence_of_element_located((By.XPATH, selector))) != None:
            return self.browser

    