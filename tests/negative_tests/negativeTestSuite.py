import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from helpers.send_message_helper import tear_down, set_up
from util.config import LOCATOR_USERNAME, LOCATOR_USER_EMAIL, LOCATOR_SUBMIT, LOCATOR_OUTPUT, INCORRECT_NAMES, \
    CORRECT_EMAIL, INCORRECT_EMAILS, CORRECT_NAME


class NegativeTestSuite:
    def __init__(self, url):
        self.url = url

    def check_incorrect_name(self):
        for name in INCORRECT_NAMES:
            driver = webdriver.Chrome()
            # 1. Запуск браузера Chrome
            set_up(driver, self.url)
            try:
                # 3. Поиск элементов и заполнение полей
                # Находим поле Full Name по его ID и вводим текст
                full_name_field = driver.find_element(By.ID, LOCATOR_USERNAME)
                full_name_field.send_keys(name)

                # Находим поле Email по его ID и вводим текст
                email_field = driver.find_element(By.ID, LOCATOR_USER_EMAIL)
                email_field.send_keys(CORRECT_EMAIL)

                # Находим кнопку Submit по ее ID и кликаем
                submit_button = driver.find_element(By.ID, LOCATOR_SUBMIT)
                submit_button.click()

                # 4. Проверка результата
                time.sleep(5)  # Пауза, чтобы увидеть результат отправки

                output = driver.find_element(By.ID, LOCATOR_OUTPUT)
                output.find_element(By.ID,"name")
                raise AssertionError(f"Тест для '{name}' упал с ошибкой")
            except NoSuchElementException:
                print(f"Тест для {name} пройден")
                pass
            except AssertionError as e:
                print(f"Ошибка {e}")
            finally:
                tear_down(driver)


    def check_incorrect_email(self):
        for email in INCORRECT_EMAILS:
            driver = webdriver.Chrome()
            # 1. Запуск браузера Chrome
            set_up(driver, self.url)
            try:
                # 3. Поиск элементов и заполнение полей
                # Находим поле Full Name по его ID и вводим текст
                full_name_field = driver.find_element(By.ID, LOCATOR_USERNAME)
                full_name_field.send_keys(CORRECT_NAME)

                # Находим поле Email по его ID и вводим текст
                email_field = driver.find_element(By.ID, LOCATOR_USER_EMAIL)
                email_field.send_keys(email)

                # Находим кнопку Submit по ее ID и кликаем
                submit_button = driver.find_element(By.ID, LOCATOR_SUBMIT)
                submit_button.click()

                # 4. Проверка результата
                time.sleep(5)  # Пауза, чтобы увидеть результат отправки

                output = driver.find_element(By.ID, LOCATOR_OUTPUT)
                output.find_element(By.ID, "email")
                raise AssertionError (f"Тест для '{email}' упал с ошибкой")
            except NoSuchElementException:
                print(f"Тест для {email} пройден")
                pass
            except AssertionError as e:
                print(f"Ошибка {e}")
            finally:
                tear_down(driver)
