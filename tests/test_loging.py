from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures('setup_teardown')
class TestLoging:
    @staticmethod
    def generate_email_time_stamp():
        time_stamp = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
        return f"aziguy{time_stamp}@gmail.com"

    def test_login_with_valid_credentials(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "input-email").send_keys("amotooricap1@gmail.com")
        self.driver.find_element(By.ID, "input-password").send_keys("12345")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        assert self.driver.find_element(By.LINK_TEXT, "Edit your account information").is_displayed()

    def test_login_with_invalid_email_and_valid_pwd(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "input-email").send_keys(self.generate_email_time_stamp())
        self.driver.find_element(By.ID, "input-password").send_keys("12345")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(
            expected_warning_message
        )

    def test_login_with_valid_email_and_invalid_pwd(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "input-email").send_keys("amotooricap1@gmail.com")
        self.driver.find_element(By.ID, "input-password").send_keys("123450")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(
            expected_warning_message
        )

    def test_login_without_providing_credentials(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "input-email").send_keys("")
        self.driver.find_element(By.ID, "input-password").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(
            expected_warning_message
        )
