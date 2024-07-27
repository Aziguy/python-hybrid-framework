from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.search_page import SearchPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    search_box_field_name = 'search'
    search_button_xpath = '//button[contains(@class, "btn-default")]'
    my_account_drop_menu_xpath = "//span[text()='My Account']"
    login_option_link_text = "Login"
    register_option_link_text = "Register"

    def enter_product_into_search_box_field(self, product_name):
        self.driver.find_element(By.NAME, self.search_box_field_name).click()
        self.driver.find_element(By.NAME, self.search_box_field_name).clear()
        self.driver.find_element(By.NAME, self.search_box_field_name).send_keys(product_name)

    def click_on_search_button(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()
        return SearchPage(self.driver)

    def click_on_my_account_drop_menu(self):
        self.driver.find_element(By.XPATH, self.my_account_drop_menu_xpath).click()

    def select_login_option(self):
        self.driver.find_element(By.LINK_TEXT, self.login_option_link_text).click()
        return LoginPage(self.driver)

    def select_register_option(self):
        self.driver.find_element(By.LINK_TEXT, self.register_option_link_text).click()
        return RegisterPage(self.driver)

    def search_for_a_product(self, product_name):
        self.enter_product_into_search_box_field(product_name)
        return self.click_on_search_button()

    def navigate_to_login_page(self):
        self.click_on_my_account_drop_menu()
        return self.select_login_option()

    def navigate_to_register_page(self):
        self.click_on_my_account_drop_menu()
        return self.select_register_option()
