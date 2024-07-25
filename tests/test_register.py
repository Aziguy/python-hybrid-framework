import pytest
from selenium.webdriver.common.by import By

from pages.account_success_page import AccountSuccessPage
from pages.home_page import HomePage
from pages.register_page import RegisterPage
from utilities.utils import generate_email_time_stamp


@pytest.mark.usefixtures('setup_teardown')
class TestRegister:

    def test_create_account_with_mandatory_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_register_option()
        register_page = RegisterPage(self.driver)
        register_page.enter_first_name('Aziguy')
        register_page.enter_last_name('HERNANDEZ')
        register_page.enter_email(generate_email_time_stamp())
        register_page.enter_telephone('0123456789')
        register_page.enter_password('12345')
        register_page.enter_password_confirm('12345')
        register_page.select_agree_checkbox_field()
        register_page.click_on_continue_button()
        expected_text = "Your Account Has Been Created!"
        account_success_page = AccountSuccessPage(self.driver)
        assert account_success_page.retrieve_account_creation_message().__eq__(expected_text)

    def test_create_account_with_all_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_register_option()
        register_page = RegisterPage(self.driver)
        register_page.enter_first_name('Aziguy')
        register_page.enter_last_name('HERNANDEZ')
        register_page.enter_email(generate_email_time_stamp())
        register_page.enter_telephone('0123456789')
        register_page.enter_password('12345')
        register_page.enter_password_confirm('12345')
        register_page.select_yes_radio_button()
        register_page.select_agree_checkbox_field()
        register_page.click_on_continue_button()
        expected_text = "Your Account Has Been Created!"
        account_success_page = AccountSuccessPage(self.driver)
        assert account_success_page.retrieve_account_creation_message().__eq__(expected_text)

    def test_create_account_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_register_option()
        register_page = RegisterPage(self.driver)
        register_page.enter_first_name('Aziguy')
        register_page.enter_last_name('HERNANDEZ')
        register_page.enter_email("amotooricap1@gmail.com")
        register_page.enter_telephone('0123456789')
        register_page.enter_password('12345')
        register_page.enter_password_confirm('12345')
        register_page.select_agree_checkbox_field()
        register_page.click_on_continue_button()
        expected_warning_message = "Warning: E-Mail Address is already registered!"
        assert register_page.retrieve_duplicate_email_warning().__contains__(expected_warning_message)

    def test_create_account_without_any_fields(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.select_register_option()
        register_page = RegisterPage(self.driver)
        register_page.enter_first_name('')
        register_page.enter_last_name('')
        register_page.enter_email('')
        register_page.enter_telephone('')
        register_page.enter_password('')
        register_page.enter_password_confirm('')
        register_page.click_on_continue_button()
        expected_privacy_policy_warning_message = "Warning: You must agree to the Privacy Policy!"
        assert register_page.retrieve_privacy_policy_warning().__contains__(expected_privacy_policy_warning_message)
        expected_firstname_warning_message = "First Name must be between 1 and 32 characters!"
        assert register_page.retrieve_first_name_warning().__contains__(expected_firstname_warning_message)
        expected_lastname_warning_message = "Last Name must be between 1 and 32 characters!"
        assert register_page.retrieve_last_name_warning().__contains__(expected_lastname_warning_message)
        expected_email_warning_message = "E-Mail Address does not appear to be valid!"
        assert register_page.retrieve_email_warning().__contains__(expected_email_warning_message)
        expected_telephone_warning_message = "Telephone must be between 3 and 32 characters!"
        assert register_page.retrieve_telephone_warning().__contains__(expected_telephone_warning_message)
        expected_password_warning_message = "Password must be between 4 and 20 characters!"
        assert register_page.retrieve_password_warning().__contains__(expected_password_warning_message)
