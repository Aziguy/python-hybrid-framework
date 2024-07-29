import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from utilities.utils import read_configurations


@pytest.fixture()
def setup_teardown(request):
    browser = read_configurations("basic infos", "browser")
    global driver
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


@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test", attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep
