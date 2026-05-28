import time

from selenium.webdriver.common.by import By

from helpers import send_message_helper


def check_correct_name(name, correct_email):
    for correct_name in name:
        # 1. Запуск браузера Chrome
        driver = send_message_helper.send_message_helper()
        try:
            # 3. Поиск элементов и заполнение полей
            # Находим поле Full Name по его ID и вводим текст
            full_name_field = driver.find_element(By.ID, "userName")
            full_name_field.send_keys(correct_name)

            # Находим поле Email по его ID и вводим текст
            email_field = driver.find_element(By.ID, "userEmail")
            email_field.send_keys(correct_email)

            # Находим кнопку Submit по ее ID и кликаем
            submit_button = driver.find_element(By.ID, "submit")
            submit_button.click()

            # 4. Проверка результата
            time.sleep(5)  # Пауза, чтобы увидеть результат отправки

            # Находим блок с отправленными данными
            result_box = driver.find_element(By.ID, "output")

            # Проверяем, что в блоке результата появился введенный текст
            assert correct_name in result_box.text
            print(f"Тест для имени '{correct_name}' успешно пройден!")
        except Exception as e:
            print(f"Тест для имени '{correct_name}' упал с ошибкой: {e}")
        finally:
            driver.quit()


def check_correct_current_address(current_address, correct_name, correct_email):
    for correct_current_address in current_address:
        # 1. Запуск браузера Chrome
        driver = send_message_helper.send_message_helper()
        try:
            # 3. Поиск элементов и заполнение полей
            # Находим поле Full Name по его ID и вводим текст
            full_name_field = driver.find_element(By.ID, "userName")
            full_name_field.send_keys(correct_name)

            # Находим поле Email по его ID и вводим текст
            email_field = driver.find_element(By.ID, "userEmail")
            email_field.send_keys(correct_email)

            # Находим поле Current Address по его ID и вводим текст
            current_address_field = driver.find_element(By.ID, "currentAddress")
            current_address_field.send_keys(correct_current_address)

            # Находим кнопку Submit по ее ID и кликаем
            submit_button = driver.find_element(By.ID, "submit")
            submit_button.click()

            # 4. Проверка результата
            time.sleep(5)  # Пауза, чтобы увидеть результат отправки

            # Находим блок с отправленными данными
            result_box = driver.find_element(By.ID, "output")
            assert correct_current_address in result_box.text
            print(f"Тест для Current Address {correct_current_address} успешно пройден!")
        except Exception as e:
            print(f"Тест для Current Address {correct_current_address} упал с ошибкой {e}")
        finally:
            driver.quit()
