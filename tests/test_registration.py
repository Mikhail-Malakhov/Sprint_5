from data import Urls
from helpers import click, fill, generate_password, login, register_user, wait_visible
from locators import LoginPageLocators, MainPageLocators, RegisterPageLocators


class TestRegistration:

    def test_registration_with_valid_data_success(self, driver, new_user):
        register_user(driver, **new_user)
        wait_visible(driver, LoginPageLocators.TITLE)
        # Проверяем, что новым аккаунтом можно войти
        login(driver, new_user["email"], new_user["password"])
        assert driver.find_element(*MainPageLocators.PLACE_ORDER_BUTTON).is_displayed()

    def test_registration_with_short_password_shows_error(self, driver, new_user):
        driver.get(Urls.REGISTER)
        fill(driver, RegisterPageLocators.NAME_INPUT, new_user["name"])
        fill(driver, RegisterPageLocators.EMAIL_INPUT, new_user["email"])
        fill(driver, RegisterPageLocators.PASSWORD_INPUT, generate_password(5))
        click(driver, RegisterPageLocators.REGISTER_BUTTON)
        error = wait_visible(driver, RegisterPageLocators.PASSWORD_ERROR)
        assert error.text == "Некорректный пароль"
