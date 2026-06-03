import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from helpers import send_message_helper
from helpers.send_message_helper import tear_down, set_up
from util.config import CORRECT_NAMES, LOCATOR_USERNAME, LOCATOR_USER_EMAIL, LOCATOR_SUBMIT, LOCATOR_OUTPUT, \
    CORRECT_ADDRESSES, LOCATOR_CURRENT_ADDRESS, CORRECT_EMAIL, CORRECT_NAME


class PositiveTestSuite:
    def __init__(self, url):
        self.url = url

    def check_correct_name(self):
        for correct_name in CORRECT_NAMES:
            driver = webdriver.Chrome()
            # 1. Запуск браузера Chrome
            set_up(driver, self.url)
            try:
                # 3. Поиск элементов и заполнение полей
                # Находим поле Full Name по его ID и вводим текст
                full_name_field = driver.find_element(By.ID, LOCATOR_USERNAME)
                full_name_field.send_keys(correct_name)

                # Находим поле Email по его ID и вводим текст
                email_field = driver.find_element(By.ID, LOCATOR_USER_EMAIL)
                email_field.send_keys(CORRECT_EMAIL)

                # Находим кнопку Submit по ее ID и кликаем
                submit_button = driver.find_element(By.ID, LOCATOR_SUBMIT)
                submit_button.click()

                # 4. Проверка результата
                time.sleep(5)  # Пауза, чтобы увидеть результат отправки

                # Находим блок с отправленными данными
                result_box = driver.find_element(By.ID, LOCATOR_OUTPUT)

                # Проверяем, что в блоке результата появился введенный текст
                assert correct_name in result_box.text
                print(f"Тест для имени '{correct_name}' успешно пройден!")
            except Exception as e:
                print(f"Тест для имени '{correct_name}' упал с ошибкой: {e}")
            finally:
                tear_down(driver)

    def check_correct_current_address(self):
        for correct_current_address in CORRECT_ADDRESSES:
            # 1. Запуск браузера Chrome
            driver = webdriver.Chrome()
            set_up(driver, self.url)
            try:
                # 3. Поиск элементов и заполнение полей
                # Находим поле Full Name по его ID и вводим текст
                full_name_field = driver.find_element(By.ID, LOCATOR_USERNAME)
                full_name_field.send_keys(CORRECT_NAME)

                # Находим поле Email по его ID и вводим текст
                email_field = driver.find_element(By.ID, LOCATOR_USER_EMAIL)
                email_field.send_keys(CORRECT_EMAIL)

                # Находим поле Current Address по его ID и вводим текст
                current_address_field = driver.find_element(By.ID, LOCATOR_CURRENT_ADDRESS)
                current_address_field.send_keys(correct_current_address)

                # Находим кнопку Submit по ее ID и кликаем
                submit_button = driver.find_element(By.ID, LOCATOR_SUBMIT)
                submit_button.click()

                # 4. Проверка результата
                time.sleep(5)  # Пауза, чтобы увидеть результат отправки

                # Находим блок с отправленными данными
                result_box = driver.find_element(By.ID, LOCATOR_OUTPUT)
                assert correct_current_address in result_box.text
                print(f"Тест для Current Address {correct_current_address} успешно пройден!")
            except Exception as e:
                print(f"Тест для Current Address {correct_current_address} упал с ошибкой {e}")
            finally:
                tear_down(driver)
