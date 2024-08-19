"""Страница Настроек"""
# Библиотеки
import time
from selenium.webdriver import Remote
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

# Импорты методов и элементов
from src.methods.base_methods import BaseMethods as BM

# -------------------------------------------- Система ----------------------------------------------------
class system_settings:
    # ЭЛЕМЕНТЫ
    settings_page_link = 'https://mpp-tst-mr1.star.lanit.ru/configuration/'                                                         # Страница Настроек
    seetings_button_page_link = '//*[@id="configuration-header-button"]'                                                            # Кнопка "Настройки" в хэдере
    system_menu_item = '//*[@id="system-menu-item"]'                                                                                # Кнопка "Система"
        # Блок путей на странице "Технические настройки"
    system_technical_item = '//*[@id="tech-menu-item"]'                                                                             # Кнопка "Технические настройки"
    configuration_control_intermediate_path = '//*[@id="configuration-control-intermediate_path"]'                                  # "Технические настройки" --> Промежуточное хранилище
    configuration_control_log_level = '//*[@id="configuration-control-log.level"]'                                                  # "Технические настройки" --> Уровень логгирования
        # Блок путей на странице "Получение поставок"
    system_receiver_menu_item = '//*[@id="receiver-menu-item"]'                                                                     # Кнопка "Получение поставок"
    receiving_supplies_configuration_control_regexp_subject_mail_check = '//*[@id="configuration-control-regexp_subject_mail_check"]'                  # "Получение поставок" --> "Фильтр темы письма"
    receiving_supplies_configuration_control_departure_lifetime = '//*[@id="configuration-control-departure_lifetime"]'                                # "Получение поставок" --> "Время жизни отправления (мин)"
    receiving_supplies_configuration_control_regexp_determine_supply_subject = '//*[@id="configuration-control-regexp_determine_supply_subject"]'      # "Получение поставок" --> "Фильтр темы поставки из темы письма"
    receiving_supplies_configuration_control_mq_queue_name = '//*[@id="configuration-control-mq.queue.name"]'                                          # "Получение поставок" --> "Очередь модуля Получение поставок"
    receiving_supplies_configuration_control_mail_input_host = '//*[@id="configuration-control-mail.input.host"]'                                      # "Получение поставок" --> "Адрес почтового сервера"
    receiving_supplies_configuration_control_mail_input_port = '//*[@id="configuration-control-mail.input.port"]'                                      # "Получение поставок" --> "Порт почтового сервера"
    receiving_supplies_configuration_control_mail_input_user = '//*[@id="configuration-control-mail.input.user"]'                                      # "Получение поставок" --> "Имя пользователя почтового сервера"
    receiving_supplies_configuration_control_mail_input_proto = '//*[@id="configuration-control-mail.input.proto"]'                                    # "Получение поставок" --> "Протокол почтового сервера"
    receiving_supplies_configuration_control_log_level_receiver_menu = '//*[@id="configuration-control-log.level"]'                                    # "Получение поставок" --> "Уровень логирования"
    receiving_supplies_configuration_control_mail_input_read_timer = '//*[@id="configuration-control-mail.input.read_timer"]'                          # "Получение поставок" --> "Таймер чтения"
    receiving_supplies_configuration_control_regexp_determine_supply_developer = '//*[@id="configuration-control-regexp_determine_supply_developer"]'  # "Получение поставок" --> "Фильтр разработчика"
    receiving_supplies_configuration_control_regexp_determine_supply_snapshot = '//*[@id="configuration-control-regexp_determine_supply_snapshot"]'    # "Получение поставок" --> "Фильтр снапшота"
    receiving_supplies_configuration_control_regexp_determine_supply_release = '//*[@id="configuration-control-regexp_determine_supply_release"]'      # "Получение поставок" --> "Фильтр релиза"
        # Блок путей на странице "Криптографическая обработка данных"
    system_cryptographic_data_processing = '//*[@id="decryption-menu-item"]'                                                        # Кнопка "Криптографическая обработка данных"
    crypto_configuration_control_mq_queue_name = '//*[@id="configuration-control-mq.queue.name"]'                                   # "Криптографическая обработка данных" --> "Очередь модуля Криптографической обработки данных"
    crypto_configuration_control_decryption_ip = '//*[@id="configuration-control-decryption.ip"]'                                   # "Криптографическая обработка данных" --> "Сетевое имя (или IP адрес) сервера Янтарь"
    crypto_configuration_control_decryption_port = '//*[@id="configuration-control-decryption.port"]'                               # "Криптографическая обработка данных" --> "Порт Янтарь"
    crypto_configuration_control_decryption_cert_my = '//*[@id="configuration-control-decryption.cert.my"]'                         # "Криптографическая обработка данных" --> "Имя сессии Янтарь"
    crypto_configuration_control_log_level = '//*[@id="configuration-control-log.level"]'                                           # "Криптографическая обработка данных" --> "Уровень логирования"
        # Блок путей на странице "Распаковки поставок"
    unzip_menu_item = '//*[@id="unzip-menu-item"]'                                                                                  # Кнопка "Распаковки поставок"
    unzip_configuration_control_mq_queue_name = '//*[@id="configuration-control-mq.queue.name"]'                                    # "Распаковки поставок" --> "Очередь модуля Распаковки поставок"
    unzip_configuration_control_log_level = '//*[@id="configuration-control-log.level"]'                                            # "Распаковки поставок" --> "Уровень логирования"
        # Блок путей на странице "валидация поставок"
    validator_menu_item = '//*[@id="validator-menu-item"]'                                                                          # Кнопка "Валидация файлов"
    validator_configuration_control_mq_queue_name = '//*[@id="configuration-control-mq.queue.name"]'                                # "Валидация файлов" --> "Очередь модуля Валидации данных"
    validator_configuration_control_log_level = '//*[@id="configuration-control-log.level"]'                                        # "Валидация файлов" --> "Уровень логирования"
        # Блок путей на странице "Антивирусная проверка"
    antivir_menu_item = '//*[@id="antivir-menu-item"]'                                                                              # Кнопка "Антивирусная проверка"
    antivir_configuration_control_antivir_regexp = '//*[@id="configuration-control-antivir.regexp"]'                                # "Антивирусная проверка" --> "Фильтр результата работы Антивируса"
    antivir_configuration_control_antivir_command_check = '//*[@id="configuration-control-antivir.command.check"]'                  # "Антивирусная проверка" --> "Команда проверки наличия антивируса"
    antivir_configuration_control_antivir_command_scan = '//*[@id="configuration-control-antivir.command.scan"]'                    # "Антивирусная проверка" --> "Команда сканирования антивирусом"
    antivir_configuration_control_mq_queue_name = '//*[@id="configuration-control-mq.queue.name"]'                                  # "Антивирусная проверка" --> "Очередь модуля Антивирусной проверки"
    antivir_configuration_control_log_level = '//*[@id="configuration-control-log.level"]'                                          # "Антивирусная проверка" --> "Уровень логирования"
        # Блок путей на странице "Расчет контрольных сумм"
    checksum_menu_item = '//*[@id="checkSum-menu-item"]'                                                                            # Кнопка "Антивирусная проверка"
    checksum_configuration_control_mq_queue_name = '//*[@id="configuration-control-mq.queue.name"]'                                 # "Расчет контрольных сумм" --> "Очередь модуля Расчета контрольных сумм"
    checksum_configuration_control_log_level = '//*[@id="configuration-control-log.level"]'                                         # "Расчет контрольных сумм" --> "Уровень логирования"
        # Блок путей на странице "Публикация данных"
    publisher_menu_item = '//*[@id="publisher-menu-item"]'                                                                          # Кнопка "Публикация данных"
    publisher_configuration_control_mq_queue_name = '//*[@id="configuration-control-mq.queue.name"]'                                # "Публикация данных" --> "Очередь модуля Публикации данных"
    publisher_configuration_control_log_level = '//*[@id="configuration-control-log.level"]'                                        # "Публикация данных" --> "Уровень логирования"
        # Блок путей на странице "Очистка каталога поставок"
    cleaner_menu_item = '//*[@id="cleaner-menu-item"]'                                                                              # Кнопка "Очистка каталога поставок"
    cleaner_configuration_control_mq_queue_name = '//*[@id="configuration-control-mq.queue.name"]'                                  # "Очистка каталога поставок" --> "Очередь модуля Очистки каталога поставок"
    cleaner_configuration_control_log_level = '//*[@id="configuration-control-log.level"]'                                          # "Очистка каталога поставок" --> "Уровень логирования"
    cleaner_configuration_control_supply_storage_time = '//*[@id="configuration-control-supply_storage_time"]'                      # "Очистка каталога поставок" --> "Время хранения поставок"
    cleaner_configuration_control_period_of_check = '//*[@id="configuration-control-period_of_check"]'                              # "Очистка каталога поставок" --> "Период запуска очистки"
        # Блок путей на странице "API"
    api_menu_item = '//*[@id="api-menu-item"]'                                                                                      # Кнопка "API"
    api_configuration_control_mq_queue_name = '//*[@id="configuration-control-mq.queue.name"]'                                      # "API" --> "Очередь модуля API веб-интерфейса"
    api_configuration_control_log_level = '//*[@id="configuration-control-log.level"]'                                              # "API" --> "Уровень логирования"
    api_configuration_control_ldap_user_dn = '//*[@id="configuration-control-ldap.user.dn"]'                                        # "API" --> "Верхняя запись LDAP для поиска пользователей"
    api_configuration_control_ldap_group_dn= '//*[@id="configuration-control-ldap.group.dn"]'                                       # "API" --> "Верхняя запись LDAP для поиска групп"
    api_configuration_control_ldap_group_roles_filter = '//*[@id="configuration-control-ldap.group.roles_filter"]'                  # "API" --> "Фильтр поиска LDAP групп для ролей МПП"
    api_configuration_control_ldap_user_search_scope = '//*[@id="configuration-control-ldap.user.search_scope"]'                    # "API" --> "Глубина поиска записей в LDAP"
    api_configuration_control_ldap_host = '//*[@id="configuration-control-ldap.host"]'                                              # "API" --> "Сервер LDAP"
    api_configuration_control_ldap_bind_user = '//*[@id="configuration-control-ldap.bind_user"]'                                    # "API" --> "Системный пользователь LDAP"                      
    api_configuration_control_ldap_user_attribute = '//*[@id="configuration-control-ldap.user.attribute"]'                          # "API" --> "Свойство записи LDAP для поиска логина пользователя"
    api_configuration_control_ldap_port = '//*[@id="configuration-control-ldap.port"]'                                              # "API" --> "Порт сервера LDAP"
        # Блок путей на странице "Уведомления"
    notification_menu_item = '//*[@id="notification-menu-item"]'                                                                    # Кнопка "Уведомления"
    notification_configuration_control_mq_queue_name = '//*[@id="configuration-control-mq.queue.name"]'                             # "Уведомления" --> "Очередь модуля"
    notification_configuration_control_log_level = '//*[@id="configuration-control-log.level"]'                                     # "Уведомления" --> "Уровень логирования"
    notification_configuration_control_mail_output_fromaddress = '//*[@id="configuration-control-mail.output.fromaddress"]'         # "Уведомления" --> "Адрес, от кого отправляется письмо"
    notification_configuration_control_mail_output_host = '//*[@id="configuration-control-mail.output.host"]'                       # "Уведомления" --> "Хост почтового сервера для отправки писем"
    notification_configuration_control_mail_output_port = '//*[@id="configuration-control-mail.output.port"]'                       # "Уведомления" --> "Порт почтового сервера для отправки писем"
    notification_configuration_control_mail_output_user = '//*[@id="configuration-control-mail.output.user"]'                       # "Уведомления" --> "Имя пользователя аккаунта исходящей почты"
    notification_configuration_control_mail_output_strategy = '//*[@id="configuration-control-mail.output.strategy"]'               # "Уведомления" --> "Стратегия для отправки писем"
        # Блок путей на странице "Брокер сообщений ActiveMQ"
    activemq_menu_item = '//*[@id="activemq-menu-item"]'                                                                            # Кнопка "Брокер сообщений ActiveMQ"
    activemq_configuration_control_mq_broker_host = '//*[@id="configuration-control-mq.broker.host"]'                               # "Брокер сообщений ActiveMQ" --> "Адрес хоста брокера сообщений"
    activemq_configuration_control_mq_broker_port = '//*[@id="configuration-control-mq.broker.port"]'                               # "Брокер сообщений ActiveMQ" --> "Порт хоста брокера сообщений"
    activemq_configuration_control_mq_broker_user = '//*[@id="configuration-control-mq.broker.user"]'                               # "Брокер сообщений ActiveMQ" --> "Имя пользователя брокера сообщений"

    system_configuration_save_button = '//*[@id="configuration-save-button"]'                                                       # Кнопка "Сохранения настроек"
    allert_save_text_xpath = '/html/body/div/div[1]/div/div'                                                                        # Поле всплывающего аллерта о сохранении настроек


    # ЗНАЧЕНИЯ
    allert_save_text = 'Настройки успешно сохранены'                                                                                # Всплывающий аллерт о сохранении настроек


    def __init__(self, browser) -> None:
        self.browser = browser

    def go_to_settings_page(self):
        """Переход на страницу настроек"""
        BM(browser=self.browser).click_on_the_element(selector=self.seetings_button_page_link)
        BM(browser=self.browser).getting_a_text_element(selector=self.system_menu_item)
    
    def editing_technical_settings(self):
        """Редактирование настроек Система --> Технический"""
        BM(browser=self.browser).click_on_the_element(selector=self.system_menu_item) # Раскрытие "Система"
        BM(browser=self.browser).click_on_the_element(selector=self.system_technical_item) # Переход к Техническим настройкам
        # Редактирование настроек
        BM(browser=self.browser).enter_text_in_the_element(selector=self.configuration_control_intermediate_path, input_text='test/opt/mpp/files') # Редактирование настройки "Промежуточное хранилище"
        BM(browser=self.browser).click_on_the_element(selector=self.system_configuration_save_button) # Сохраняю измененные настройки
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value=self.allert_save_text) # Проверяю аллерт
        # Обновляю страницу и проверяю измененные элементы
        BM(browser=self.browser).page_reload() # Обновляю страницу
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.configuration_control_intermediate_path, second_value='test/opt/mpp/files', atribut='value')
        # Возвращаю стандартные настройки
        BM(browser=self.browser).enter_text_in_the_element(selector=self.configuration_control_intermediate_path, input_text='/opt/mpp/files') # Редактирование настройки "Промежуточное хранилище"
        BM(browser=self.browser).click_on_the_element(selector=self.system_configuration_save_button) # Сохраняю измененные настройки
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value=self.allert_save_text) # Проверяю аллерт
    
    def editing_receiving_supplies(self):
        """Редактирование настроек Система --> Получение поставок"""
        BM(browser=self.browser).click_on_the_element(selector=self.system_menu_item) # Раскрытие "Система"
        BM(browser=self.browser).click_on_the_element(selector=self.system_receiver_menu_item) # Переход к Техническим настройкам
        # Редактирование настроек
        BM(browser=self.browser).enter_text_in_the_element(selector=self.receiving_supplies_configuration_control_regexp_subject_mail_check, input_text='test^\w\d\d_[A-Za-z0-9-.]+(_\w+)?_[^_]+_(?<part>\d+)_(?<total>\d+)$') # Редактирование настройки "Фильтр темы письма"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.receiving_supplies_configuration_control_departure_lifetime, input_text='123') # Редактирование настройки "Время жизни отправления (мин)"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.receiving_supplies_configuration_control_regexp_determine_supply_subject, input_text='test(?<supply>.*)_\d+_\d+') # Редактирование настройки "Фильтр темы поставки из темы письма"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.receiving_supplies_configuration_control_mq_queue_name, input_text='testreceiver') # Редактирование настройки "Очередь модуля Получение поставок"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.receiving_supplies_configuration_control_mail_input_host, input_text='testmail.star.lanit.ru') # Редактирование настройки "Адрес почтового сервера"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.receiving_supplies_configuration_control_mail_input_port, input_text='123') # Редактирование настройки "Порт почтового сервера"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.receiving_supplies_configuration_control_mail_input_user, input_text='testinbox_mpp@star.lanit.ru') # Редактирование настройки "Имя пользователя почтового сервера"
        BM(browser=self.browser).click_on_the_element_no_roll(selector=self.receiving_supplies_configuration_control_mail_input_proto) # Раскрытие настройки "Протокол почтового сервера"
        BM(browser=self.browser).click_on_the_element_no_roll(selector='//*[@id="configuration-control-mail.input.proto-option-0"]') # Выбор протокола imap
        BM(browser=self.browser).enter_text_in_the_element(selector=self.receiving_supplies_configuration_control_mail_input_read_timer, input_text='123') # Редактирование настройки "Таймер чтения"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.receiving_supplies_configuration_control_regexp_determine_supply_developer, input_text='test^[^_]*_(?<developer>[^_^\-]*).*_.*$') # Редактирование настройки "Фильтр разработчика"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.receiving_supplies_configuration_control_regexp_determine_supply_snapshot, input_text='test[^_]+_[^_]+_(?<snapshot>.*)$') # Редактирование настройки "Фильтр снапшота"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.receiving_supplies_configuration_control_regexp_determine_supply_release, input_text='test[^_]+_[^_]+_[^-]+-(?<release>.*)$') # Редактирование настройки "Фильтр релиза"
        BM(browser=self.browser).click_on_the_element(selector=self.system_configuration_save_button) # Сохраняю измененные настройки
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value=self.allert_save_text) # Проверяю аллерт
        # Обновляю страницу и проверяю измененные элементы
        BM(browser=self.browser).page_reload() # Обновляю страницу
        BM(browser=self.browser).checking_the_presence_of_an_element_on_the_page(selector=self.system_menu_item)
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.receiving_supplies_configuration_control_regexp_subject_mail_check, second_value='test^\w\d\d_[A-Za-z0-9-.]+(_\w+)?_[^_]+_(?<part>\d+)_(?<total>\d+)$', atribut='value') # Проверяю "Фильтр темы письма"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.receiving_supplies_configuration_control_departure_lifetime, second_value='123', atribut='value') # Проверяю "Время жизни отправления (мин)"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.receiving_supplies_configuration_control_regexp_determine_supply_subject, second_value='test(?<supply>.*)_\d+_\d+', atribut='value') # Проверяю "Фильтр темы поставки из темы письма"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.receiving_supplies_configuration_control_mq_queue_name, second_value='testreceiver', atribut='value')# Проверяю "Очередь модуля Получение поставок"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.receiving_supplies_configuration_control_mail_input_host, second_value='testmail.star.lanit.ru', atribut='value')# Проверяю "Адрес почтового сервера"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.receiving_supplies_configuration_control_mail_input_port, second_value='123', atribut='value')# Проверяю "Порт почтового сервера"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.receiving_supplies_configuration_control_mail_input_user, second_value='testinbox_mpp@star.lanit.ru', atribut='value')# Проверяю "Имя пользователя почтового сервера"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.receiving_supplies_configuration_control_mail_input_proto, second_value='imap', atribut='value')# Проверяю "Протокол почтового сервера"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.receiving_supplies_configuration_control_mail_input_read_timer, second_value='123', atribut='value')# Проверяю "Таймер чтения"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.receiving_supplies_configuration_control_regexp_determine_supply_developer, second_value='test^[^_]*_(?<developer>[^_^\-]*).*_.*$', atribut='value')# Проверяю "Фильтр разработчика"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.receiving_supplies_configuration_control_regexp_determine_supply_snapshot, second_value='test[^_]+_[^_]+_(?<snapshot>.*)$', atribut='value')# Проверяю "Фильтр снапшота"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.receiving_supplies_configuration_control_regexp_determine_supply_release, second_value='test[^_]+_[^_]+_[^-]+-(?<release>.*)$', atribut='value')# Проверяю "Фильтр релиза"
        # Возвращаю стандартные настройки
        BM(browser=self.browser).enter_text_in_the_element(selector=self.receiving_supplies_configuration_control_regexp_subject_mail_check, input_text='^\w\d\d_[A-Za-z0-9-.]+(_\w+)?_[^_]+_(?<part>\d+)_(?<total>\d+)$') # Редактирование настройки "Фильтр темы письма"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.receiving_supplies_configuration_control_departure_lifetime, input_text='30') # Редактирование настройки "Время жизни отправления (мин)"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.receiving_supplies_configuration_control_regexp_determine_supply_subject, input_text='(?<supply>.*)_\d+_\d+') # Редактирование настройки "Фильтр темы поставки из темы письма"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.receiving_supplies_configuration_control_mq_queue_name, input_text='receiver') # Редактирование настройки "Очередь модуля Получение поставок"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.receiving_supplies_configuration_control_mail_input_host, input_text='mail.star.lanit.ru') # Редактирование настройки "Адрес почтового сервера"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.receiving_supplies_configuration_control_mail_input_port, input_text='110') # Редактирование настройки "Порт почтового сервера"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.receiving_supplies_configuration_control_mail_input_user, input_text='inbox_mpp@star.lanit.ru') # Редактирование настройки "Имя пользователя почтового сервера"
        BM(browser=self.browser).click_on_the_element_no_roll(selector=self.receiving_supplies_configuration_control_mail_input_proto) # Раскрытие настройки "Протокол почтового сервера"
        BM(browser=self.browser).click_on_the_element_no_roll(selector='//*[@id="configuration-control-mail.input.proto-option-1"]') # Выбор протокола pop3
        BM(browser=self.browser).enter_text_in_the_element(selector=self.receiving_supplies_configuration_control_mail_input_read_timer, input_text='60') # Редактирование настройки "Таймер чтения"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.receiving_supplies_configuration_control_regexp_determine_supply_developer, input_text='^[^_]*_(?<developer>[^_^\-]*).*_.*$') # Редактирование настройки "Фильтр разработчика"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.receiving_supplies_configuration_control_regexp_determine_supply_snapshot, input_text='[^_]+_[^_]+_(?<snapshot>.*)$') # Редактирование настройки "Фильтр снапшота"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.receiving_supplies_configuration_control_regexp_determine_supply_release, input_text='[^_]+_[^_]+_[^-]+-(?<release>.*)$') # Редактирование настройки "Фильтр релиза"
        BM(browser=self.browser).click_on_the_element(selector=self.system_configuration_save_button) # Сохраняю измененные настройки
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value=self.allert_save_text) # Проверяю аллерт

    def cryptographic_data_processing(self):
        """Редактирование настроек Система --> Криптографическая обработка данных"""
        BM(browser=self.browser).click_on_the_element(selector=self.system_menu_item) # Раскрытие "Система"
        BM(browser=self.browser).click_on_the_element(selector=self.system_cryptographic_data_processing) # Переход к Криптографическая обработка данных
        # Редактирование настроек
        BM(browser=self.browser).enter_text_in_the_element(selector=self.crypto_configuration_control_mq_queue_name, input_text='testcrypto') # Редактирование настройки "Очередь модуля Криптографической обработки данных"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.crypto_configuration_control_decryption_ip, input_text='0.0.0.0') # Редактирование настройки "Сетевое имя (или IP адрес) сервера Янтарь"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.crypto_configuration_control_decryption_port, input_text='111') # Редактирование настройки "Порт Янтарь"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.crypto_configuration_control_decryption_cert_my, input_text='testuser228') # Редактирование настройки "Имя сессии Янтарь"
        BM(browser=self.browser).click_on_the_element(selector=self.system_configuration_save_button) # Сохраняю измененные настройки
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value=self.allert_save_text) # Проверяю аллерт
        # Обновляю страницу и проверяю измененные элементы
        BM(browser=self.browser).page_reload() # Обновляю страницу
        BM(browser=self.browser).checking_the_presence_of_an_element_on_the_page(selector=self.system_menu_item)
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.crypto_configuration_control_mq_queue_name, second_value='testcrypto', atribut='value') # Проверяю "Очередь модуля Криптографической обработки данных"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.crypto_configuration_control_decryption_ip, second_value='0.0.0.0', atribut='value') # Проверяю "Сетевое имя (или IP адрес) сервера Янтарь"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.crypto_configuration_control_decryption_port, second_value='111', atribut='value') # Проверяю "Порт Янтарь"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.crypto_configuration_control_decryption_cert_my, second_value='testuser228', atribut='value') # Проверяю "Имя сессии Янтарь"
        # Возвращаю стандартные настройки
        BM(browser=self.browser).enter_text_in_the_element(selector=self.crypto_configuration_control_mq_queue_name, input_text='crypto') # Редактирование настройки "Очередь модуля Криптографической обработки данных"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.crypto_configuration_control_decryption_ip, input_text='172.29.39.42') # Редактирование настройки "Сетевое имя (или IP адрес) сервера Янтарь"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.crypto_configuration_control_decryption_port, input_text='1333') # Редактирование настройки "Порт Янтарь"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.crypto_configuration_control_decryption_cert_my, input_text='user001') # Редактирование настройки "Имя сессии Янтарь"
        BM(browser=self.browser).click_on_the_element(selector=self.system_configuration_save_button) # Сохраняю измененные настройки
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value=self.allert_save_text) # Проверяю аллерт

    def unpacking_supplies(self):
        """Редактирование настроек Система --> Распаковки поставок"""
        BM(browser=self.browser).click_on_the_element(selector=self.system_menu_item) # Раскрытие "Система"
        BM(browser=self.browser).click_on_the_element(selector=self.unzip_menu_item) # Переход к Распаковки поставок
        # Редактирование настроек
        BM(browser=self.browser).enter_text_in_the_element(selector=self.unzip_configuration_control_mq_queue_name, input_text='testunzip') # Редактирование настройки "Очередь модуля Распаковки поставок"
        BM(browser=self.browser).click_on_the_element(selector=self.system_configuration_save_button) # Сохраняю измененные настройки
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value=self.allert_save_text) # Проверяю аллерт
        # Обновляю страницу и проверяю измененные элементы
        BM(browser=self.browser).page_reload() # Обновляю страницу
        BM(browser=self.browser).checking_the_presence_of_an_element_on_the_page(selector=self.system_menu_item)
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.unzip_configuration_control_mq_queue_name, second_value='testunzip', atribut='value') # Проверяю "Очередь модуля Распаковки поставок"
        # Возвращаю стандартные настройки
        BM(browser=self.browser).enter_text_in_the_element(selector=self.unzip_configuration_control_mq_queue_name, input_text='unzip') # Редактирование настройки "Очередь модуля Распаковки поставок"
        BM(browser=self.browser).click_on_the_element(selector=self.system_configuration_save_button) # Сохраняю измененные настройки
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value=self.allert_save_text) # Проверяю аллерт
    
    def validation_of_deliveries(self):
        """Редактирование настроек Система --> Валидация поставок"""
        BM(browser=self.browser).click_on_the_element(selector=self.system_menu_item) # Раскрытие "Система"
        BM(browser=self.browser).click_on_the_element(selector=self.validator_menu_item) # Переход к Валидация поставок
        # Редактирование настроек
        BM(browser=self.browser).enter_text_in_the_element(selector=self.validator_configuration_control_mq_queue_name, input_text='testvalidation') # Редактирование настройки "Очередь модуля Валидации данных"
        BM(browser=self.browser).click_on_the_element(selector=self.system_configuration_save_button) # Сохраняю измененные настройки
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value=self.allert_save_text) # Проверяю аллерт
        # Обновляю страницу и проверяю измененные элементы
        BM(browser=self.browser).page_reload() # Обновляю страницу
        BM(browser=self.browser).checking_the_presence_of_an_element_on_the_page(selector=self.system_menu_item)
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.validator_configuration_control_mq_queue_name, second_value='testvalidation', atribut='value') # Проверяю "Очередь модуля Валидации данных"
        # Возвращаю стандартные настройки
        BM(browser=self.browser).enter_text_in_the_element(selector=self.validator_configuration_control_mq_queue_name, input_text='validation') # Редактирование настройки "Очередь модуля Валидации данных"
        BM(browser=self.browser).click_on_the_element(selector=self.system_configuration_save_button) # Сохраняю измененные настройки
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value=self.allert_save_text) # Проверяю аллерт

    def аntivirus_check(self):
        """Редактирование настроек Система --> Антивирусная проверка"""
        BM(browser=self.browser).click_on_the_element(selector=self.system_menu_item) # Раскрытие "Система"
        BM(browser=self.browser).click_on_the_element(selector=self.antivir_menu_item) # Переход к Антивирусная проверка
        # Редактирование настроек
        BM(browser=self.browser).enter_text_in_the_element(selector=self.antivir_configuration_control_antivir_regexp, input_text='TestTotal.detected.(objects|)[\s]+:[\s]+(?<count>[0-9]+)') # Редактирование настройки "Фильтр результата работы Антивируса"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.antivir_configuration_control_antivir_command_check, input_text='testkesl-control') # Редактирование настройки "Команда проверки наличия антивируса"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.antivir_configuration_control_antivir_command_scan, input_text='testkesl-control --scan-file') # Редактирование настройки "Команда сканирования антивирусом"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.antivir_configuration_control_mq_queue_name, input_text='testantivir') # Редактирование настройки "Очередь модуля Антивирусной проверки"
        BM(browser=self.browser).click_on_the_element(selector=self.system_configuration_save_button) # Сохраняю измененные настройки
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value=self.allert_save_text) # Проверяю аллерт
        # Обновляю страницу и проверяю измененные элементы
        BM(browser=self.browser).page_reload() # Обновляю страницу
        BM(browser=self.browser).checking_the_presence_of_an_element_on_the_page(selector=self.system_menu_item)
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.antivir_configuration_control_antivir_regexp, second_value='TestTotal.detected.(objects|)[\s]+:[\s]+(?<count>[0-9]+)', atribut='value') # Проверяю "Фильтр результата работы Антивируса"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.antivir_configuration_control_antivir_command_check, second_value='testkesl-control', atribut='value') # Проверяю "Команда проверки наличия антивируса"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.antivir_configuration_control_antivir_command_scan, second_value='testkesl-control --scan-file', atribut='value') # Проверяю "Команда сканирования антивирусом"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.antivir_configuration_control_mq_queue_name, second_value='testantivir', atribut='value') # Проверяю "Очередь модуля Антивирусной проверки"
        # Возвращаю стандартные настройки
        BM(browser=self.browser).enter_text_in_the_element(selector=self.antivir_configuration_control_antivir_regexp, input_text='Total.detected.(objects|)[\s]+:[\s]+(?<count>[0-9]+)') # Редактирование настройки "Фильтр результата работы Антивируса"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.antivir_configuration_control_antivir_command_check, input_text='kesl-control') # Редактирование настройки "Команда проверки наличия антивируса"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.antivir_configuration_control_antivir_command_scan, input_text='kesl-control --scan-file') # Редактирование настройки "Команда сканирования антивирусом"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.antivir_configuration_control_mq_queue_name, input_text='antivir') # Редактирование настройки "Очередь модуля Антивирусной проверки"
        BM(browser=self.browser).click_on_the_element(selector=self.system_configuration_save_button) # Сохраняю измененные настройки
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value=self.allert_save_text) # Проверяю аллерт

    def calculation_of_checksums(self):
        """Редактирование настроек Система --> Расчет контрольных сумм"""
        BM(browser=self.browser).click_on_the_element(selector=self.system_menu_item) # Раскрытие "Система"
        BM(browser=self.browser).click_on_the_element(selector=self.checksum_menu_item) # Переход к Расчет контрольных сумм
        # Редактирование настроек
        BM(browser=self.browser).enter_text_in_the_element(selector=self.checksum_configuration_control_mq_queue_name, input_text='testchecksum') # Редактирование настройки "Очередь модуля Расчета контрольных сумм"
        BM(browser=self.browser).click_on_the_element(selector=self.system_configuration_save_button) # Сохраняю измененные настройки
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value=self.allert_save_text) # Проверяю аллерт
        # Обновляю страницу и проверяю измененные элементы
        BM(browser=self.browser).page_reload() # Обновляю страницу
        BM(browser=self.browser).checking_the_presence_of_an_element_on_the_page(selector=self.system_menu_item)
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.checksum_configuration_control_mq_queue_name, second_value='testchecksum', atribut='value') # Проверяю "Очередь модуля Расчета контрольных сумм"
        # Возвращаю стандартные настройки
        BM(browser=self.browser).enter_text_in_the_element(selector=self.checksum_configuration_control_mq_queue_name, input_text='checksum') # Редактирование настройки "Очередь модуля Расчета контрольных сумм"
        BM(browser=self.browser).click_on_the_element(selector=self.system_configuration_save_button) # Сохраняю измененные настройки
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value=self.allert_save_text) # Проверяю аллерт

    def publishing_data(self):
        """Редактирование настроек Система --> Публикация данных"""
        BM(browser=self.browser).click_on_the_element(selector=self.system_menu_item) # Раскрытие "Система"
        BM(browser=self.browser).click_on_the_element(selector=self.publisher_menu_item) # Переход к Публикация данных
        # Редактирование настроек
        BM(browser=self.browser).enter_text_in_the_element(selector=self.publisher_configuration_control_mq_queue_name, input_text='testpublisher') # Редактирование настройки "Очередь модуля Публикации данных"
        BM(browser=self.browser).click_on_the_element(selector=self.system_configuration_save_button) # Сохраняю измененные настройки
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value=self.allert_save_text) # Проверяю аллерт
        # Обновляю страницу и проверяю измененные элементы
        BM(browser=self.browser).page_reload() # Обновляю страницу
        BM(browser=self.browser).checking_the_presence_of_an_element_on_the_page(selector=self.system_menu_item)
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.publisher_configuration_control_mq_queue_name, second_value='testpublisher', atribut='value') # Проверяю Очередь модуля Публикации данных"
        # Возвращаю стандартные настройки
        BM(browser=self.browser).enter_text_in_the_element(selector=self.publisher_configuration_control_mq_queue_name, input_text='publisher') # Редактирование настройки "Очередь модуля Публикации данных"
        BM(browser=self.browser).click_on_the_element(selector=self.system_configuration_save_button) # Сохраняю измененные настройки
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value=self.allert_save_text) # Проверяю аллерт

    def cleaning_the_supply_catalog(self):
        """Редактирование настроек Система --> Очистка каталога поставок"""
        BM(browser=self.browser).click_on_the_element(selector=self.system_menu_item) # Раскрытие "Система"
        BM(browser=self.browser).click_on_the_element(selector=self.cleaner_menu_item) # Переход к Очистка каталога поставок
        # Редактирование настроек
        BM(browser=self.browser).enter_text_in_the_element(selector=self.cleaner_configuration_control_mq_queue_name, input_text='testcleaner') # Редактирование настройки "Очередь модуля Очистки каталога поставок"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.cleaner_configuration_control_supply_storage_time, input_text='111') # Редактирование настройки "Время хранения поставок"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.cleaner_configuration_control_period_of_check, input_text='111') # Редактирование настройки "Период запуска очистки"
        BM(browser=self.browser).click_on_the_element(selector=self.system_configuration_save_button) # Сохраняю измененные настройки
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value=self.allert_save_text) # Проверяю аллерт
        # Обновляю страницу и проверяю измененные элементы
        BM(browser=self.browser).page_reload() # Обновляю страницу
        BM(browser=self.browser).checking_the_presence_of_an_element_on_the_page(selector=self.system_menu_item)
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.cleaner_configuration_control_mq_queue_name, second_value='testcleaner', atribut='value') # Проверяю "Очередь модуля Очистки каталога поставок"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.cleaner_configuration_control_supply_storage_time, second_value='111', atribut='value') # Проверяю "Время хранения поставок"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.cleaner_configuration_control_period_of_check, second_value='111', atribut='value') # Проверяю "Период запуска очистки"
        # Возвращаю стандартные настройки
        BM(browser=self.browser).enter_text_in_the_element(selector=self.cleaner_configuration_control_mq_queue_name, input_text='cleaner') # Редактирование настройки "Очередь модуля Очистки каталога поставок"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.cleaner_configuration_control_supply_storage_time, input_text='7') # Редактирование настройки "Время хранения поставок"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.cleaner_configuration_control_period_of_check, input_text='6') # Редактирование настройки "Период запуска очистки"
        BM(browser=self.browser).click_on_the_element(selector=self.system_configuration_save_button) # Сохраняю измененные настройки
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value=self.allert_save_text) # Проверяю аллерт

    def application_programming_interface(self):
        """Редактирование настроек Система --> API"""
        BM(browser=self.browser).click_on_the_element(selector=self.system_menu_item) # Раскрытие "Система"
        BM(browser=self.browser).click_on_the_element(selector=self.api_menu_item) # Переход к API
        # Редактирование настроек
        BM(browser=self.browser).enter_text_in_the_element(selector=self.api_configuration_control_mq_queue_name, input_text='testapi') # Редактирование настройки "Очередь модуля API веб-интерфейса"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.api_configuration_control_ldap_user_dn, input_text='testdc=vip,dc=cbr,dc=ru') # Редактирование настройки "Верхняя запись LDAP для поиска пользователей"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.api_configuration_control_ldap_group_dn, input_text='testOU=МЗП,OU=УТС,OU=ДИТ,DC=vip,DC=cbr,DC=ru') # Редактирование настройки "Верхняя запись LDAP для поиска групп"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.api_configuration_control_ldap_group_roles_filter, input_text='test(&(objectClass=group)(!(memberOf=CN=Релиз менеджер,OU=МПП,OU=УТС,OU=ДИТ,DC=vip,DC=cbr,DC=ru)))') # Редактирование настройки "Фильтр поиска LDAP групп для ролей МПП"
        BM(browser=self.browser).click_on_the_element_no_roll(selector=self.api_configuration_control_ldap_user_search_scope) # Раскрытие настройки "Глубина поиска записей в LDAP"
        BM(browser=self.browser).click_on_the_element_no_roll(selector='//*[@id="configuration-control-ldap.user.search_scope-option-0"]') # Выбор протокола BASE
        BM(browser=self.browser).enter_text_in_the_element(selector=self.api_configuration_control_ldap_host, input_text='0.0.0.0') # Редактирование настройки "Сервер LDAP"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.api_configuration_control_ldap_bind_user, input_text='testsvc-adm') # Редактирование настройки "Системный пользователь LDAP"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.api_configuration_control_ldap_user_attribute, input_text='testsAMAccountName') # Редактирование настройки "Свойство записи LDAP для поиска логина пользователя"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.api_configuration_control_ldap_port, input_text='1111') # Редактирование настройки "Порт сервера LDAP"
        BM(browser=self.browser).click_on_the_element(selector=self.system_configuration_save_button) # Сохраняю измененные настройки
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value=self.allert_save_text) # Проверяю аллерт
        # Обновляю страницу и проверяю измененные элементы
        BM(browser=self.browser).page_reload() # Обновляю страницу
        BM(browser=self.browser).checking_the_presence_of_an_element_on_the_page(selector=self.system_menu_item)
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.api_configuration_control_mq_queue_name, second_value='testapi', atribut='value') # Проверяю "Очередь модуля API веб-интерфейса"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.api_configuration_control_ldap_user_dn, second_value='testdc=vip,dc=cbr,dc=ru', atribut='value') # Проверяю "Верхняя запись LDAP для поиска пользователей"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.api_configuration_control_ldap_group_dn, second_value='testOU=МЗП,OU=УТС,OU=ДИТ,DC=vip,DC=cbr,DC=ru', atribut='value') # Проверяю "Верхняя запись LDAP для поиска групп"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.api_configuration_control_ldap_group_roles_filter, second_value='test(&(objectClass=group)(!(memberOf=CN=Релиз менеджер,OU=МПП,OU=УТС,OU=ДИТ,DC=vip,DC=cbr,DC=ru)))', atribut='value') # Проверяю "Фильтр поиска LDAP групп для ролей МПП"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.api_configuration_control_ldap_user_search_scope, second_value='BASE', atribut='value') # Проверяю "Глубина поиска записей в LDAP"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.api_configuration_control_ldap_host, second_value='0.0.0.0', atribut='value') # Проверяю "Сервер LDAP"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.api_configuration_control_ldap_bind_user, second_value='testsvc-adm', atribut='value') # Проверяю "Системный пользователь LDAP"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.api_configuration_control_ldap_user_attribute, second_value='testsAMAccountName', atribut='value') # Проверяю "Свойство записи LDAP для поиска логина пользователя"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.api_configuration_control_ldap_port, second_value='1111', atribut='value') # Проверяю "Порт сервера LDAP"
        # Возвращаю стандартные настройки
        BM(browser=self.browser).enter_text_in_the_element(selector=self.api_configuration_control_mq_queue_name, input_text='api') # Редактирование настройки "Очередь модуля API веб-интерфейса"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.api_configuration_control_ldap_user_dn, input_text='dc=vip,dc=cbr,dc=ru') # Редактирование настройки "Верхняя запись LDAP для поиска пользователей"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.api_configuration_control_ldap_group_dn, input_text='OU=МЗП,OU=УТС,OU=ДИТ,DC=vip,DC=cbr,DC=ru') # Редактирование настройки "Верхняя запись LDAP для поиска групп"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.api_configuration_control_ldap_group_roles_filter, input_text='(&(objectClass=group)(!(memberOf=CN=Релиз менеджер,OU=МПП,OU=УТС,OU=ДИТ,DC=vip,DC=cbr,DC=ru)))') # Редактирование настройки "Фильтр поиска LDAP групп для ролей МПП"
        BM(browser=self.browser).click_on_the_element_no_roll(selector=self.api_configuration_control_ldap_user_search_scope) # Раскрытие настройки "Глубина поиска записей в LDAP"
        BM(browser=self.browser).click_on_the_element_no_roll(selector='//*[@id="configuration-control-ldap.user.search_scope-option-2"]') # Выбор протокола BASE
        BM(browser=self.browser).enter_text_in_the_element(selector=self.api_configuration_control_ldap_host, input_text='172.29.39.94') # Редактирование настройки "Сервер LDAP"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.api_configuration_control_ldap_bind_user, input_text='svc-adm') # Редактирование настройки "Системный пользователь LDAP"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.api_configuration_control_ldap_user_attribute, input_text='sAMAccountName') # Редактирование настройки "Свойство записи LDAP для поиска логина пользователя"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.api_configuration_control_ldap_port, input_text='3268') # Редактирование настройки "Порт сервера LDAP"
        BM(browser=self.browser).click_on_the_element(selector=self.system_configuration_save_button) # Сохраняю измененные настройки
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value=self.allert_save_text) # Проверяю аллерт

    def notifications_settings(self):
        """Редактирование настроек Система --> Уведомления"""
        BM(browser=self.browser).click_on_the_element(selector=self.system_menu_item) # Раскрытие "Система"
        BM(browser=self.browser).click_on_the_element(selector=self.notification_menu_item) # Переход к API
        # Редактирование настроек
        BM(browser=self.browser).enter_text_in_the_element(selector=self.notification_configuration_control_mq_queue_name, input_text='testnotification') # Редактирование настройки "Очередь модуля"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.notification_configuration_control_mail_output_fromaddress, input_text='testinbox_mpp@star.lanit.ru') # Редактирование настройки "Адрес, от кого отправляется письмо"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.notification_configuration_control_mail_output_host, input_text='testmail.star.lanit.ru') # Редактирование настройки "Хост почтового сервера для отправки писем"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.notification_configuration_control_mail_output_port, input_text='111') # Редактирование настройки "Порт почтового сервера для отправки писем"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.notification_configuration_control_mail_output_user, input_text='testinbox_mpp@star.lanit.ru') # Редактирование настройки "Имя пользователя аккаунта исходящей почты"
        BM(browser=self.browser).click_on_the_element_no_roll(selector=self.notification_configuration_control_mail_output_strategy) # Раскрытие настройки "Стратегия для отправки писем"
        BM(browser=self.browser).click_on_the_element_no_roll(selector='//*[@id="configuration-control-mail.output.strategy-option-2"]') # Выбор протокола SMTP_TLS
        BM(browser=self.browser).click_on_the_element(selector=self.system_configuration_save_button) # Сохраняю измененные настройки
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value=self.allert_save_text) # Проверяю аллерт
        # Обновляю страницу и проверяю измененные элементы
        BM(browser=self.browser).page_reload() # Обновляю страницу
        BM(browser=self.browser).checking_the_presence_of_an_element_on_the_page(selector=self.system_menu_item)
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.notification_configuration_control_mq_queue_name, second_value='testnotification', atribut='value') # Проверяю "Очередь модуля"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.notification_configuration_control_mail_output_fromaddress, second_value='testinbox_mpp@star.lanit.ru', atribut='value') # Проверяю ""Адрес, от кого отправляется письмо""
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.notification_configuration_control_mail_output_host, second_value='testmail.star.lanit.ru', atribut='value') # Проверяю "Хост почтового сервера для отправки писем"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.notification_configuration_control_mail_output_port, second_value='111', atribut='value') # Проверяю "Порт почтового сервера для отправки писем"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.notification_configuration_control_mail_output_user, second_value='testinbox_mpp@star.lanit.ru', atribut='value') # Проверяю "Имя пользователя аккаунта исходящей почты"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.notification_configuration_control_mail_output_strategy, second_value='SMTP_TLS', atribut='value') # Проверяю "Стратегия для отправки писем"
        # Возвращаю стандартные настройки
        BM(browser=self.browser).enter_text_in_the_element(selector=self.notification_configuration_control_mq_queue_name, input_text='notification') # Редактирование настройки "Очередь модуля"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.notification_configuration_control_mail_output_fromaddress, input_text='inbox_mpp@star.lanit.ru') # Редактирование настройки "Адрес, от кого отправляется письмо"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.notification_configuration_control_mail_output_host, input_text='mail.star.lanit.ru') # Редактирование настройки "Хост почтового сервера для отправки писем"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.notification_configuration_control_mail_output_port, input_text='25') # Редактирование настройки "Порт почтового сервера для отправки писем"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.notification_configuration_control_mail_output_user, input_text='inbox_mpp@star.lanit.ru') # Редактирование настройки "Имя пользователя аккаунта исходящей почты"
        BM(browser=self.browser).click_on_the_element_no_roll(selector=self.notification_configuration_control_mail_output_strategy) # Раскрытие настройки "Стратегия для отправки писем"
        BM(browser=self.browser).click_on_the_element_no_roll(selector='//*[@id="configuration-control-mail.output.strategy-option-0"]') # Выбор протокола SMTP_TLS
        BM(browser=self.browser).click_on_the_element(selector=self.system_configuration_save_button) # Сохраняю измененные настройки
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value=self.allert_save_text) # Проверяю аллерт

    def activemq_message_broker(self):
        """Редактирование настроек Система --> Брокер сообщений ActiveMQ"""
        BM(browser=self.browser).click_on_the_element(selector=self.system_menu_item) # Раскрытие "Система"
        BM(browser=self.browser).click_on_the_element(selector=self.activemq_menu_item) # Переход к Брокер сообщений ActiveMQ
        # Редактирование настроек
        BM(browser=self.browser).enter_text_in_the_element(selector=self.activemq_configuration_control_mq_broker_host, input_text='testlocalhost') # Редактирование настройки "Адрес хоста брокера сообщений"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.activemq_configuration_control_mq_broker_port, input_text='11111') # Редактирование настройки "Порт хоста брокера сообщений"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.activemq_configuration_control_mq_broker_user, input_text='testmpp') # Редактирование настройки "Имя пользователя брокера сообщений"
        BM(browser=self.browser).click_on_the_element(selector=self.system_configuration_save_button) # Сохраняю измененные настройки
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value=self.allert_save_text) # Проверяю аллерт
        # Обновляю страницу и проверяю измененные элементы
        BM(browser=self.browser).page_reload() # Обновляю страницу
        BM(browser=self.browser).checking_the_presence_of_an_element_on_the_page(selector=self.system_menu_item)
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.activemq_configuration_control_mq_broker_host, second_value='testlocalhost', atribut='value') # Проверяю "Адрес хоста брокера сообщений"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.activemq_configuration_control_mq_broker_port, second_value='11111', atribut='value') # Проверяю "Порт хоста брокера сообщений"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.activemq_configuration_control_mq_broker_user, second_value='testmpp', atribut='value') # Проверяю "Имя пользователя брокера сообщений"
        # Возвращаю стандартные настройки
        BM(browser=self.browser).enter_text_in_the_element(selector=self.activemq_configuration_control_mq_broker_host, input_text='localhost') # Редактирование настройки "Адрес хоста брокера сообщений"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.activemq_configuration_control_mq_broker_port, input_text='61616') # Редактирование настройки "Порт хоста брокера сообщений"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.activemq_configuration_control_mq_broker_user, input_text='mpp') # Редактирование настройки "Имя пользователя брокера сообщений"
        BM(browser=self.browser).click_on_the_element(selector=self.system_configuration_save_button) # Сохраняю измененные настройки
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value=self.allert_save_text) # Проверяю аллерт


