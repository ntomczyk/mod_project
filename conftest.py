import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


# It helps to add properties to junit xml report
def pytest_collection_modifyitems(items):
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
        options.add_argument("--lang=os.getenv('BROWSER_CHROME_LANG')")
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    else:
        print("Run test in headless mode: --headless")
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument(
            "--ignore-certificate-errors --whitelisted-ips --disable-dev-shm-usage --no-sandbox --disable-notifications"
        )
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--lang=os.getenv('BROWSER_CHROME_LANG')")
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        # TO DO - there can be another browsers

    driver.set_page_load_timeout(30)
    driver.maximize_window()
    request.cls.driver = driver
    # TO DO - there can be screenshots only for failed tests
    yield driver
    driver.quit()
