import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from curl import *
from data import Credential
from utils import *

@pytest.mark.usefixtures("register_new_account")
class TextCheckNewRegistration:
    def test_registration(self):
        driver, email, password = register_new_account

        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.fiel_password).send_keys(password)
        driver.find_element(*Locators.button_entrance).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site


@pytest.mark.usefixtures("start_from_main_not_login")
class TestCheckCreationAccount:
    def test_existing_account(self):
        driver = start_from_main_not_login

        driver.find_element(*Locators.ins_login).click()

        driver.find_element(*Locators.field_name).send_keys(Credential.name)
        driver.find_element(*Locators.field_email).send_keys(Credential.email)
        driver.find_element(*Locators.fiel_password).send_keys(Credential.password)
        driver.find_element(*Locators.button_login).click()

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ins_error_account)) == 'Такой пользователь уже существует'


@pytest.mark.usefixtures("start_from_main_not_login")
class TestCheckRegistrationNotName:
    def test_registration_not_name(self):
        driver = start_from_main_not_login

        driver.find_element(*Locators.ins_login).click()

        email = generate_email()
        password = generate_password()

        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.fiel_password).send_keys(password)
        driver.find_element(*Locators.button_login).click()

        assert driver.current_url == register_site


@pytest.mark.usefixtures("start_from_main_not_login")
class TestCheckErrorPassword:
    def test_error_password(self):
        driver = start_from_main_not_login

        driver.find_element(*Locators.ins_login).click()

        driver.find_element(*Locators.field_name).send_keys(Credential.name)
        driver.find_element(*Locators.field_email).send_keys(Credential.email)
        driver.find_element(*Locators.fiel_password).send_keys(Credential.password)
        driver.find_element(*Locators.button_login).click()

        assert WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ins_error_password)) == 'Некорректный пароль'


@pytest.mark.usefixtures("start_from_main_not_login")
class TestCheckErrorPasswordTwo:
    def test_not_password(self):
        driver = start_from_main_not_login
        email = 'nadya@yandex.ru'

        driver.find_element(*Locators.ins_login).click()

        driver.find_element(*Locators.field_name).send_keys(Credential.name)
        driver.find_element(*Locators.field_email).send_keys(email)
        driver.find_element(*Locators.button_login).click()

        assert driver.current_url == register_site