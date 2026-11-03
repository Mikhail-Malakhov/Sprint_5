from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import TIMEOUT, Urls
from helpers import click, wait_visible
from locators import HeaderLocators, LoginPageLocators, MainPageLocators, ProfilePageLocators


class TestPersonalAccount:

    def test_go_to_personal_account_by_click_on_personal_account_button(self, logged_in_driver):
        driver = logged_in_driver
        click(driver, HeaderLocators.PERSONAL_ACCOUNT_LINK)
        WebDriverWait(driver, TIMEOUT).until(EC.url_to_be(Urls.PROFILE))
        assert wait_visible(driver, ProfilePageLocators.PROFILE_LINK).is_displayed()

    def test_go_from_personal_account_to_constructor_by_constructor_button(self, logged_in_driver):
        driver = logged_in_driver
        click(driver, HeaderLocators.PERSONAL_ACCOUNT_LINK)
        wait_visible(driver, ProfilePageLocators.PROFILE_LINK)
        click(driver, HeaderLocators.CONSTRUCTOR_LINK)
        assert wait_visible(driver, MainPageLocators.CONSTRUCTOR_TITLE).is_displayed()

    def test_go_from_personal_account_to_constructor_by_logo(self, logged_in_driver):
        driver = logged_in_driver
        click(driver, HeaderLocators.PERSONAL_ACCOUNT_LINK)
        wait_visible(driver, ProfilePageLocators.PROFILE_LINK)
        click(driver, HeaderLocators.LOGO)
        assert wait_visible(driver, MainPageLocators.CONSTRUCTOR_TITLE).is_displayed()

    def test_logout_by_logout_button_in_personal_account(self, logged_in_driver):
        driver = logged_in_driver
        click(driver, HeaderLocators.PERSONAL_ACCOUNT_LINK)
        click(driver, ProfilePageLocators.LOGOUT_BUTTON)
        WebDriverWait(driver, TIMEOUT).until(EC.url_to_be(Urls.LOGIN))
        assert wait_visible(driver, LoginPageLocators.TITLE).is_displayed()
