import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Локаторы для полей ввода
LOCATOR_FIRST_NAME = "firstName"
LOCATOR_LAST_NAME = "lastName"
LOCATOR_EMAIL = "userEmail"
LOCATOR_GENDER_MALE = "gender-radio-1"
LOCATOR_GENDER_FEMALE = "gender-radio-2"
LOCATOR_GENDER_OTHER = "gender-radio-3"
LOCATOR_USER_NUMBER = "userNumber"
LOCATOR_DATE_OF_BIRTH = "dateOfBirthInput"
LOCATOR_SUBJECT = "subjectsInput"
LOCATOR_HOBBIES_SPORTS = "hobbies-checkbox-1"
LOCATOR_HOBBIES_READING = "hobbies-checkbox-2"
LOCATOR_HOBBIES_MUSIC = "hobbies-checkbox-3"
LOCATOR_CURRENT_ADDRESS = "currentAddress"
LOCATOR_SUBMIT_BUTTON = "submit"
URL = "https://qa-guru.github.io/one-page-form/automation-practice-form.html"


class TestRegistrationForm:

    @pytest.fixture
    def driver(self):
        """Фикстура для инициализации и закрытия браузера."""

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(5)

        yield driver
        driver.quit()

    @pytest.mark.parametrize(
        "first_name,last_name,email,gender, phone_number",
        [
            # --- Позитивные тесты ---
            ("Nikita", "Ermilov", "nikita@mail.ru", LOCATOR_GENDER_FEMALE, "1234567890")
        ]
    )
    def test_registration_form(self, driver, first_name, last_name, email, gender, phone_number):
        # 1. Открытие страницы
        driver.get(URL)

        # 2. Создаем ожидание
        explicit_wait = WebDriverWait(driver, 10)
        # 3. Поиск нужных элементов
        first_name_field = explicit_wait.until(EC.visibility_of_element_located((By.ID, LOCATOR_FIRST_NAME)))
        last_name_field = explicit_wait.until(EC.visibility_of_element_located((By.ID, LOCATOR_LAST_NAME)))
        email_field = explicit_wait.until(EC.visibility_of_element_located((By.ID, LOCATOR_EMAIL)))
        gender_radio = explicit_wait.until(EC.visibility_of_element_located((By.ID, gender)))
        user_number_field = explicit_wait.until(EC.visibility_of_element_located((By.ID, LOCATOR_USER_NUMBER)))
        submit_button = explicit_wait.until(EC.element_to_be_clickable((By.ID, LOCATOR_SUBMIT_BUTTON)))
        # 4. Очищаем поля
        first_name_field.clear()
        last_name_field.clear()
        email_field.clear()
        user_number_field.clear()
        # Убираем баннер
        driver.execute_script("document.getElementById('fixedban')?.remove();")
        # 5. Заполняем поля
        first_name_field.send_keys(first_name)
        last_name_field.send_keys(last_name)
        email_field.send_keys(email)
        gender_radio.click()
        user_number_field.send_keys(phone_number)
        time.sleep(10)
        # 6. Скролим до кнопки submit и кликаем
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_button)
        submit_button.click()




