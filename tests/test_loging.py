from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By


def generate_email_time_stamp():
    time_stamp = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    return f"aziguy{time_stamp}@gmail.com"


def test_login_with_valid_credentials():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    driver.find_element(By.ID, "input-email").send_keys("amotooricap1@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("12345")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    assert driver.find_element(By.LINK_TEXT, "Edit your account information").is_displayed()
    driver.quit()


def test_login_with_invalid_email_and_valid_pwd():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    driver.find_element(By.ID, "input-email").send_keys(generate_email_time_stamp())
    driver.find_element(By.ID, "input-password").send_keys("12345")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    assert driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(
        expected_warning_message
    )
    driver.quit()


def test_login_with_valid_email_and_invalid_pwd():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    driver.find_element(By.ID, "input-email").send_keys("amotooricap1@gmail.com")
    driver.find_element(By.ID, "input-password").send_keys("123450")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    assert driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(
        expected_warning_message
    )
    driver.quit()


def test_login_without_providing_credentials():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    driver.find_element(By.ID, "input-email").send_keys("")
    driver.find_element(By.ID, "input-password").send_keys("")
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    assert driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(
        expected_warning_message
    )
    driver.quit()
