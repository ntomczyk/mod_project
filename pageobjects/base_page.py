from typing import Annotated
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class BasePage:

    """Class with base general selenium methods for interacting with web elements, loading pages etc."""

    SELECT_OPTIONS = (By.CSS_SELECTOR, "option")

    def __init__(self, driver):
        self.driver = driver

    # this function opens given page, BASE_URL is defined in .modivo.env
    def open_page(self, url: str):
        self.driver.get(url)

    # this function checks visibility, finds and returns element
    def find(self, locator: Annotated[tuple, "WebElement"], time_in_s=10):
        return WebDriverWait(self.driver, time_in_s).until(
            EC.visibility_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    # this function finds and returns elements
    def find_elements(self, locator: Annotated[tuple, "WebElement"], time_in_s=10):
        return WebDriverWait(self.driver, time_in_s).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )

    # this function checks if the web element is clickable and click on it
    def click_on(self, locator: Annotated[tuple, "WebElement"], time_in_s=10):
        self.element_is_visible(locator)
        return (
            WebDriverWait(self.driver, time_in_s)
            .until(
                EC.element_to_be_clickable(locator),
                message=f"Can't find elements by locator {locator}",
            )
            .click()
        )

    # this function finds element and clear the text
    def clear(self, locator: Annotated[tuple, "WebElement"], time_in_s=15):
        WebDriverWait(self.driver, time_in_s).until(
            EC.visibility_of_element_located(locator),
            message=f"Can't find elements by locator {locator}",
        ).clear()

    # this function finds element and  passes text to element
    def enter_text(
        self, locator: Annotated[tuple, "WebElement"], text: str, time_in_s=15
    ):
        return (
            WebDriverWait(self.driver, time_in_s)
            .until(
                EC.visibility_of_element_located(locator),
                message=f"Can't find elements by locator {locator}",
            )
            .send_keys(text)
        )

    # this function checks if the web element is visible
    def element_is_visible(self, locator: Annotated[tuple, "WebElement"], time_in_s=10):
        return WebDriverWait(self.driver, time_in_s).until(
            EC.visibility_of_element_located(locator),
            message=f"Can't find elements by locator {locator}",
        )

    # this function checks if the web element is not visible
    def element_is_not_visible(
        self, locator: Annotated[tuple, "WebElement"], time_in_s=10
    ):
        return WebDriverWait(self.driver, time_in_s).until(
            EC.invisibility_of_element_located(locator),
            message=f"Element with locator {locator} exist",
        )

    # this function get text from element
    def get_text_of(self, locator: Annotated[tuple, "WebElement"], time_in_s=10):
        return (
            WebDriverWait(self.driver, time_in_s)
            .until(
                EC.visibility_of_element_located(locator),
                message=f"Can't find elements by locator {locator}",
            )
            .text
        )

    # this function switches to given iframe
    def switch_to_iframe(self, locator: Annotated[tuple, "WebElement"], time_in_s=10):
        WebDriverWait(self.driver, time_in_s).until(
            EC.frame_to_be_available_and_switch_to_it(locator),
            message=f"Can't find iframe by locator {locator}",
        )

    # this function locates the list and select element from the list by value
    def select_by_visible_text(
        self, locator: Annotated[tuple, "WebElement"], text: str, time_in_s=15
    ):
        WebDriverWait(self.driver, time_in_s).until(
            EC.presence_of_all_elements_located(self.SELECT_OPTIONS)
        )
        select_element = Select(self.find(locator))
        select_element.select_by_visible_text(text)

    # this function finds elements and return value css property e.g."font-size" ->16px
    def value_of_property(self, locator: Annotated[tuple, "WebElement"], property_of_element: str):
        element = self.find(locator)
        return element.get_property(property_of_element)

    # this function wait for loading new page
    def wait_for_page_loading(self, current_url: str, time_in_s=15):
        WebDriverWait(self.driver, time_in_s).until(
            EC.url_changes(current_url),
            message=f"Page wasn't loading, current url is:  {current_url}",
        )

    # this function wait for url matches
    def wait_for_expected_url(self, expected_url: str, time_in_s=15):
        WebDriverWait(self.driver, time_in_s).until(
            EC.url_to_be(expected_url),
            message=f"Url not matches, expected url is:  {expected_url}",
        )

    # this function checks if the web element is visible and depend of result return True of False
    def check_if_exists(self, locator: Annotated[tuple, "WebElement"], time_in_seconds):
        try:
            WebDriverWait(self.driver, time_in_seconds).until(
                EC.visibility_of_element_located(locator),
                message=f"Can't find element by locator {locator}",
            )
        except TimeoutException:
            return False
        return True

    # this function gets value of given attribute of web element
    def value_of_attribute(self, locator: Annotated[tuple, "WebElement"], attribute: str):
        return (
            WebDriverWait(self.driver, 15)
            .until(
                EC.visibility_of_element_located(locator),
                message=f"Can't find elements by locator {locator}",
            )
            .get_attribute(attribute)
        )
