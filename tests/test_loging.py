import pytest
from selenium.webdriver.common.by import By

from pages.account_page import AccountPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utilities.utils import generate_email_time_stamp


@pytest.mark.usefixtures('setup_teardown')
class TestLoging:

    def test_login_with_valid_credentials(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_login_option()
        login_page = LoginPage(self.driver)
        login_page.enter_email_address("amotooricap1@gmail.com")
        login_page.enter_password("12345")
        login_page.click_on_login_button()
        account_page = AccountPage(self.driver)
        assert account_page.display_status_of_edit_your_account_information_option()

    def test_login_with_invalid_email_and_valid_pwd(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_login_option()
        login_page = LoginPage(self.driver)
        login_page.enter_email_address(generate_email_time_stamp())
        login_page.enter_password("12345")
        login_page.click_on_login_button()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)

    def test_login_with_valid_email_and_invalid_pwd(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_login_option()
        login_page = LoginPage(self.driver)
        login_page.enter_email_address("amotooricap1@gmail.com")
        login_page.enter_password("123450")
        login_page.click_on_login_button()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)

    def test_login_without_providing_credentials(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_login_option()
        login_page = LoginPage(self.driver)
        login_page.enter_email_address("")
        login_page.enter_password("")
        login_page.click_on_login_button()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert login_page.retrieve_warning_message().__contains__(expected_warning_message)
