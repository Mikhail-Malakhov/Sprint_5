import random
import string
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import TIMEOUT, Urls, UserData
from locators import CommonLocators, LoginPageLocators, MainPageLocators, RegisterPageLocators

CURRENT_TAB_CLASS = "tab_tab_type_current"  # Класс, который получает выбранная вкладка конструктора


# ---------- Генераторы данных ----------

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


def generate_user_data():
    """Возвращает данные нового пользователя: имя, логин (email) и пароль."""
    return {"name": generate_name(), "email": generate_email(), "password": generate_password()}


# ---------- Ожидания и действия ----------

def wait_visible(driver, locator):
    return WebDriverWait(driver, TIMEOUT).until(EC.visibility_of_element_located(locator))


def click(driver, locator):
    """Ждёт, пока исчезнет оверлей загрузки и элемент станет кликабельным, затем кликает."""
    WebDriverWait(driver, TIMEOUT).until(EC.invisibility_of_element_located(CommonLocators.MODAL_OVERLAY))
    WebDriverWait(driver, TIMEOUT).until(EC.element_to_be_clickable(locator)).click()


def fill(driver, locator, text):
    field = wait_visible(driver, locator)
    field.clear()
    field.send_keys(text)


class tab_has_current_class:
    """Условие ожидания: у вкладки есть класс tab_tab_type_current, и он держится stable_for секунд.

    После клика по вкладке список ингредиентов плавно прокручивается, и подсветка
    по пути переходит через соседние вкладки. Поэтому ждём, пока прокрутка закончится.
    """

    def __init__(self, locator, stable_for=1.0):
        self.locator = locator
        self.stable_for = stable_for
        self.since = None

    def __call__(self, driver):
        tab = driver.find_element(*self.locator)
        if CURRENT_TAB_CLASS not in tab.get_attribute("class"):
            self.since = None
            return False
        if self.since is None:
            self.since = time.monotonic()
        return tab if time.monotonic() - self.since >= self.stable_for else False


def open_constructor_tab(driver, locator):
    """Кликает по вкладке конструктора и возвращает её элемент после того, как она стала выбранной."""
    click(driver, locator)
    return WebDriverWait(driver, TIMEOUT, poll_frequency=0.2).until(
        tab_has_current_class(locator),
        message="Вкладка конструктора не стала выбранной",
    )


# ---------- Сценарии ----------

def register_user(driver, name, email, password):
    """Регистрирует пользователя через форму и ждёт перехода на страницу входа."""
    driver.get(Urls.REGISTER)
    fill(driver, RegisterPageLocators.NAME_INPUT, name)
    fill(driver, RegisterPageLocators.EMAIL_INPUT, email)
    fill(driver, RegisterPageLocators.PASSWORD_INPUT, password)
    click(driver, RegisterPageLocators.REGISTER_BUTTON)
    WebDriverWait(driver, TIMEOUT).until(EC.url_to_be(Urls.LOGIN))


def register_new_user(driver):
    """Генерирует данные, регистрирует нового пользователя и возвращает его данные."""
    user = generate_user_data()
    register_user(driver, **user)
    return user


def login(driver, email, password):
    """Заполняет форму входа (страница входа уже открыта) и ждёт главную для авторизованного пользователя."""
    fill(driver, LoginPageLocators.EMAIL_INPUT, email)
    fill(driver, LoginPageLocators.PASSWORD_INPUT, password)
    click(driver, LoginPageLocators.LOGIN_BUTTON)
    wait_visible(driver, MainPageLocators.PLACE_ORDER_BUTTON)
