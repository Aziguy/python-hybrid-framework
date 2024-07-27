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
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account(
            first_name='Aziguy',
            last_name='HERNANDEZ',
            email=generate_email_time_stamp(),
            telephone='0123456789',
            password='secure_password',
            password_confirm='secure_password',
            yes_or_no='no',
            privacy_policy='select',
        )
        expected_text = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_creation_message().__eq__(expected_text)

    def test_create_account_with_all_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        account_success_page = register_page.register_an_account(
            first_name='Aziguy',
            last_name='HERNANDEZ',
            email=generate_email_time_stamp(),
            telephone='0123456789',
            password='secure_password',
            password_confirm='secure_password',
            yes_or_no='yes',
            privacy_policy='select',
        )
        expected_text = "Your Account Has Been Created!"
        assert account_success_page.retrieve_account_creation_message().__eq__(expected_text)

    def test_create_account_with_duplicate_email(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account(
            first_name='Aziguy',
            last_name='HERNANDEZ',
            email='amotooricap1@gmail.com',
            telephone='0123456789',
            password='secure_password',
            password_confirm='secure_password',
            yes_or_no='no',
            privacy_policy='select',
        )
        expected_warning_message = "Warning: E-Mail Address is already registered!"
        assert register_page.retrieve_duplicate_email_warning().__contains__(expected_warning_message)

    def test_register_without_entering_any_fields(self):
        home_page = HomePage(self.driver)
        register_page = home_page.navigate_to_register_page()
        register_page.register_an_account(
            first_name='',
            last_name='',
            email='',
            telephone='',
            password='',
            password_confirm='',
            yes_or_no='no',
            privacy_policy='no',
        )

        assert register_page.verify_all_warnings(
            privacy_policy="Warning: You must agree to the Privacy Policy!",
            first_name="First Name must be between 1 and 32 characters!",
            last_name="Last Name must be between 1 and 32 characters!",
            email="E-Mail Address does not appear to be valid!",
            telephone="Telephone must be between 3 and 32 characters!",
            password="Password must be between 4 and 20 characters!",
        )
