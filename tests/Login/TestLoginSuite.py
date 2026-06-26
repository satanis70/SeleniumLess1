import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

LOCATOR_LOGIN = "login-input"
LOCATOR_PASSWORD = "password-input"
LOCATOR_SUBMIT_LOGIN = "submit-button"
URL = "https://qa-guru.github.io/one-page-form/login.html"
LOCATOR_RESULT = "error-message"


class TestLoginSuite:

    @pytest.fixture
    def driver(self):
        """Фикстура для инициализации и закрытия браузера."""
        # options = webdriver.ChromeOptions()
        # options.add_argument("--headless")  # Фоновый режим для CI/CD
        # options.add_argument("--window-size=1920,1080")
        # driver = webdriver.Chrome(options=options)

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)

        yield driver

        driver.quit()

    # Реализация DDT подхода через параметризацию pytest
    @pytest.mark.parametrize(
        "login, password, scenario_type, expected_text",
        [
            # ---  ПОЗИТИВНЫЕ СЦЕНАРИИ ---
            ("nik@mail.ru", "123456", "positive", "Вы успешно вошли"),
            ("name@example.com", "28itji", "positive", "Вы успешно вошли"),
            # --- НЕГАТИВНЫЕ СЦЕНАРИИ ---
            ("im@mail.com", " ", "negative", "Заполните поле пароль"),
            (" ", "123456", "negative", "Заполните поле логин"),
            (" ", " ", "negative", "Заполните поля"),
            ("1", "123456", "negative", "Для входа в систему необходимо ввести не менее 3 символов."),
            ("1", "123456", "negative", "Логин должен быть больше 2 символов"),
            ("123", "1", "negative", "Пароль должен быть больше 5 символов"),
            ("12345678901234567890123456789012345678901234567890", "123456", "negative",
             "Логин должен быть не длиньше 32 символов")
        ]
    )
    def test_login_form(self, driver, login, password, scenario_type, expected_text):
        """Тест кейс, принимающий наборы данных (DDT)."""

        # 1. Открытие тестируемой страницы
        driver.get(URL)
        # 2. Поиск элементов формы
        login_field = driver.find_element(By.ID, LOCATOR_LOGIN)
        password_field = driver.find_element(By.ID, LOCATOR_PASSWORD)
        submit_button = driver.find_element(By.ID, LOCATOR_SUBMIT_LOGIN)

        # 3. Очищаем поля
        login_field.clear()
        password_field.clear()

        # 4. Заполняем поля
        login_field.send_keys(login)
        password_field.send_keys(password)
        submit_button.click()
        # 5. Находит текст с результатом
        result_actual = driver.find_element(By.ID, LOCATOR_RESULT).text

        # 6. Проверка результата
        if scenario_type == "positive":
            assert expected_text in result_actual, f"Ожидался успешный вход, но получено: '{result_actual}'"  # "Wrong login or password"
        else:
            assert expected_text in result_actual or driver.current_url != "success_url", \
                f"Форма пропустила некорректные данные: login='{login}', Pass='{password}'"
