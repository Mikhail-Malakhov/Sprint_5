from helpers import click, get_active_tab_after_scroll
from locators import MainPageLocators


class TestConstructor:

    def test_go_to_buns_section(self, driver):
        # «Булки» активна по умолчанию, поэтому сначала уходим на другую вкладку
        click(driver, MainPageLocators.SAUCES_TAB)
        get_active_tab_after_scroll(driver, "Соусы")
        click(driver, MainPageLocators.BUNS_TAB)
        assert get_active_tab_after_scroll(driver, "Булки") == "Булки"

    def test_go_to_sauces_section(self, driver):
        click(driver, MainPageLocators.SAUCES_TAB)
        assert get_active_tab_after_scroll(driver, "Соусы") == "Соусы"

    def test_go_to_fillings_section(self, driver):
        click(driver, MainPageLocators.FILLINGS_TAB)
        assert get_active_tab_after_scroll(driver, "Начинки") == "Начинки"
