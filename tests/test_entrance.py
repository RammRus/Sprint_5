import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from curl import *
from data import Credential


class TestButtonExit:

    def test_check_login_out(self, start_from_login_page):
        driver = start_from_login_page

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ins_bred))

        driver.find_element(*Locators.button_personal).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ins_profile))

        driver.find_element(*Locators.button_exit).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(login_site))

        assert driver.current_url == login_site


class TestMainButton:
    def test_check_entrance_by_button(self, start_from_site_not_login):
        driver = start_from_site_not_login

        driver.find_element(*Locators.entrance_on_the_main).click()

        driver.find_element(*Locators.field_email).send_keys(Credential.email)
        driver.find_element(*Locators.fiel_password).send_keys(Credential.password)
        driver.find_element(*Locators.button_entrance).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site


class TestCheckRegister:
    
    def test_login_password(self, start_from_recovery_page):
        driver = start_from_recovery_page

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ins_bred))
 
        assert driver.current_url == main_site


class TestCheckEntranceFromRecoveryPage:
    def test_button_inscription_login(self, start_from_main_not_login):
        driver = start_from_main_not_login

        driver.find_element(*Locators.ins_login).click()
        driver.find_element(*Locators.ins_button_entrance).click()
        driver.find_element(*Locators.field_email).send_keys(Credential.email)
        driver.find_element(*Locators.fiel_password).send_keys(Credential.password)
        driver.find_element(*Locators.button_entrance).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site

