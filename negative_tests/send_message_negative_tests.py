import time
from symtable import Class

from selenium import webdriver
from selenium.webdriver.common.by import By

from helpers import send_message_helper


def check_incorrect_name(names, correct_email):
    for name in names:
        # 1. Запуск браузера Chrome
        driver = send_message_helper.send_message_helper()
        try:
            # 3. Поиск элементов и заполнение полей
            # Находим поле Full Name по его ID и вводим текст
            full_name_field = driver.find_element(By.ID, "userName")
            full_name_field.send_keys(name)

            # Находим поле Email по его ID и вводим текст
            email_field = driver.find_element(By.ID, "userEmail")
            email_field.send_keys(correct_email)

            # Находим кнопку Submit по ее ID и кликаем
            submit_button = driver.find_element(By.ID, "submit")
            submit_button.click()

            # 4. Проверка результата
            time.sleep(5)  # Пауза, чтобы увидеть результат отправки

            output = driver.find_element(By.ID, "output")
            classes = output.get_attribute("class")
            assert "has-content" not in classes
            print(f"Тест для имени '{name}' пройден успешно!")
        except Exception as e:
            print(f"Тест для имени '{name}' упал с ошибкой: {e}")
        finally:
            driver.quit()


def check_incorrect_email(emails, correct_name):
    for email in emails:
        # 1. Запуск браузера Chrome
        driver = send_message_helper.send_message_helper()
        try:
            # 3. Поиск элементов и заполнение полей
            # Находим поле Full Name по его ID и вводим текст
            full_name_field = driver.find_element(By.ID, "userName")
            full_name_field.send_keys(correct_name)

            # Находим поле Email по его ID и вводим текст
            email_field = driver.find_element(By.ID, "userEmail")
            email_field.send_keys(email)

            # Находим кнопку Submit по ее ID и кликаем
            submit_button = driver.find_element(By.ID, "submit")
            submit_button.click()

            # 4. Проверка результата
            time.sleep(5)  # Пауза, чтобы увидеть результат отправки

            output = driver.find_element(By.ID, "output")
            classes = output.get_attribute("class") or ""
            assert "has-content" not in classes
            print(f"Тест для почты '{email}' пройден успешно!")
        except Exception as e:
            print(f"Тест для почты '{email}' упал с ошибкой: {e}")
        finally:
            driver.quit()
