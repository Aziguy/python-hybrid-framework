import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('setup_teardown')
class TestSearch:

    def test_search_for_valid_product(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://tutorialsninja.com/demo/')
        self.driver.find_element(By.NAME, 'search').send_keys('HP')
        self.driver.find_element(By.XPATH, '//button[contains(@class, "btn-default")]').click()
        assert self.driver.find_element(By.LINK_TEXT, 'HP LP3065').is_displayed()

    def test_search_for_invalid_product(self):
        self.driver.find_element(By.NAME, 'search').send_keys('Honda')
        self.driver.find_element(By.XPATH, '//button[contains(@class, "btn-default")]').click()
        expected_text = 'There is no product that matches the search criteria.'
        assert self.driver.find_element(By.XPATH, '//input[@id="button-search"]/following-sibling::p').text.__eq__(
            expected_text
        )

    def test_search_for_without_fill_any_product_terms(self):
        self.driver.find_element(By.NAME, 'search').send_keys('')
        self.driver.find_element(By.XPATH, '//button[contains(@class, "btn-default")]').click()
        expected_text = 'There is no product that matches the search criteria.'
        assert self.driver.find_element(
            By.XPATH, '//input[@id="button-search"]/following-sibling::p'
        ).text.__contains__(expected_text)
