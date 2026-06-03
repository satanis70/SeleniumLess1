import time

from selenium import webdriver


def set_up(driver, url):
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)  # Пауза, чтобы визуально заметить открытие

def tear_down(driver):
    driver.quit()