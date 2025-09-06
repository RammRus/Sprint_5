import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from curl import *
from data import Credential
from utils import *


class TestChapterBread:
    def test_check_chapter_bread(self, start_from_login_page):
        driver = start_from_login_page
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ins_sauce)).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ins_bred)).click()

        active = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.active_section))
        assert active.is_displayed()

        active_tab = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.active_section))
        assert "Булки" in active_tab.text


class TestChapterFillings:
    def test_check_chapter_fillings(self, start_from_login_page):
        driver = start_from_login_page

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ins_fillings)).click()

        active = WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.active_section))
        assert "Начинки" in active.text


class TestChapterSauce:
    def test_check_chapter_sauce(self, start_from_login_page):
        driver = start_from_login_page

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ins_sauce)).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Locators.active_section)).is_displayed()
        active = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.active_section))
        
        assert "Соусы" in active.text