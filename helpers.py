import random
import string
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import TIMEOUT, Urls, UserData
from locators import LoginPageLocators, MainPageLocators, RegisterPageLocators


def generate_email():
    """Генерирует уникальный логин (email) вида имя_фамилия_когорта_3цифры@домен."""
    digits = random.randint(100, 999)
    return f"{UserData.NAME}_{UserData.SURNAME}_{UserData.COHORT}_{digits}@{UserData.DOMAIN}"


def generate_password(length=8):
    """Генерирует пароль заданной длины (по умолчанию 8 символов, минимум для сервиса — 6)."""
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))


def generate_name():
    """Генерирует непустое имя пользователя."""
    return "Тест" + "".join(random.choice(string.ascii_lowercase) for _ in range(5))


def wait_visible(driver, locator):
    return WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located(locator))


def click(driver, locator):
    WebDriverWait(driver, TIMEOUT).until(EC.element_to_be_clickable(locator)).click()


def fill(driver, locator, text):
    field = wait_visible(driver, locator)
    field.clear()
    field.send_keys(text)


class active_tab_is_stable:
    """Условие ожидания: активная вкладка конструктора равна expected и держится stable_for секунд.

    После клика по вкладке список ингредиентов плавно прокручивается, и подсветка вкладок
    по пути «пролетает» через соседние разделы. Поэтому ждём окончания прокрутки.
    """

    def __init__(self, expected, stable_for=1.0):
        self.expected = expected
        self.stable_for = stable_for
        self.since = None

    def __call__(self, driver):
        text = driver.find_element(*MainPageLocators.ACTIVE_TAB).text
        if text != self.expected:
            self.since = None
            return False
        if self.since is None:
            self.since = time.monotonic()
        return time.monotonic() - self.since >= self.stable_for


def get_active_tab_after_scroll(driver, expected):
    """Ждёт, пока активной стабильно станет вкладка expected, и возвращает текст активной вкладки."""
    WebDriverWait(driver, TIMEOUT, poll_frequency=0.2).until(
        active_tab_is_stable(expected),
        message=f"Вкладка «{expected}» не стала активной",
    )
    return driver.find_element(*MainPageLocators.ACTIVE_TAB).text


def register_user(driver, name, email, password):
    """Регистрирует пользователя через форму и ждёт перехода на страницу входа."""
    driver.get(Urls.REGISTER)
    fill(driver, RegisterPageLocators.NAME_INPUT, name)
    fill(driver, RegisterPageLocators.EMAIL_INPUT, email)
    fill(driver, RegisterPageLocators.PASSWORD_INPUT, password)
    click(driver, RegisterPageLocators.REGISTER_BUTTON)
    WebDriverWait(driver, TIMEOUT).until(EC.url_to_be(Urls.LOGIN))


def login(driver, email, password):
    """Заполняет форму входа (страница входа уже открыта) и ждёт главную для авторизованного пользователя."""
    fill(driver, LoginPageLocators.EMAIL_INPUT, email)
    fill(driver, LoginPageLocators.PASSWORD_INPUT, password)
    click(driver, LoginPageLocators.LOGIN_BUTTON)
    wait_visible(driver, MainPageLocators.PLACE_ORDER_BUTTON)