# -------------------------------------------- Типы публикаций --------------------------------------------
class types_of_publications:
    # ЭЛЕМЕНТЫ
    settings_page_link = 'https://mpp-tst-mr1.star.lanit.ru/configuration/'                                                         # Страница Настроек
    seetings_button_page_link = '//*[@id="configuration-header-button"]'                                                            # Кнопка "Настройки" в хэдере
    types_menu_item = '//*[@id="types-menu-item"]'                                                                                  # Кнопка "Типы публикаций"
    types_menu_b01 = '//*[@id="typeC01-menu-item"]'                                                                                 # Кнопка "Типы публикаций C01"
    types_button_destinations = '//*[@id="destinations-sections-navigation-tab"]'                                                   # Кнопка "Места публикаций"
    add_new_places_of_publication = '//*[@id="table-add-button"]'                                                                   # Кнопка "Добавить" новое место публикации
    path_places_of_publication_name = '//*[@id="destinationName-input"]'                                                            # Путь Название
    path_places_of_publication_adress = '//*[@id="url-input"]'                                                                      # Путь Адрес
    path_places_of_publication_api = '//*[@id="apiKey-input"]'                                                                      # Путь API
    path_places_of_publication_filter = '//*[@id="regexp-input"]'                                                                   # Путь Фильтр темы поставки
    path_places_of_publication_user = '//*[@id="username-input"]'                                                                   # Путь Пользователь
    path_places_of_publication_password = '//*[@id="password-input"]'                                                               # Путь Пароль
    path_places_of_publication_settings = '//*[@id="destination-settings-values-select"]'                                           # Поле инпута "Тип места публикации"

    save_button = '//*[text()="Сохранить"]'                                                                                         # Кнопка "Сохранить"
    cancel_button = '//*[text()="Отменить"]'                                                                                        # Кнопка "Отменить"
    allert_save_text_xpath = '/html/body/div/div[1]/div/div'                                                                        # Поле всплывающего аллерта

    # ЗНАЧЕНИЯ
    value_places_of_publication_name = 'tname'                                                                                      # Значение Названиe
    value_places_of_publication_adress = '0.0.0.0'                                                                                  # Значение Адрес
    value_places_of_publication_api = 'f4a43a3ga3g34g'                                                                              # Значение API 
    value_places_of_publication_filter = '^C01_Adm'                                                                                 # Значение Фильтр темы поставки
    value_places_of_publication_user = 'tuser'                                                                                      # Значение Пользователь
    value_places_of_publication_password = 'tpassword'                                                                              # Значение Пароль

    def __init__(self, browser) -> None:
        self.browser = browser

    def switch_to_publication_type(self):
        """Переход в Настройки"""
        BM(browser=self.browser).click_on_the_element(selector=self.seetings_button_page_link) # Переход на страницу "Настройки"
        BM(browser=self.browser).getting_a_text_element(selector=self.types_menu_item) # Проверка перехода

    def crud_places_of_publication(self):
        """КРУД Места публикаций"""
        BM(browser=self.browser).click_on_the_element(selector=self.types_menu_item) # Раскрываю "Типы публикаций"
        BM(browser=self.browser).click_on_the_element(selector=self.types_menu_b01) # Выбираю Тип C01
        BM(browser=self.browser).click_on_the_element(selector=self.types_button_destinations) # Выбираю "Места публикаций"
        # Создания места публикации
        BM(browser=self.browser).click_on_the_element(selector=self.add_new_places_of_publication) # Нажимаю кнопку "Добавить"
        BM(browser=self.browser).enter_text_in_the_element(selector=self.path_places_of_publication_name, input_text=self.value_places_of_publication_name) # Вписываю название
        BM(browser=self.browser).enter_text_in_the_element(selector=self.path_places_of_publication_adress, input_text=self.value_places_of_publication_adress) # Вписываю Адрес
        BM(browser=self.browser).enter_text_in_the_element(selector=self.path_places_of_publication_api, input_text=self.value_places_of_publication_api) # Вписываю API
        BM(browser=self.browser).enter_text_in_the_element(selector=self.path_places_of_publication_filter, input_text=self.value_places_of_publication_filter) # Вписываю Фильтр
        BM(browser=self.browser).enter_text_in_the_element(selector=self.path_places_of_publication_user, input_text=self.value_places_of_publication_user) # Вписываю Пользователь
        BM(browser=self.browser).enter_text_in_the_element(selector=self.path_places_of_publication_password, input_text=self.value_places_of_publication_password) # Вписываю Пароль
        BM(browser=self.browser).click_on_the_element(selector=self.path_places_of_publication_settings) # Раскрываю Тип места публикации
        BM(browser=self.browser).click_on_the_element(selector='//*[@id="destination-settings-values-select-option-0"]') # Выбираю ftp
        BM(browser=self.browser).click_on_the_element(selector=self.save_button) # Нажимаю кнопку "Сохранить"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value="Место публикации успешно добавлено") # Проверяю аллерт
        # Проверка созданного места публикации
        BM(browser=self.browser).page_reload() # Обновление страницы
        BM(browser=self.browser).click_on_the_element(selector=self.types_button_destinations) # Выбираю "Места публикаций"
        BM(browser=self.browser).getting_a_text_element(selector=self.add_new_places_of_publication) # Проверка Отображения страницы
        BM(browser=self.browser).click_on_the_element(selector=f"//*[text()='{self.value_places_of_publication_name}']/..//*[@aria-label='Редактировать']")
        BM(browser=self.browser).getting_a_text_element(selector=self.path_places_of_publication_name) # Проверка Отображения Места публикации
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.path_places_of_publication_name, second_value=self.value_places_of_publication_name, atribut='value') # Проверяю название
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.path_places_of_publication_adress, second_value=self.value_places_of_publication_adress, atribut='value') # Проверяю Адрес
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.path_places_of_publication_api, second_value='*****', atribut='value') # Проверяю API
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.path_places_of_publication_filter, second_value=self.value_places_of_publication_filter, atribut='value') # Проверяю Фильтр
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.path_places_of_publication_user, second_value=self.value_places_of_publication_user, atribut='value') # Проверяю Пользователь
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.path_places_of_publication_password, second_value='*****', atribut='value') # Проверяю Пароль
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.path_places_of_publication_settings, second_value='ftp', atribut='value') # Проверяю Тип места публикации
        # Редактирование места публикации
        BM(browser=self.browser).enter_text_in_the_element(selector=self.path_places_of_publication_name, input_text=f"t{self.value_places_of_publication_name}") # Вписываю название
        BM(browser=self.browser).enter_text_in_the_element(selector=self.path_places_of_publication_adress, input_text=f"t{self.value_places_of_publication_adress}") # Вписываю Адрес
        BM(browser=self.browser).enter_text_in_the_element(selector=self.path_places_of_publication_api, input_text=f"t{self.value_places_of_publication_api}") # Вписываю API
        BM(browser=self.browser).enter_text_in_the_element(selector=self.path_places_of_publication_filter, input_text=f"t{self.value_places_of_publication_filter}") # Вписываю Фильтр
        BM(browser=self.browser).enter_text_in_the_element(selector=self.path_places_of_publication_user, input_text=f"t{self.value_places_of_publication_user}") # Вписываю Пользователь
        BM(browser=self.browser).enter_text_in_the_element(selector=self.path_places_of_publication_password, input_text=f"t{self.value_places_of_publication_password}") # Вписываю Пароль
        BM(browser=self.browser).click_on_the_element(selector=self.path_places_of_publication_settings) # Раскрываю Тип места публикации
        BM(browser=self.browser).click_on_the_element(selector='//*[@id="destination-settings-values-select-option-1"]') # Выбираю smb
        BM(browser=self.browser).click_on_the_element(selector=self.save_button) # Нажимаю кнопку "Сохранить"
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value="Место публикации успешно изменено") # Проверяю аллерт
        # Проверка места публикации
        BM(browser=self.browser).page_reload() # Обновление страницы
        BM(browser=self.browser).click_on_the_element(selector=self.types_button_destinations) # Выбираю "Места публикаций"
        BM(browser=self.browser).getting_a_text_element(selector=self.add_new_places_of_publication) # Проверка Отображения страницы
        BM(browser=self.browser).click_on_the_element(selector=f"//*[text()='t{self.value_places_of_publication_name}']/..//*[@aria-label='Редактировать']")
        BM(browser=self.browser).getting_a_text_element(selector=self.path_places_of_publication_name) # Проверка Отображения Места публикации
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.path_places_of_publication_name, second_value=f"t{self.value_places_of_publication_name}", atribut='value') # Проверяю название
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.path_places_of_publication_adress, second_value=f"t{self.value_places_of_publication_adress}", atribut='value') # Проверяю Адрес
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.path_places_of_publication_api, second_value='*****', atribut='value') # Проверяю API
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.path_places_of_publication_filter, second_value=f"t{self.value_places_of_publication_filter}", atribut='value') # Проверяю Фильтр
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.path_places_of_publication_user, second_value=f"t{self.value_places_of_publication_user}", atribut='value') # Проверяю Пользователь
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.path_places_of_publication_password, second_value='*****', atribut='value') # Проверяю Пароль
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.path_places_of_publication_settings, second_value='smb', atribut='value') # Проверяю Тип места публикации
        BM(browser=self.browser).click_on_the_element(selector=self.cancel_button)
        # Удаляю место публикации
        BM(browser=self.browser).click_on_the_element(selector=f"//*[text()='t{self.value_places_of_publication_name}']/..//*[@aria-label='Удалить']") # Нажимаю кнопку "Удалить"
        BM(browser=self.browser).click_on_the_element(selector='//*[@id="destination-delete-dialog-delete-button"]') # Подтверждение удаления
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value=f"Место публикации t{self.value_places_of_publication_name} успешно удалено") # Проверяю аллерт


