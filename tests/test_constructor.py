from helpers import CURRENT_TAB_CLASS, open_constructor_tab
from locators import MainPageLocators


class TestConstructor:

    def test_go_to_buns_section(self, driver):
        # «Булки» выбраны по умолчанию, поэтому сначала переходим на другую вкладку
        open_constructor_tab(driver, MainPageLocators.SAUCES_TAB)
        tab = open_constructor_tab(driver, MainPageLocators.BUNS_TAB)
        assert CURRENT_TAB_CLASS in tab.get_attribute("class")

    def test_go_to_sauces_section(self, driver):
        tab = open_constructor_tab(driver, MainPageLocators.SAUCES_TAB)
        assert CURRENT_TAB_CLASS in tab.get_attribute("class")

    def test_go_to_fillings_section(self, driver):
        tab = open_constructor_tab(driver, MainPageLocators.FILLINGS_TAB)
        assert CURRENT_TAB_CLASS in tab.get_attribute("class")
