from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By


def generate_email_time_stamp():
    time_stamp = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    return f"aziguy{time_stamp}@gmail.com"


def test_create_account_with_mandatory_fields():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH, '//span[text()="My Account"]').click()
    driver.find_element(By.LINK_TEXT, 'Register').click()
    driver.find_element(By.ID, 'input-firstname').send_keys('Aziguy')
    driver.find_element(By.ID, 'input-lastname').send_keys('HERNANDEZ')
    driver.find_element(By.ID, 'input-email').send_keys(generate_email_time_stamp())
    driver.find_element(By.ID, 'input-telephone').send_keys('0123456789')
    driver.find_element(By.ID, 'input-password').send_keys('12345')
    driver.find_element(By.ID, 'input-confirm').send_keys('12345')
    driver.find_element(By.NAME, 'agree').click()
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
    expected_text = "Your Account Has Been Created!"
    assert driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_text)
    driver.quit()


def test_create_account_with_all_fields():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH, '//span[text()="My Account"]').click()
    driver.find_element(By.LINK_TEXT, 'Register').click()
    driver.find_element(By.ID, 'input-firstname').send_keys('Aziguy')
    driver.find_element(By.ID, 'input-lastname').send_keys('HERNANDEZ')
    driver.find_element(By.ID, 'input-email').send_keys(generate_email_time_stamp())
    driver.find_element(By.ID, 'input-telephone').send_keys('0123456789')
    driver.find_element(By.ID, 'input-password').send_keys('12345')
    driver.find_element(By.ID, 'input-confirm').send_keys('12345')
    driver.find_element(By.XPATH, '//input[@value="Continue"]').click()
    driver.find_element(By.NAME, 'agree').click()
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
    expected_text = "Your Account Has Been Created!"
    assert driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_text)
    driver.quit()


def test_create_account_with_duplicate_email():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH, '//span[text()="My Account"]').click()
    driver.find_element(By.LINK_TEXT, 'Register').click()
    driver.find_element(By.ID, 'input-firstname').send_keys('Aziguy')
    driver.find_element(By.ID, 'input-lastname').send_keys('HERNANDEZ')
    driver.find_element(By.ID, 'input-email').send_keys("amotooricap1@gmail.com")
    driver.find_element(By.ID, 'input-telephone').send_keys('0123456789')
    driver.find_element(By.ID, 'input-password').send_keys('12345')
    driver.find_element(By.ID, 'input-confirm').send_keys('12345')
    driver.find_element(By.XPATH, '//input[@value="Continue"]').click()
    driver.find_element(By.NAME, 'agree').click()
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
    expected_warning_message = "Warning: E-Mail Address is already registered!"
    assert driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text.__contains__(
        expected_warning_message
    )
    driver.quit()


def test_create_account_without_any_fields():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH, '//span[text()="My Account"]').click()
    driver.find_element(By.LINK_TEXT, 'Register').click()
    driver.find_element(By.ID, 'input-firstname').send_keys('')
    driver.find_element(By.ID, 'input-lastname').send_keys('')
    driver.find_element(By.ID, 'input-email').send_keys("")
    driver.find_element(By.ID, 'input-telephone').send_keys('')
    driver.find_element(By.ID, 'input-password').send_keys('')
    driver.find_element(By.ID, 'input-confirm').send_keys('')
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
    expected_privacy_policy_warning_message = "Warning: You must agree to the Privacy Policy!"
    assert driver.find_element(By.XPATH, "//div[@id='account-register']/div[1]").text.__contains__(
        expected_privacy_policy_warning_message
    )
    expected_firstname_warning_message = "First Name must be between 1 and 32 characters!"
    assert driver.find_element(By.XPATH, "//input[@id='input-firstname']/following-sibling::div").text.__eq__(
        expected_firstname_warning_message
    )
    expected_lastname_warning_message = "Last Name must be between 1 and 32 characters!"
    assert driver.find_element(By.XPATH, "//input[@id='input-lastname']/following-sibling::div").text.__eq__(
        expected_lastname_warning_message
    )
    expected_email_warning_message = "E-Mail Address does not appear to be valid!"
    assert driver.find_element(By.XPATH, "//input[@id='input-email']/following-sibling::div").text.__eq__(
        expected_email_warning_message
    )
    expected_telephone_warning_message = "Telephone must be between 3 and 32 characters!"
    assert driver.find_element(By.XPATH, "//input[@id='input-telephone']/following-sibling::div").text.__eq__(
        expected_telephone_warning_message
    )
    expected_password_warning_message = "Password must be between 4 and 20 characters!"
    assert driver.find_element(By.XPATH, "//input[@id='input-password']/following-sibling::div").text.__eq__(
        expected_password_warning_message
    )
    driver.quit()