# -------------------------------------------- Маршруты ---------------------------------------------------


# -------------------------------------------- Сервисы ----------------------------------------------------
class services:
    # ЭЛЕМЕНТЫ
    settings_button = '//*[@id="configuration-header-button"]'                                                                      # Кнопка "Настроек"
    services_buton = '//*[@id="services-menu-item"]'                                                                                # Кнопка "Логирование" на странице настроек
    stop_button = '//*[@id="services-select-panel-stop-button"]'                                                                    # Кнопка "Остановки" сервиса
    allert_save_text_xpath = '/html/body/div/div[1]/div/div/div[1]'                                                                 # Поле всплывающего аллерта
    # ЗНАЧЕНИЯ
    stop_service_text = "Остановлен"                                                                                                # Значение остановленного текста   

    def __init__(self, browser) -> None:
        self.browser = browser

    def go_to_services_page(self):
        BM(browser=self.browser).click_on_the_element(selector=self.settings_button) # Нажимаю кнопку "Настройки"
        BM(browser=self.browser).click_on_the_element(selector=self.services_buton) # Нажимаю кнопку "Логирование"
    
    def disabling_and_enabling_services(self, service_check, xpath_stop_service, xpath_start_service):
        """Отключение и включение каждого сервиса"""
        BM(browser=self.browser).click_on_the_element(selector=service_check) # Выбираю сервис
        BM(browser=self.browser).click_on_the_element(selector=self.stop_button) # Останавливаю сервис
        BM(browser=self.browser).checking_the_presence_of_an_element_on_the_page(selector=self.allert_save_text_xpath, wait_time=20) # Проверяю аллерт
        BM(browser=self.browser).page_reload() # Обновление страницы
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=xpath_stop_service, second_value=self.stop_service_text) # Проверяю что сервис остановлен
        BM(browser=self.browser).click_on_the_element(selector=xpath_start_service) # Запускаю сервис
        BM(browser=self.browser).checking_the_presence_of_an_element_on_the_page(selector=self.allert_save_text_xpath, wait_time=20) # Проверяю аллерт
        BM(browser=self.browser).page_reload() # Обновление страницы





