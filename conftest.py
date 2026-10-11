import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    """Фикстура для инициализации и закрытия браузера."""
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()
