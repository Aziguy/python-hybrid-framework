from selenium.webdriver.common.by import By

from pages.account_success_page import AccountSuccessPage


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

    first_name_field_id = "input-firstname"
    last_name_field_id = "input-lastname"
    email_field_id = "input-email"
    telephone_field_id = "input-telephone"
    password_field_id = "input-password"
    confirm_password_field_id = "input-confirm"
    agree_field_name = "agree"
    continue_button_xpath = "//input[@value='Continue']"
    yes_radio_button_xpath = "//input[@name='newsletter'][@value='1']"
    duplicate_email_warning_xpath = "//div[@id='account-register']/div[1]"
    privacy_policy_warning_xpath = "//div[@id='account-register']/div[1]"
    first_name_warning_xpath = "//input[@id='input-firstname']/following-sibling::div"
    last_name_warning_xpath = "//input[@id='input-lastname']/following-sibling::div"
    email_warning_xpath = "//input[@id='input-email']/following-sibling::div"
    telephone_warning_xpath = "//input[@id='input-telephone']/following-sibling::div"
    password_warning_xpath = "//input[@id='input-password']/following-sibling::div"

    def enter_first_name(self, first_name_text):
        self.driver.find_element(By.ID, self.first_name_field_id).click()
        self.driver.find_element(By.ID, self.first_name_field_id).clear()
        self.driver.find_element(By.ID, self.first_name_field_id).send_keys(first_name_text)

    def enter_last_name(self, last_name_text):
        self.driver.find_element(By.ID, self.last_name_field_id).click()
        self.driver.find_element(By.ID, self.last_name_field_id).clear()
        self.driver.find_element(By.ID, self.last_name_field_id).send_keys(last_name_text)

    def enter_email(self, email_text):
        self.driver.find_element(By.ID, self.email_field_id).click()
        self.driver.find_element(By.ID, self.email_field_id).clear()
        self.driver.find_element(By.ID, self.email_field_id).send_keys(email_text)

    def enter_telephone(self, telephone_text):
        self.driver.find_element(By.ID, self.telephone_field_id).click()
        self.driver.find_element(By.ID, self.telephone_field_id).clear()
        self.driver.find_element(By.ID, self.telephone_field_id).send_keys(telephone_text)

    def enter_password(self, password_text):
        self.driver.find_element(By.ID, self.password_field_id).click()
        self.driver.find_element(By.ID, self.password_field_id).clear()
        self.driver.find_element(By.ID, self.password_field_id).send_keys(password_text)

    def enter_password_confirm(self, password_text):
        self.driver.find_element(By.ID, self.confirm_password_field_id).click()
        self.driver.find_element(By.ID, self.confirm_password_field_id).clear()
        self.driver.find_element(By.ID, self.confirm_password_field_id).send_keys(password_text)

    def select_agree_checkbox_field(self):
        self.driver.find_element(By.NAME, self.agree_field_name).click()

    def click_on_continue_button(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()
        return AccountSuccessPage(self.driver)

    def select_yes_radio_button(self):
        self.driver.find_element(By.XPATH, self.yes_radio_button_xpath).click()

    def register_an_account(self, **user_data):
        field_methods = {
            'first_name': self.enter_first_name,
            'last_name': self.enter_last_name,
            'email': self.enter_email,
            'telephone': self.enter_telephone,
            'password': self.enter_password,
            'password_confirm': self.enter_password_confirm,
        }

        for field, method in field_methods.items():
            if field in user_data:
                method(user_data[field])

        if user_data.get('yes_or_no') == 'yes':
            self.select_yes_radio_button()

        if user_data.get('privacy_policy') == 'select':
            self.select_agree_checkbox_field()

        return self.click_on_continue_button()

    def retrieve_duplicate_email_warning(self):
        return self.driver.find_element(By.XPATH, self.duplicate_email_warning_xpath).text

    def retrieve_privacy_policy_warning(self):
        return self.driver.find_element(By.XPATH, self.privacy_policy_warning_xpath).text

    def retrieve_first_name_warning(self):
        return self.driver.find_element(By.XPATH, self.first_name_warning_xpath).text

    def retrieve_last_name_warning(self):
        return self.driver.find_element(By.XPATH, self.last_name_warning_xpath).text

    def retrieve_email_warning(self):
        return self.driver.find_element(By.XPATH, self.email_warning_xpath).text

    def retrieve_telephone_warning(self):
        return self.driver.find_element(By.XPATH, self.telephone_warning_xpath).text

    def retrieve_password_warning(self):
        return self.driver.find_element(By.XPATH, self.password_warning_xpath).text

    def verify_all_warnings(self, **expected_warnings):
        warning_types = ['privacy_policy', 'first_name', 'last_name', 'email', 'telephone', 'password']

        actual_warnings = {
            warning_type: getattr(self, f'retrieve_{warning_type}_warning')() for warning_type in warning_types
        }

        for warning_type, expected_warning in expected_warnings.items():
            actual_warning = actual_warnings.get(warning_type)
            if warning_type == 'privacy_policy':
                if expected_warning not in actual_warning:
                    return False
            elif expected_warning != actual_warning:
                return False

        return True
