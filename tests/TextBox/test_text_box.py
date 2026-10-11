import pytest
from pages.text_box_page import TextBoxPage


@pytest.mark.parametrize(
    "fullname, email, current_address, permanent_address",
    [
        ("niki", "niki@mail.com", "ул. Ленина д5 кв 15", "ул. Ленина д5 кв 15"),
        ("Никита", "example@google.com", "г. Москва", "г. Новосибирск")
    ]
)
def test_successful_submit(driver, fullname, email, current_address, permanent_address):
    page = TextBoxPage(driver)
    page.open()
    page.text_box(fullname, email, current_address, permanent_address)
    assert fullname in page.get_output_name()
    assert email in page.get_output_email()
    assert current_address in page.get_output_current_address()
    assert permanent_address in page.get_output_permanent_address()


@pytest.mark.parametrize(
    "fullname, email, current_address, permanent_address",
    [
        ("niki", "nikimail.com", "ул. Ленина д5 кв 15", "ул. Ленина д5 кв 15"),
        ("Никита", "example@@google.com", "г. Москва", "г. Новосибирск")
    ]
)
def test_submit_with_invalid_email(driver, fullname, email, current_address, permanent_address):
    page = TextBoxPage(driver)
    page.open()
    page.text_box(fullname, email, current_address, permanent_address)
    name_elements = page.find_output_name_elements()
    email_elements = page.find_output_email_elements()
    current_address_elements = page.find_output_current_address_elements()
    permanent_address_elements = page.find_output_permanent_address_elements()
    output_children = page.find_output_children()
    assert len(name_elements) == 0
    assert len(output_children) == 0
    assert len(email_elements) == 0
    assert len(current_address_elements) == 0
    assert len(permanent_address_elements) == 0
