from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    return chrome_browser


def test_registration():
    email = "AutoTest@gmail.com"
    username = "AutoTest"
    password1 = "AutoTest123."
    password2 = password1
    login_url = 'http://127.0.0.1:8000/users/login/'
    email_field = browser.find_element(By.ID, value="id_username")
    password1_field = browser.find_element(By.ID, value="id_password1")
    password2_field = browser.find_element(By.ID, value="id_password2")
    email_field.send_keys(email)
    password1_field.send_keys(password1)
    password2_field.send_keys(password1)


def test_login(browser):
    email = "AutoTest@gmail.com"
    password = "AutoTest123."
    login_url = 'http://127.0.0.1:8000/users/login/'
    browser.get(login_url)
    email_field = browser.find_element(By.ID, value="id_username")
    password_field = browser.find_element(By.ID, value="id_password")

    email_field.send_keys(email)
    password_field.send_keys(password)

    login_button = browser.find_element(By.CLASS_NAME, value="button")

    login_button.click()
