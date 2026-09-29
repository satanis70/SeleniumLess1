import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

LOCATOR_LOGIN = "login-input"
LOCATOR_PASSWORD = "password-input"
LOCATOR_SUBMIT_LOGIN = "submit-button"
URL = "https://qa-guru.github.io/one-page-form/login.html"
LOCATOR_RESULT = "error-message"


class TestLoginSuite:

    @pytest.fixture
    def driver(self):
        """Фикстура для инициализации и закрытия браузера."""

        driver = webdriver.Chrome()
        driver.maximize_window()

        yield driver

        driver.quit()

    @staticmethod
    def set_up_and_return_result(driver, login, password, scenario_type, expected_text):
        driver.get(URL)

        # 1. Подготовка ожидания
        wait = WebDriverWait(driver, 10)

        # 2. Поиск элементов формы
        login_field = driver.find_element(By.ID, LOCATOR_LOGIN)
        password_field = driver.find_element(By.ID, LOCATOR_PASSWORD)

        # Явно ожидаем что элемент появился в DOM
        submit_button = wait.until(EC.presence_of_element_located((By.ID, LOCATOR_SUBMIT_LOGIN)))

        # 3. Очищаем поля
        login_field.clear()
        password_field.clear()

        # 4. Заполняем поля
        login_field.send_keys(login)
        password_field.send_keys(password)
        submit_button.click()

        # 5. Находим текст с результатом
        result_element = wait.until(
            EC.visibility_of_element_located((By.ID, LOCATOR_RESULT))
        )
        return result_element.text

    @pytest.mark.parametrize(
        "login, password, scenario_type, expected_text",
        [
            ("nik@mail.ru", "123456", "positive", "Вы успешно вошли"),
            ("name@example.com", "28itji", "positive", "Вы успешно вошли"),
        ]
    )
    def test_login_form_positive(self, driver, login, password, scenario_type, expected_text):
        result_actual = self.set_up_and_return_result(driver, login, password, scenario_type, expected_text)

        # Проверка результата
        assert expected_text in result_actual, f"Ожидался успешный вход, но получено: '{result_actual}'"

    @pytest.mark.parametrize(
        "login, password, scenario_type, expected_text",
        [
            ("im@mail.com", " ", "negative", "Password is required (minimum 6 characters)"),
            (" ", "123456", "negative", "Login is required (minimum 3 characters)"),
            (" ", " ", "negative", "Login and password are required (minimum 3 and 6 characters)"),
            ("1", "123456", "negative", "Login must be at least 3 characters"),
            ("123", "1", "negative", "Password must be at least 6 characters"),
            ("12345678901234567890123456789012345678901234567890", "123456", "negative",
             "Логин должен быть не больше 32 символов")
        ]
    )
    def test_login_form_negative(self, driver, login, password, scenario_type, expected_text):
        result_actual = self.set_up_and_return_result(driver, login, password, scenario_type, expected_text)

        # Проверка результата
        assert expected_text in result_actual, f"Ожидалось '{expected_text}', получено '{result_actual}'"
