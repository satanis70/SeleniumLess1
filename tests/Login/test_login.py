import pytest
from pages.login_page import LoginPage


@pytest.mark.parametrize("login, password",
                         [
                             ("nik@mail.ru", "123456"),
                             ("name@example.com", "28itji"),
                             ("user1", "password1")
                         ])
def test_successful_login(driver, login, password):
    page = LoginPage(driver)
    page.open()
    page.login(login, password)
    assert page.get_welcome_text() == f"Welcome, {login}!"


@pytest.mark.parametrize("login, password",
                         [
                             ("user1", "password"),
                             ("user1", "password2")
                         ])
def test_login_with_wrong_password(driver, login, password):
    page = LoginPage(driver)
    page.open()
    page.login(login, password)
    assert page.get_error_text() == "Wrong login or password"


@pytest.mark.parametrize("login, password",
                         [
                             ("user", "password1"),
                             ("user2", "password1")
                         ])
def test_login_with_wrong_login(driver, login, password):
    page = LoginPage(driver)
    page.open()
    page.login(login, password)
    assert page.get_error_text() == "Wrong login or password"
