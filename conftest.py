import pytest
from selenium import webdriver
from utilities.utils import read_configurations


@pytest.fixture()
def setup_teardown(request):
    browser = read_configurations("basic infos", "browser")
    # driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        raise ValueError("Browser not supported")
    driver.maximize_window()
    url = read_configurations("basic infos", "url")
    driver.get(url)
    request.cls.driver = driver
    yield
    driver.quit()
