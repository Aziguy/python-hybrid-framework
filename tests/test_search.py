import pytest
from selenium.webdriver.common.by import By
from pages.home_page import HomePage
from pages.search_page import SearchPage


@pytest.mark.usefixtures('setup_teardown')
class TestSearch:

    def test_search_for_valid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field("HP")
        home_page.click_on_search_button()
        search_page = SearchPage(self.driver)
        assert search_page.display_status_of_valid_product()

    def test_search_for_invalid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field("Honda")
        home_page.click_on_search_button()
        expected_text = 'There is no product that matches the search criteria.'
        search_page = SearchPage(self.driver)
        assert search_page.retrieve_no_product_message().__eq__(expected_text)

    def test_search_for_without_fill_any_product_terms(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field("Honda")
        home_page.click_on_search_button()
        expected_text = 'There is no product that matches the search criteria.'
        search_page = SearchPage(self.driver)
        assert search_page.retrieve_no_product_message().__eq__(expected_text)
