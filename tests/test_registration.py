from data import Urls
from helpers import (
    click,
    fill,
    generate_email,
    generate_name,
    generate_password,
    generate_user_data,
    login,
    register_user,
    wait_visible,
)
from locators import LoginPageLocators, MainPageLocators, RegisterPageLocators


class TestRegistration:

    def test_registration_with_valid_data_success(self, driver):
        user = generate_user_data()
        register_user(driver, **user)
        wait_visible(driver, LoginPageLocators.TITLE)
        # Проверяем, что новым аккаунтом можно войти
        login(driver, user["email"], user["password"])
        assert driver.find_element(*MainPageLocators.PLACE_ORDER_BUTTON).is_displayed()

    def test_registration_with_short_password_shows_error(self, driver):
        driver.get(Urls.REGISTER)
        fill(driver, RegisterPageLocators.NAME_INPUT, generate_name())
        fill(driver, RegisterPageLocators.EMAIL_INPUT, generate_email())
        fill(driver, RegisterPageLocators.PASSWORD_INPUT, generate_password(5))
        click(driver, RegisterPageLocators.REGISTER_BUTTON)
        error = wait_visible(driver, RegisterPageLocators.PASSWORD_ERROR)
        assert error.text == "Некорректный пароль"
