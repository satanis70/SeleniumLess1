import time

from selenium import webdriver


def send_message_helper():
    driver = webdriver.Chrome()
    driver.get("https://qa-guru.github.io/one-page-form/text-box.html")
    driver.maximize_window()
    time.sleep(5)  # Пауза, чтобы визуально заметить открытие
    return driver