# -------------------------------------------- Логирование ------------------------------------------------
class logging:
    # ЭЛЕМЕНТЫ
    settings_button = '//*[@id="configuration-header-button"]'                                                                      # Кнопка "Настроек"
    logging_buton = '//*[@id="logging-configuration-menu-item"]'                                                                    # Кнопка "Логирование" на странице настроек
    receiver_module_setting_button = '//*[@id="receiver-module-setting-button"]'                                                    # Кнопка раскрытия модуля "Получение поставок"
    decryption_module_setting_button = '//*[@id="decryption-module-setting-button"]'                                                # Кнопка раскрытия модуля "Криптографическая обработка данных"
    unzip_module_setting_button = '//*[@id="unzip-module-setting-button"]'                                                          # Кнопка раскрытия модуля "Распаковки поставок"
    validator_module_setting_button = '//*[@id="validator-module-setting-button"]'                                                  # Кнопка раскрытия модуля "Валидация файлов"
    antivir_module_setting_button = '//*[@id="antivir-module-setting-button"]'                                                      # Кнопка раскрытия модуля "Антивирусная проверка"
    checkSum_module_setting_button = '//*[@id="checkSum-module-setting-button"]'                                                    # Кнопка раскрытия модуля "Расчет контрольных сумм"
    publisher_module_setting_button = '//*[@id="publisher-module-setting-button"]'                                                  # Кнопка раскрытия модуля "Публикация данных"
    cleaner_module_setting_button = '//*[@id="cleaner-module-setting-button"]'                                                      # Кнопка раскрытия модуля "Очистка каталога поставок"
    api_module_setting_button = '//*[@id="api-module-setting-button"]'                                                              # Кнопка раскрытия модуля "API"
    notification_module_setting_button = '//*[@id="notification-module-setting-button"]'                                            # Кнопка раскрытия модуля "Уведомления"
    type_warning = '//*[@id="WARNING-logging-setting-menu-item"]'                                                                   # Тип WARNING
    type_debug = '//*[@id="DEBUG-logging-setting-menu-item"]'                                                                       # Тип DEBUG
    save_button = '//*[text()="Сохранить"]'                                                                                         # Кнопка "Сохранить"
    cancel_button = '//*[text()="Отменить"]'                                                                                        # Кнопка "Отменить"
    allert_save_text_xpath = '/html/body/div/div[1]/div/div'                                                                        # Поле всплывающего аллерта

    # ЗНАЧЕНИЯ
    tetxt_type_warning = 'WARNING'                                                                                                  # Текст варининг уровня логирования
    tetxt_type_debug = 'DEBUG'                                                                                                      # Текст дебаг уровня логирования

    def __init__(self, browser) -> None:
        self.browser = browser

    def go_to_logging_page(self):
        BM(browser=self.browser).click_on_the_element(selector=self.settings_button) # Нажимаю кнопку "Настройки"
        BM(browser=self.browser).click_on_the_element(selector=self.logging_buton) # Нажимаю кнопку "Логирование"

    def check_logging(self):
        """Изменение настроек логирования и их проверка"""
        # Перевожу все модули в "Warning"
        BM(browser=self.browser).click_on_the_element(selector=self.receiver_module_setting_button) # Раскрваю "Получение поставок"
        BM(browser=self.browser).click_on_the_element(selector=self.type_warning) # Выбираю WARNING
        BM(browser=self.browser).click_on_the_element(selector=self.decryption_module_setting_button) # Раскрваю "Криптографическая обработка данных"
        BM(browser=self.browser).click_on_the_element(selector=self.type_warning) # Выбираю WARNING
        BM(browser=self.browser).click_on_the_element(selector=self.unzip_module_setting_button) # Раскрваю "Распаковки поставок"
        BM(browser=self.browser).click_on_the_element(selector=self.type_warning) # Выбираю WARNING
        BM(browser=self.browser).click_on_the_element(selector=self.validator_module_setting_button) # Раскрваю "Валидация файлов"
        BM(browser=self.browser).click_on_the_element(selector=self.type_warning) # Выбираю WARNING
        BM(browser=self.browser).click_on_the_element(selector=self.antivir_module_setting_button) # Раскрваю "Антивирусная проверка"
        BM(browser=self.browser).click_on_the_element(selector=self.type_warning) # Выбираю WARNING
        BM(browser=self.browser).click_on_the_element(selector=self.checkSum_module_setting_button) # Раскрваю "Расчет контрольных сумм"
        BM(browser=self.browser).click_on_the_element(selector=self.type_warning) # Выбираю WARNING
        BM(browser=self.browser).click_on_the_element(selector=self.publisher_module_setting_button) # Раскрваю "Публикация данных"
        BM(browser=self.browser).click_on_the_element(selector=self.type_warning) # Выбираю WARNING
        BM(browser=self.browser).click_on_the_element(selector=self.cleaner_module_setting_button) # Раскрваю "Очистка каталога поставок"
        BM(browser=self.browser).click_on_the_element(selector=self.type_warning) # Выбираю WARNING
        BM(browser=self.browser).click_on_the_element(selector=self.api_module_setting_button) # Раскрваю "API"
        BM(browser=self.browser).click_on_the_element(selector=self.type_warning) # Выбираю WARNING
        BM(browser=self.browser).click_on_the_element(selector=self.notification_module_setting_button) # Раскрваю "Уведомления"
        BM(browser=self.browser).click_on_the_element(selector=self.type_warning) # Выбираю WARNING
        # Проверка значений
        BM(browser=self.browser).page_reload() # Обновление страницы
        BM(browser=self.browser).checking_the_presence_of_an_element_on_the_page(selector=self.receiver_module_setting_button) # Проверяю загрузку страницы
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.receiver_module_setting_button, second_value=self.tetxt_type_warning, atribut='textContent')
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.decryption_module_setting_button, second_value=self.tetxt_type_warning, atribut='textContent')
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.unzip_module_setting_button, second_value=self.tetxt_type_warning, atribut='textContent')
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.validator_module_setting_button, second_value=self.tetxt_type_warning, atribut='textContent')
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.antivir_module_setting_button, second_value=self.tetxt_type_warning, atribut='textContent')
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.checkSum_module_setting_button, second_value=self.tetxt_type_warning, atribut='textContent')
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.publisher_module_setting_button, second_value=self.tetxt_type_warning, atribut='textContent')
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.cleaner_module_setting_button, second_value=self.tetxt_type_warning, atribut='textContent')
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.api_module_setting_button, second_value=self.tetxt_type_warning, atribut='textContent')
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.notification_module_setting_button, second_value=self.tetxt_type_warning, atribut='textContent')
        # Возвращаю старые значения
        BM(browser=self.browser).click_on_the_element(selector=self.receiver_module_setting_button) # Раскрваю "Получение поставок"
        BM(browser=self.browser).click_on_the_element(selector=self.type_debug) # Выбираю DEBUG
        BM(browser=self.browser).click_on_the_element(selector=self.decryption_module_setting_button) # Раскрваю "Криптографическая обработка данных"
        BM(browser=self.browser).click_on_the_element(selector=self.type_debug) # Выбираю DEBUG
        BM(browser=self.browser).click_on_the_element(selector=self.unzip_module_setting_button) # Раскрваю "Распаковки поставок"
        BM(browser=self.browser).click_on_the_element(selector=self.type_debug) # Выбираю DEBUG
        BM(browser=self.browser).click_on_the_element(selector=self.validator_module_setting_button) # Раскрваю "Валидация файлов"
        BM(browser=self.browser).click_on_the_element(selector=self.type_debug) # Выбираю DEBUG
        BM(browser=self.browser).click_on_the_element(selector=self.antivir_module_setting_button) # Раскрваю "Антивирусная проверка"
        BM(browser=self.browser).click_on_the_element(selector=self.type_debug) # Выбираю DEBUG
        BM(browser=self.browser).click_on_the_element(selector=self.checkSum_module_setting_button) # Раскрваю "Расчет контрольных сумм"
        BM(browser=self.browser).click_on_the_element(selector=self.type_debug) # Выбираю DEBUG
        BM(browser=self.browser).click_on_the_element(selector=self.publisher_module_setting_button) # Раскрваю "Публикация данных"
        BM(browser=self.browser).click_on_the_element(selector=self.type_debug) # Выбираю DEBUG
        BM(browser=self.browser).click_on_the_element(selector=self.cleaner_module_setting_button) # Раскрваю "Очистка каталога поставок"
        BM(browser=self.browser).click_on_the_element(selector=self.type_debug) # Выбираю DEBUG
        BM(browser=self.browser).click_on_the_element(selector=self.api_module_setting_button) # Раскрваю "API"
        BM(browser=self.browser).click_on_the_element(selector=self.type_debug) # Выбираю DEBUG
        BM(browser=self.browser).click_on_the_element(selector=self.notification_module_setting_button) # Раскрваю "Уведомления"
        BM(browser=self.browser).click_on_the_element(selector=self.type_debug) # Выбираю DEBUG




