from data import Urls
from helpers import click, login, wait_visible
from locators import (
    ForgotPasswordPageLocators,
    HeaderLocators,
    LoginPageLocators,
    MainPageLocators,
    RegisterPageLocators,
)


class TestLogin:

    def test_login_via_login_to_account_button_on_main_page(self, driver, registered_user):
        driver.get(Urls.MAIN)
        click(driver, MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON)
        wait_visible(driver, LoginPageLocators.TITLE)
        login(driver, registered_user["email"], registered_user["password"])
        assert driver.find_element(*MainPageLocators.PLACE_ORDER_BUTTON).is_displayed()

    def test_login_via_personal_account_button(self, driver, registered_user):
        driver.get(Urls.MAIN)
        click(driver, HeaderLocators.PERSONAL_ACCOUNT_LINK)
        wait_visible(driver, LoginPageLocators.TITLE)
        login(driver, registered_user["email"], registered_user["password"])
        assert driver.find_element(*MainPageLocators.PLACE_ORDER_BUTTON).is_displayed()

    def test_login_via_link_in_registration_form(self, driver, registered_user):
        driver.get(Urls.REGISTER)
        click(driver, RegisterPageLocators.LOGIN_LINK)
        wait_visible(driver, LoginPageLocators.TITLE)
        login(driver, registered_user["email"], registered_user["password"])
        assert driver.find_element(*MainPageLocators.PLACE_ORDER_BUTTON).is_displayed()

    def test_login_via_link_in_forgot_password_form(self, driver, registered_user):
        driver.get(Urls.FORGOT_PASSWORD)
        wait_visible(driver, ForgotPasswordPageLocators.TITLE)
        click(driver, ForgotPasswordPageLocators.LOGIN_LINK)
        wait_visible(driver, LoginPageLocators.TITLE)
        login(driver, registered_user["email"], registered_user["password"])
        assert driver.find_element(*MainPageLocators.PLACE_ORDER_BUTTON).is_displayed()
