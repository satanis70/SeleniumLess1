import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Локаторы для полей ввода
LOCATOR_USERNAME = "userName"
LOCATOR_USER_EMAIL = "userEmail"
LOCATOR_SUBMIT = "submit"
LOCATOR_CURRENT_ADDRESS = "currentAddress"
LOCATOR_PERMANENT_ADDRESS = "permanentAddress"

# Локаторы для результатов (CSS селекторы)
SELECTOR_OUTPUT_NAME = (By.CSS_SELECTOR, "#output #name")
SELECTOR_OUTPUT_EMAIL = (By.CSS_SELECTOR, "#output #email")
SELECTOR_OUTPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
SELECTOR_OUTPUT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")
SELECTOR_OUTPUT_BLOCK = (By.CSS_SELECTOR, "#output")

URL = "https://qa-guru.github.io/one-page-form/text-box.html"


class TestTextBoxSuite:
    @pytest.fixture
    def driver(self):

        """Фикстура для инициализации и закрытия браузера."""

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)

        yield driver

        driver.quit()

    @pytest.mark.parametrize(
        "fullname, email, current_address, permanent_address, scenario_type",
        [  # --- Позитивные тесты ---
            ("niki", "niki@mail.com", "ул. Ленина д5 кв 15", "ул. Ленина д5 кв 15", "positive"),
            ("Никита", "example@google.com", "г. Москва", "г. Новосибирск", "positive"),
            # --- Негативные тесты ---
            (" ", " ", " ", " ", "negative"),
            ("Никита", "examplegoogle.com", "г. Москва", "г. Новосибирск", "negative"),
        ]
    )
    def test_text_box(self, driver, fullname, email, current_address, permanent_address, scenario_type):

        # 1. Открытие страницы
        driver.get(URL)

        fluent_wait = WebDriverWait(
            driver,
            timeout=10,
            poll_frequency=0.5,
            ignored_exceptions=[NoSuchElementException]
        )

        # 2. Поиск нужных элементов
        fullname_field = fluent_wait.until(EC.visibility_of_element_located((By.ID, LOCATOR_USERNAME)))
        email_field = driver.find_element(By.ID, LOCATOR_USER_EMAIL)
        current_address_field = driver.find_element(By.ID, LOCATOR_CURRENT_ADDRESS)
        permanent_address_field = driver.find_element(By.ID, LOCATOR_PERMANENT_ADDRESS)
        submit_button = driver.find_element(By.ID, LOCATOR_SUBMIT)

        # 3. Очищаем поля
        fullname_field.clear()
        email_field.clear()
        current_address_field.clear()
        permanent_address_field.clear()

        # 4. Заполняем поля
        fullname_field.send_keys(fullname)
        email_field.send_keys(email)
        current_address_field.send_keys(current_address)
        permanent_address_field.send_keys(permanent_address)

        submit_button.click()

        # 5. Разделяем логику для позитивных и негативных тестов
        if scenario_type == "positive":
            # Находим все элементы результата
            result_name = fluent_wait.until(EC.visibility_of_element_located(SELECTOR_OUTPUT_NAME))
            result_email = fluent_wait.until(EC.visibility_of_element_located(SELECTOR_OUTPUT_EMAIL))
            result_current_address = fluent_wait.until(
                EC.visibility_of_element_located(SELECTOR_OUTPUT_CURRENT_ADDRESS))
            result_permanent_address = fluent_wait.until(
                EC.visibility_of_element_located(SELECTOR_OUTPUT_PERMANENT_ADDRESS))

            # Проверяем что данные совпадают
            assert fullname in result_name.text, f"Ожидалось '{fullname}', получено '{result_name.text}'"
            assert email in result_email.text, f"Ожидалось '{email}, получено '{result_email.text}'"
            assert current_address in result_current_address.text, f"Ожидалось '{current_address}, получено '{result_current_address.text}'"
            assert permanent_address in result_permanent_address.text, f"Ожидалось '{permanent_address}, получено '{result_permanent_address.text}'"

        else:
            # Негативные
            name_elements = driver.find_elements(*SELECTOR_OUTPUT_NAME)
            email_elements = driver.find_elements(*SELECTOR_OUTPUT_EMAIL)
            current_address_elements = driver.find_elements(*SELECTOR_OUTPUT_CURRENT_ADDRESS)
            permanent_address_elements = driver.find_elements(*SELECTOR_OUTPUT_PERMANENT_ADDRESS)

            assert len(name_elements) == 0, "Элемент Name найден, но его не должно быть"
            assert len(email_elements) == 0, "Элемент Email найден, но его не должно быть"
            assert len(current_address_elements) == 0, "Элемент Current Address найден, но его не должно быть"
            assert len(permanent_address_elements) == 0, "Элемент Permanent Address найден, но его не должно быть"
