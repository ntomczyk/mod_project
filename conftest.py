import os
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


# It helps to add properties to junit xml report
def pytest_collection_modifyitems(session, config, items):
    for item in items:
        for marker in item.iter_markers(name="test_id"):
            test_id = marker.args[0]
            item.user_properties.append(("test_id", test_id))


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome-headless",
        help="Type in browser name e.g. chrome:  ",
    )


# Fixture for starting and closing session for all test, as default tests run in chrome browser in headless mode
@pytest.fixture()
def setup(request) -> webdriver:
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        print("Run test in Chrome browser: --chrome")
        options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    elif browser == "firefox":
        print("Run test in Firefox browser: --firefox")
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        print("Run test in headless mode: --headless")
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument(
            "--ignore-certificate-errors --whitelisted-ips --disable-dev-shm-usage --no-sandbox --disable-notifications"
        )
        options.add_argument("--lang=pl")
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    driver.set_page_load_timeout(10)
    driver.maximize_window()
    request.cls.driver = driver
    before_failed = request.session.testsfailed
    yield driver
    if request.session.testsfailed != before_failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Test failed",
            attachment_type=AttachmentType.PNG,
        )
    driver.quit()
