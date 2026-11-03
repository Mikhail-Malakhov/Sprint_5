import pytest
from selenium import webdriver

from data import Urls
from helpers import login, register_new_user


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="chrome или firefox")


@pytest.fixture
def driver(request):
    """Открывает браузер на главной странице и закрывает его после теста (driver.quit())."""
    browser = request.config.getoption("--browser")
    if browser == "firefox":
        driver = webdriver.Firefox()
    else:
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(Urls.MAIN)
    yield driver
    driver.quit()


@pytest.fixture
def registered_user(driver):
    """Зарегистрированный пользователь (данные генерируются и регистрируются в helpers)."""
    return register_new_user(driver)


@pytest.fixture
def logged_in_driver(driver, registered_user):
    """Браузер с авторизованным пользователем на главной странице."""
    driver.get(Urls.LOGIN)
    login(driver, registered_user["email"], registered_user["password"])
    return driver
