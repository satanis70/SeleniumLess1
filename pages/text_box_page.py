from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TextBoxPage:
    URL = "https://qa-guru.github.io/one-page-form/text-box.html"

    # Локаторы для полей ввода
    LOCATOR_USERNAME = (By.ID, "userName")
    LOCATOR_USER_EMAIL = (By.ID, "userEmail")
    LOCATOR_SUBMIT = (By.ID, "submit")
    LOCATOR_CURRENT_ADDRESS = (By.ID, "currentAddress")
    LOCATOR_PERMANENT_ADDRESS = (By.ID, "permanentAddress")

    # Локаторы для результатов (CSS селекторы)
    OUTPUT_NAME = (By.CSS_SELECTOR, "#output #name")
    OUTPUT_EMAIL = (By.CSS_SELECTOR, "#output #email")
    OUTPUT_CURRENT_ADDRESS = (By.CSS_SELECTOR, "#output #currentAddress")
    OUTPUT_PERMANENT_ADDRESS = (By.CSS_SELECTOR, "#output #permanentAddress")
    OUTPUT_BLOCK = (By.CSS_SELECTOR, "#output")
    OUTPUT_CHILDREN = (By.XPATH, "//*[@id='output']/*")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(
            self.driver,
            timeout=10,
            poll_frequency=0.5,
            ignored_exceptions=[NoSuchElementException]
        )

    def open(self):
        self.driver.get(self.URL)
        return self

    def text_box(self, username, email, current_address, permanent_address):
        full_name_field = self.wait.until(expected_conditions.visibility_of_element_located(self.LOCATOR_USERNAME))
        email_field = self.wait.until(expected_conditions.visibility_of_element_located(self.LOCATOR_USER_EMAIL))
        current_address_field = self.wait.until(
            expected_conditions.visibility_of_element_located(self.LOCATOR_CURRENT_ADDRESS))
        permanent_address_field = self.wait.until(
            expected_conditions.visibility_of_element_located(self.LOCATOR_PERMANENT_ADDRESS))

        full_name_field.clear()
        full_name_field.send_keys(username)

        email_field.clear()
        email_field.send_keys(email)

        current_address_field.clear()
        current_address_field.send_keys(current_address)

        permanent_address_field.clear()
        permanent_address_field.send_keys(permanent_address)

        self.wait.until(expected_conditions.visibility_of_element_located(self.LOCATOR_SUBMIT)).click()

        return self

    def get_output_block(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.OUTPUT_BLOCK))

    def get_output_name(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.OUTPUT_NAME)).text

    def get_output_email(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.OUTPUT_EMAIL)).text

    def get_output_current_address(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.OUTPUT_CURRENT_ADDRESS)).text

    def get_output_permanent_address(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.OUTPUT_PERMANENT_ADDRESS)).text

    def find_output_name_elements(self):
        return self.driver.find_elements(*self.OUTPUT_NAME)

    def find_output_email_elements(self):
        return self.driver.find_elements(*self.OUTPUT_EMAIL)

    def find_output_current_address_elements(self):
        return self.driver.find_elements(*self.OUTPUT_CURRENT_ADDRESS)

    def find_output_permanent_address_elements(self):
        return self.driver.find_elements(*self.OUTPUT_PERMANENT_ADDRESS)

    def find_output_children(self):
        return self.driver.find_elements(*self.OUTPUT_CHILDREN)