# -------------------------------------------- Разработчики -----------------------------------------------
class developers:
    # ЭЛЕМЕНТЫ
    developers_page = 'https://mpp-tst-mr1.star.lanit.ru/configuration/developers'                                                  # Страница "Разработчики"
    button_add_new_developer = '//*[@id="table-add-button"]'                                                                        # Кнопка "Добавить" нового разработчика
    input_name_new_developer = '//*[@id="devName-input"]'                                                                           # Поле добавления имени нового разработчика
    input_devid_new_developer = '//*[@id="shortName-input"]'                                                                        # Поле добавления DevID нового разработчика
    input_email_new_developer = '//*[@id="email-input"]'                                                                            # Поле добавления почты нового разработчика
    notify_when_a_letter_is_received = '//*[@id="notifyPublish-switch"]'                                                            # Поле "Уведомлять о получении письма"
    тotify_about_the_publication_of_a_letter = '//*[@id="notifyReceive-switch"]'                                                    # Поле "Уведомлять о публикации письма"
    save_button = "//*[text()='Сохранить']"                                                                                         # Поле "Сохранить" разработчика
    exit_button = "//*[text()='Отменить']"                                                                                          # Поле "Отменить" разработчика
    allert_save_text_xpath = '/html/body/div/div[1]/div/div'                                                                        # Поле всплывающего аллерта
    find_create_developer = "//*[text()='TestDev']/..//*[@aria-label='Редактировать']"                                              # Функция открытия на редактирование только что созданного разработчика
    find_change_developer = "//*[text()='t_TestDev']/..//*[@aria-label='Редактировать']"                                            # Открыаю отредактированного разработчика на редактирование
    find_delete_developer = '//*[text()="t_TestDev"]/..//*[@aria-label="Удалить"]'                                                  # Кнопка удаления разработчика

    # ЗНАЧЕНИЯ
    value_name_new_developer = 'TestDev'                                                                                            # Имя нового разработчика
    value_devid_new_developer = 'TestDev'                                                                                           # DevID нового разработчика
    value_email_new_developer = 'TestDev@test.ru'                                                                                   # Почта нового разработчика


    def __init__(self, browser) -> None:
        self.browser = browser

    def go_to_developers_page(self):
        """Переход на страницу настроек"""
        BM(browser=self.browser).go_to_the_page(link=self.developers_page)

    def crud_developers(self):
        """Создание, проверка, изменение и удаление разработчика"""
            # Создание нового разработчика
        BM(browser=self.browser).click_on_the_element(selector=self.button_add_new_developer)
        BM(browser=self.browser).enter_text_in_the_element(selector=self.input_name_new_developer, input_text=self.value_name_new_developer) # Вписываю имя разработчика
        BM(browser=self.browser).enter_text_in_the_element(selector=self.input_devid_new_developer, input_text=self.value_devid_new_developer) # Вписываю DevID разработчика
        BM(browser=self.browser).enter_text_in_the_element(selector=self.input_email_new_developer, input_text=self.value_email_new_developer) # Вписываю почту разработчика
        BM(browser=self.browser).click_on_the_element(selector=f"{self.notify_when_a_letter_is_received}/..") # Отключаю "Уведомлять о получении письма"
        BM(browser=self.browser).click_on_the_element(selector=f"{self.тotify_about_the_publication_of_a_letter}/..") # Отключаю "Уведомлять о публикации письма"
        BM(browser=self.browser).click_on_the_element(selector=self.save_button) # Сохраняю
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value="Разработчик успешно добавлен") # Проверяю аллерт
            # Проверка разработчика
        BM(browser=self.browser).page_reload() # Обновляю страницу
        BM(browser=self.browser).checking_the_presence_of_an_element_on_the_page(selector=self.button_add_new_developer) # Проверяю что страница загрузилась
        BM(browser=self.browser).click_on_the_element(selector=self.find_create_developer) # Открываю разработчика на редактирование
        BM(browser=self.browser).checking_the_presence_of_an_element_on_the_page(selector=self.input_name_new_developer) # Проверяю что страница загрузилась
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.input_name_new_developer, second_value=self.value_name_new_developer, atribut='value') # Проверяю имя
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.input_devid_new_developer, second_value=self.value_devid_new_developer, atribut='value') # Проверяю DevID
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.input_email_new_developer, second_value=self.value_email_new_developer, atribut='value') # Проверяю email
            # Редактирую
        BM(browser=self.browser).enter_text_in_the_element(selector=self.input_name_new_developer, input_text=f"t_{self.value_name_new_developer}") # Вписываю имя разработчика
        BM(browser=self.browser).enter_text_in_the_element(selector=self.input_devid_new_developer, input_text=f"t_{self.value_devid_new_developer}") # Вписываю DevID разработчика
        BM(browser=self.browser).enter_text_in_the_element(selector=self.input_email_new_developer, input_text=f"t_{self.value_email_new_developer}") # Вписываю почту разработчика
        BM(browser=self.browser).click_on_the_element(selector=f"{self.notify_when_a_letter_is_received}/..") # Включаю "Уведомлять о получении письма"
        BM(browser=self.browser).click_on_the_element(selector=f"{self.тotify_about_the_publication_of_a_letter}/..") # Включа "Уведомлять о публикации письма"
        BM(browser=self.browser).click_on_the_element(selector=self.save_button) # Сохраняю
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value="Разработчик успешно изменён") # Проверяю аллерт
            # Проверяю
        BM(browser=self.browser).page_reload() # Обновляю страницу
        BM(browser=self.browser).checking_the_presence_of_an_element_on_the_page(selector=self.button_add_new_developer) # Проверяю что страница загрузилась
        BM(browser=self.browser).click_on_the_element(selector=self.find_change_developer) # Открываю разработчика на редактирование
        BM(browser=self.browser).checking_the_presence_of_an_element_on_the_page(selector=self.input_name_new_developer) # Проверяю что страница загрузилась
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.input_name_new_developer, second_value=f"t_{self.value_name_new_developer}", atribut='value') # Проверяю имя
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.input_devid_new_developer, second_value=f"t_{self.value_devid_new_developer}", atribut='value') # Проверяю DevID
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.input_email_new_developer, second_value=f"t_{self.value_email_new_developer}", atribut='value') # Проверяю email
        BM(browser=self.browser).click_on_the_element(selector=self.exit_button)
            # Удаляю разработчика
        BM(browser=self.browser).click_on_the_element(selector= self.find_delete_developer) # Удаление девелопера
        BM(browser=self.browser).click_on_the_element(selector= '//*[@id="developers-delete-dialog-delete-button"]') # Подтверждение удаления
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value="Разработчик удален") # Проверяю аллерт


