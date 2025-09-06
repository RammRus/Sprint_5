import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from curl import *
from data import Credential
from utils import *

class TestTransitionByConstructor:
    def test_transition_by_constructor(self, start_from_main_page):
        driver = start_from_main_page
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        driver.find_element(*Locators.button_personal).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.button_const))

        driver.find_element(*Locators.button_const).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site


class TestTransitionByLogo:
    def test_transition_by_logo(self, start_from_login_page):
        driver = start_from_login_page
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.button_personal))

        driver.find_element(*Locators.button_personal).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ins_profile))

        driver.find_element(*Locators.logo).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(main_site))

        assert driver.current_url == main_site


class TestCgeckingPageProfile:
    def test_transition_before_profile(self, start_from_login_page):
        driver = start_from_login_page
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ins_bred))

        driver.find_element(*Locators.button_personal).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(profile_site))

        assert driver.current_url == profile_site