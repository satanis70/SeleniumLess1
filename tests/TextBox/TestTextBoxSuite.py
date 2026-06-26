import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

LOCATOR_USERNAME = "userName"
LOCATOR_USER_EMAIL = "userEmail"
LOCATOR_SUBMIT = "submit"
LOCATOR_CURRENT_ADDRESS = "currentAddress"
LOCATOR_PERMANENT_ADDRESS = "permanentAddress"
LOCATOR_NAME_RESULT = '//*[@id="name"]'
LOCATOR_EMAIL_RESULT = '//*[@id="email"]'
LOCATOR_CURRENT_ADDRESS_RESULT = '/html/body/main/section/div/p[3]'
LOCATOR_PERMANENT_ADDRESS_RESULT = '/html/body/main/section/div/p[4]'
LOCATOR_OUTPUT_CHILDREN = (By.XPATH, "//*[@id='output']/*")
SELECTOR_OUTPUT_NAME = (By.CSS_SELECTOR, "#output #name")
SELECTOR_OUTPUT_EMAIL = (By.CSS_SELECTOR, "#output #email")
SELECTOR_OUTPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
SELECTOR_OUTPUT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")
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

        # 2. Поиск нужных элементов
        fullname_field = driver.find_element(By.ID, LOCATOR_USERNAME)
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

        # 5. Находим текст с результатом
        result_fullname = driver.find_element(By.XPATH, LOCATOR_NAME_RESULT)
        result_email = driver.find_element(By.XPATH, LOCATOR_EMAIL_RESULT)
        result_current_address = driver.find_element(By.XPATH, LOCATOR_CURRENT_ADDRESS_RESULT)
        result_permanent_address = driver.find_element(By.XPATH, LOCATOR_PERMANENT_ADDRESS_RESULT)

        # 6. Находим все элементы с ID через селектор
        output_name_counter = len(driver.find_elements(*SELECTOR_OUTPUT_NAME))
        output_email_counter = len(driver.find_elements(*SELECTOR_OUTPUT_EMAIL))
        output_current_address_counter = len(driver.find_elements(*SELECTOR_OUTPUT_CURRENT_ADDRESS))
        output_permanent_address_counter = len(driver.find_elements(*SELECTOR_OUTPUT_PERMANENT_ADDRESS))

        # 6. Проверка результата
        if scenario_type == "positive":
            assert fullname in result_fullname.text, f"Поле результата fullname пустое или заполнено неверно"
            assert email in result_email.text, f"Поле результата email пустое или заполнено неверно"
            assert current_address in result_current_address.text, f"Поле результата current_address пустое или заполнено неверно"
            assert permanent_address in result_permanent_address.text, f"Поле результата permanent_address пустое или заполнено неверно"
        else:
            assert output_name_counter == 0, f"Элемент Name найден, но его не должно быть"
            assert output_email_counter == 0, f"Элемент Email найден, но его не должно быть"
            assert output_current_address_counter == 0, f"Элемент Current Address найден, но его не должно быть"
            assert output_permanent_address_counter == 0, f"Элемент Permananet Address найден, но его не должно быть"
