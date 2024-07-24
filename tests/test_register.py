from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('setup_teardown')
class TestRegister:
    @staticmethod
    def generate_email_time_stamp():
        time_stamp = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        return f"aziguy{time_stamp}@gmail.com"

    def test_create_account_with_mandatory_fields(self):
        self.driver.find_element(By.XPATH, '//span[text()="My Account"]').click()
        self.driver.find_element(By.LINK_TEXT, 'Register').click()
        self.driver.find_element(By.ID, 'input-firstname').send_keys('Aziguy')
        self.driver.find_element(By.ID, 'input-lastname').send_keys('HERNANDEZ')
        self.driver.find_element(By.ID, 'input-email').send_keys(self.generate_email_time_stamp())
        self.driver.find_element(By.ID, 'input-telephone').send_keys('0123456789')
        self.driver.find_element(By.ID, 'input-password').send_keys('12345')
        self.driver.find_element(By.ID, 'input-confirm').send_keys('12345')
        self.driver.find_element(By.NAME, 'agree').click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
        expected_text = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_text)

    def test_create_account_with_all_fields(self):
        self.driver.find_element(By.XPATH, '//span[text()="My Account"]').click()
        self.driver.find_element(By.LINK_TEXT, 'Register').click()
        self.driver.find_element(By.ID, 'input-firstname').send_keys('Aziguy')
        self.driver.find_element(By.ID, 'input-lastname').send_keys('HERNANDEZ')
        self.driver.find_element(By.ID, 'input-email').send_keys(self.generate_email_time_stamp())
        self.driver.find_element(By.ID, 'input-telephone').send_keys('0123456789')
        self.driver.find_element(By.ID, 'input-password').send_keys('12345')
        self.driver.find_element(By.ID, 'input-confirm').send_keys('12345')
        self.driver.find_element(By.XPATH, '//input[@value="Continue"]').click()
        self.driver.find_element(By.NAME, 'agree').click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
        expected_text = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_text)

    def test_create_account_with_duplicate_email(self):
        self.driver.find_element(By.XPATH, '//span[text()="My Account"]').click()
        self.driver.find_element(By.LINK_TEXT, 'Register').click()
        self.driver.find_element(By.ID, 'input-firstname').send_keys('Aziguy')
        self.driver.find_element(By.ID, 'input-lastname').send_keys('HERNANDEZ')
        self.driver.find_element(By.ID, 'input-email').send_keys("amotooricap1@gmail.com")
        self.driver.find_element(By.ID, 'input-telephone').send_keys('0123456789')
        self.driver.find_element(By.ID, 'input-password').send_keys('12345')
        self.driver.find_element(By.ID, 'input-confirm').send_keys('12345')
        self.driver.find_element(By.XPATH, '//input[@value="Continue"]').click()
        self.driver.find_element(By.NAME, 'agree').click()
        self.driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
        expected_warning_message = "Warning: E-Mail Address is already registered!"
        assert self.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text.__contains__(
            expected_warning_message
        )

    def test_create_account_without_any_fields(self):
        self.driver.find_element(By.XPATH, '//span[text()="My Account"]').click()
        self.driver.find_element(By.LINK_TEXT, 'Register').click()
        self.driver.find_element(By.ID, 'input-firstname').send_keys('')
        self.driver.find_element(By.ID, 'input-lastname').send_keys('')
        self.driver.find_element(By.ID, 'input-email').send_keys("")
        self.driver.find_element(By.ID, 'input-telephone').send_keys('')
        self.driver.find_element(By.ID, 'input-password').send_keys('')
        self.driver.find_element(By.ID, 'input-confirm').send_keys('')
        self.driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
        expected_privacy_policy_warning_message = "Warning: You must agree to the Privacy Policy!"
        assert self.driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text.__contains__(
            expected_privacy_policy_warning_message
        )
        expected_firstname_warning_message = "First Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-firstname']/following-sibling::div").text.__eq__(
            expected_firstname_warning_message
        )
        expected_lastname_warning_message = "Last Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-lastname']/following-sibling::div").text.__eq__(
            expected_lastname_warning_message
        )
        expected_email_warning_message = "E-Mail Address does not appear to be valid!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-email']/following-sibling::div").text.__eq__(
            expected_email_warning_message
        )
        expected_telephone_warning_message = "Telephone must be between 3 and 32 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-telephone']/following-sibling::div").text.__eq__(
            expected_telephone_warning_message
        )
        expected_password_warning_message = "Password must be between 4 and 20 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-password']/following-sibling::div").text.__eq__(
            expected_password_warning_message
        )