# -------------------------------------------- Пользователи -----------------------------------------------


# -------------------------------------------- Роли -------------------------------------------------------
class roles_pages:
    # ЭЛЕМЕНТЫ
    roles_link_pages = 'https://mpp-tst-mr1.star.lanit.ru/configuration/roles'                                                      # Страница "Роли"
    name_input = '//*[@id="name-input"]'                                                                                            # Поле ввода Названия роли
    description_input = '//*[@id="description-input"]'                                                                              # Поле ввода Описания роли
    ldap_input = '//*[@id="ldapGroup-input"]'                                                                                       # Поле ввода Группа
    save_button = "//*[text()='Сохранить']"                                                                                         # Поле "Сохранить" разработчика
    exit_button = "//*[text()='Отменить']"                                                                                          # Поле "Отменить" разработчика
    allert_save_text_xpath = '/html/body/div/div[1]/div/div'                                                                        # Поле всплывающего аллерта
    roles_menu_item = '//*[@id="roles-menu-item"]'                                                                                  # Кнопка "Роли" в левом меню настроек

    # ЗНАЧЕНИЯ
    default_role_name = 'control'                                                                                                   # Дефолтное значение названия роли
    default_role_description = 'Контролер эксплуатации'                                                                             # Дефолтное значение описания роли
    test_role_name = 'test_role'                                                                                                    # Тестовое значение названия роли
    test_role_description = 'test_description'                                                                                      # Тестовое значение описания роли


    def __init__(self, browser) -> None:
        self.browser = browser

    def go_to_roles_page(self):
        """Переход на страницу настроек"""
        BM(browser=self.browser).go_to_the_page(link=self.roles_link_pages)

    def crud_roles(self):
        "Изменение роли и проверка"
        #Редактирую Роль "control"
        BM(browser=self.browser).click_on_the_element(selector=f"//*[text()='{self.default_role_name}']/..//*[@aria-label='Редактировать']")
        BM(browser=self.browser).enter_text_in_the_element(selector=self.name_input, input_text=self.test_role_name)
        BM(browser=self.browser).enter_text_in_the_element(selector=self.description_input, input_text=self.test_role_description)
        BM(browser=self.browser).click_on_the_element(selector=self.ldap_input)
        BM(browser=self.browser).click_on_the_element(selector='//body//ul/li[9]')
        BM(browser=self.browser).click_on_the_element(selector=self.save_button)
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value="Роль успешно изменена") # Проверяю аллерт
        BM(browser=self.browser).page_reload()
        # Проверяю корректность отредактированных настроек
        BM(browser=self.browser).checking_the_presence_of_an_element_on_the_page(selector=self.roles_menu_item) # Проверяю что страница загрузилась
        BM(browser=self.browser).click_on_the_element(selector=f"//*[text()='{self.test_role_name}']/..//*[@aria-label='Редактировать']")
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.name_input, second_value=self.test_role_name, atribut='value')
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.description_input, second_value=self.test_role_description, atribut='value')
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.ldap_input, second_value='Test_Manual', atribut='textContent')
        # Возвращаю стандартные настройки
        BM(browser=self.browser).enter_text_in_the_element(selector=self.name_input, input_text=self.default_role_name)
        BM(browser=self.browser).enter_text_in_the_element(selector=self.description_input, input_text=self.default_role_description)
        BM(browser=self.browser).click_on_the_element(selector=self.ldap_input)
        BM(browser=self.browser).click_on_the_element(selector='//body//ul/li[4]')
        BM(browser=self.browser).click_on_the_element(selector=self.save_button)
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.allert_save_text_xpath , second_value="Роль успешно изменена") # Проверяю аллерт
        BM(browser=self.browser).page_reload()
        # Проверяю корректность отредактированных настроек
        BM(browser=self.browser).checking_the_presence_of_an_element_on_the_page(selector=self.roles_menu_item) # Проверяю что страница загрузилась
        BM(browser=self.browser).click_on_the_element(selector=f"//*[text()='{self.default_role_name}']/..//*[@aria-label='Редактировать']")
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.name_input, second_value=self.default_role_name, atribut='value')
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.description_input, second_value=self.default_role_description, atribut='value')
        BM(browser=self.browser).get_element_text_and_compare_with_custom_value(selector=self.ldap_input, second_value='Контролер эксплуатации', atribut='textContent')


# -------------------------------------------- Привелегии -------------------------------------------------







