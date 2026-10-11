from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    URL = "https://qa-guru.github.io/one-page-form/login.html"
    LOGIN_INPUT = (By.ID, "login-input")
    PASSWORD_INPUT = (By.ID, "password-input")
    SUBMIT_BUTTON = (By.ID, "submit-button")
    ERROR_MESSAGE = (By.ID, "error-message")
    SUCCESS_PANEL = (By.ID, "success-panel")
    WELCOME_MESSAGE = (By.ID, "welcome-message")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)
        return self

    def login(self, login, password):
        login_field = self.wait.until(expected_conditions.visibility_of_element_located(self.LOGIN_INPUT))
        password_field = self.wait.until(expected_conditions.visibility_of_element_located(self.PASSWORD_INPUT))

        login_field.clear()
        login_field.send_keys(login)

        password_field.clear()
        password_field.send_keys(password)

        self.wait.until(expected_conditions.visibility_of_element_located(self.SUBMIT_BUTTON)).click()

        return self

    def get_welcome_text(self):
        element = self.wait.until(
            expected_conditions.visibility_of_element_located(self.WELCOME_MESSAGE)
        )
        return element.text

    def get_error_text(self):
        return self.wait.until(expected_conditions.visibility_of_element_located(self.ERROR_MESSAGE)).text
