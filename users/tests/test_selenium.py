from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture()
def test_browser():
    chrome_browser = webdriver.Chrome()
    return chrome_browser


# def test_registration(test_browser):
#     email = "AutoTest@gmail.com"
#     username = "AutoTest"
#     password1 = "AutoTest123."
#     password2 = password1
#
#     register_url = 'http://127.0.0.1:8000/users/register'
#     test_browser.get(register_url)
#
#     email_field = test_browser.find_element(By.ID, value="id_email")
#     username_field = test_browser.find_element(By.ID, value="id_username")
#     password1_field = test_browser.find_element(By.ID, value="id_password1")
#     password2_field = test_browser.find_element(By.ID, value="id_password2")
#
#     email_field.send_keys(email)
#     username_field.send_keys(username)
#     password1_field.send_keys(password1)
#     password2_field.send_keys(password2)
#
#     register_button = test_browser.find_element(By.CLASS_NAME, value="button")
#     register_button.click()
#
#
# def test_login(test_browser):
#     email = "AutoTest@gmail.com"
#     password = "AutoTest123."
#     login_url = 'http://127.0.0.1:8000/users/login/'
#     test_browser.get(login_url)
#     email_field = test_browser.find_element(By.ID, value="id_username")
#     password_field = test_browser.find_element(By.ID, value="id_password")
#
#     email_field.send_keys(email)
#     password_field.send_keys(password)
#
#     login_button = test_browser.find_element(By.CLASS_NAME, value="button")
#     assert not login_button.get_attribute("disabled")
#
#     login_button.click()
