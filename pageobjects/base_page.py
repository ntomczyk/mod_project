from typing import Annotated

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementClickInterceptedException


class BasePage:

    """Class with base general selenium methods for interacting with web elements, loading pages etc."""

    SELECT_OPTIONS = (By.CSS_SELECTOR, "option")

    def __init__(self, driver):
        self.driver = driver

    # this function opens given page e.g. (base_url + "#/dashboard"), BASE_URL is defined in .modivo.env
    def open_page(self, url: str):
        self.driver.get(url)

    # this function checks visibility, finds and returns element
    def find(self, locator: Annotated[tuple, 'WebElement'], time_in_s=10):
        return WebDriverWait(self.driver, time_in_s).until(
            EC.visibility_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    # this function checks visibility, finds and returns element
    def send_Keys(self, locator: Annotated[tuple, 'WebElement'], time_in_s=10):
        return WebDriverWait(self.driver, time_in_s).until(
            EC.visibility_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    # this function finds and returns elements
    def find_elements(self, locator: Annotated[tuple, 'WebElement'], time_in_s=10):
        return WebDriverWait(self.driver, time_in_s).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )

    # this function checks if the web element is clickable and click on it
    def click_on(self, locator: Annotated[tuple, 'WebElement'], time_in_s=10):
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
    def clear(self, locator: Annotated[tuple, 'WebElement'], time_in_s=15):
        WebDriverWait(self.driver, time_in_s).until(
            EC.visibility_of_element_located(locator),
            message=f"Can't find elements by locator {locator}",
        ).clear()

    # this function finds element and  passes text to element
    def enter_text(self, locator: Annotated[tuple, 'WebElement'], text: str, time_in_s=15):
        return (
            WebDriverWait(self.driver, time_in_s)
            .until(
                EC.visibility_of_element_located(locator),
                message=f"Can't find elements by locator {locator}",
            )
            .send_keys(text)
        )

    # this function finds element and moves the mouse pointer over this element
    def hover_to(self, locator: Annotated[tuple, 'WebElement'], time_in_s=10):
        element = WebDriverWait(self.driver, time_in_s).until(
            EC.visibility_of_element_located(locator),
            message=f"Can't find elements by locator {locator}",
        )
        ActionChains(self.driver).move_to_element(element).perform()

    # this function checks if the web element is visible or not and returns true or false depending on it's visibility.
    def element_is_visible(self, locator: Annotated[tuple, 'WebElement'], time_in_s=10):
        return WebDriverWait(self.driver, time_in_s).until(
            EC.visibility_of_element_located(locator),
            message=f"Can't find elements by locator {locator}",
        )

    def element_is_not_visible(self, locator: Annotated[tuple, 'WebElement'], time_in_s=10):
        return WebDriverWait(self.driver, time_in_s).until(
            EC.invisibility_of_element_located(locator),
            message=f"Element with locator {locator} exist",
        )

    # this function get text from element
    def get_text_of(self, locator: Annotated[tuple, 'WebElement'], time_in_s=10):
        return (
            WebDriverWait(self.driver, time_in_s)
            .until(
                EC.visibility_of_element_located(locator),
                message=f"Can't find elements by locator {locator}",
            )
            .text
        )

    # this function get text from element
    def get_text_of_all_elements(self, locator: Annotated[tuple, 'WebElement'], time_in_s=15):
        return (
            WebDriverWait(self.driver, time_in_s)
            .until(
                EC.visibility_of_all_elements_located(locator),
                message=f"Can't find elements by locator {locator}",
            )
            .text
        )

    # this function get value of attribute from element
    def value_of_attribute(self, locator: Annotated[tuple, 'WebElement'], attribute: Annotated[str, 'value'], time_in_s=15):
        return (
            WebDriverWait(self.driver, time_in_s)
            .until(
                EC.visibility_of_element_located(locator),
                message=f"Can't find elements by locator {locator}",
            )
            .get_attribute(attribute)
        )

    # this function asserts comparison of a web element's text with passed in text.
    def assert_element_text(self, locator: Annotated[tuple, 'WebElement'], element_text: str, time_in_s=15):
        element = WebDriverWait(self.driver, time_in_s).until(
            EC.visibility_of_element_located(locator),
            message=f"Can't find elements by locator {locator}",
        )
        assert element.text == element_text

    # this function locate the list and select element from the list by value
    def select_by_value(self, locator: Annotated[tuple, 'WebElement'], value: str, time_in_s=15):
        WebDriverWait(self.driver, time_in_s).until(
            EC.presence_of_all_elements_located(self.SELECT_OPTIONS)
        )
        select_element = Select(self.find(locator))
        select_element.select_by_value(value)

    # this function locate the list and select element from the list by value
    def select_by_index(self, locator: Annotated[tuple, 'WebElement'], index: int, time_in_s=15):
        WebDriverWait(self.driver, time_in_s).until(
            EC.presence_of_all_elements_located(self.SELECT_OPTIONS)
        )
        select_element = Select(self.find(locator))
        select_element.select_by_index(index)

    # this function locate the list and select element from the list by value
    def select_by_visible_text(self, locator: Annotated[tuple, 'WebElement'], text: str, time_in_s=15):
        WebDriverWait(self.driver, time_in_s).until(
            EC.presence_of_all_elements_located(self.SELECT_OPTIONS)
        )
        select_element = Select(self.find(locator))
        select_element.select_by_visible_text(text)

    # this function return result, % of whole number
    def percentage(self, percent, whole):
        return (percent * whole) / 100

    # this function finds elements and return value css property e.g."font-size" ->16px
    def value_of_property(self, locator: Annotated[tuple, 'WebElement'], property: str):
        element = self.find(locator)
        return element.get_property(property)

    # this function helps get all the computed style properties of element and return value of given style
    def style_list(self, locator: Annotated[tuple, 'WebElement'], property: str):
        element = self.find(locator)
        styleprops_dict = self.driver.execute_script(
            "var items = {};"
            + "var compsty = getComputedStyle(arguments[0]);"
            + "var len = compsty.length;"
            + "for (index = 0; index < len; index++)"
            + "{items [compsty[index]] = compsty.getPropertyValue(compsty[index])};"
            + "return items;",
            element,
        )
        return styleprops_dict[property]

    # this function wait for loading new page
    def wait_for_page_loading(self, current_url, time_in_s=15):
        WebDriverWait(self.driver, time_in_s).until(
            EC.url_changes(current_url),
            message=f"Page wasn't loading, current url is:  {current_url}",
        )

    # this function wait for url matches
    def wait_for_expected_url(self, expected_url, time_in_s=15):
        WebDriverWait(self.driver, time_in_s).until(
            EC.url_to_be(expected_url),
            message=f"Url not matches, expected url is:  {expected_url}",
        )

    def check_if_exists(self, locator: Annotated[tuple, 'WebElement'], time_in_seconds):
        try:
            WebDriverWait(self.driver, time_in_seconds).until(
                EC.visibility_of_element_located(locator),
                message=f"Can't find element by locator {locator}",
            )
        except TimeoutException:
            return False
        return True

    def check_if_elements_exists(self, locator: Annotated[tuple, 'WebElement'], time_in_seconds):
        try:
            WebDriverWait(self.driver, time_in_seconds).until(
                EC.presence_of_all_elements_located(locator),
                message=f"Can't find elements by locator {locator}",
            )
        except TimeoutException:
            return False
        return True

    def check_if_not_exists(self, locator: Annotated[tuple, 'WebElement'], time_in_seconds):
        try:
            WebDriverWait(self.driver, time_in_seconds).until(
                EC.invisibility_of_element_located(locator),
                message=f"Element with locator {locator} exist",
            )
        except TimeoutException:
            return False
        return True

    def check_string(self, main_string, substring_list):
        for substring in substring_list:
            if substring in main_string:
                return True
        return False

    def retry_func(self, func, max_tries):
        for i in range(max_tries):
            try:
                return func
            except Exception as e:
                if i >= max_tries - 1:
                    raise e

    def move_from_element_with_offset(
        self, element: WebElement, x_offset: float, y_offset: float
    ):
        """
        Move to the passed element with x_offset and y_offset
        :param element: Element to move with offset from
        :param x_offset: x_offset to move to element
        :param y_offset: y_offset to move to the element
        """
        ActionChains(self.driver).move_to_element_with_offset(
            to_element=element, xoffset=x_offset, yoffset=y_offset
        ).perform()

    def move_from_element_with_offset_and_click(
        self, element: WebElement, x_offset: float, y_offset: float
    ):
        """
        Move to the passed element with x_offset and y_offset
        :param element: Element to move with offset from
        :param x_offset: x_offset to move from the element
        :param y_offset: y_offset to move from the element
        """
        ActionChains(self.driver).move_to_element_with_offset(
            to_element=element, xoffset=x_offset, yoffset=y_offset
        ).click().perform()

    def check_if_element_is_clickable(self, locator, time_in_seconds):
        try:
            WebDriverWait(self.driver, time_in_seconds).until(
                EC.element_to_be_clickable(locator)
            ).click()
        except TimeoutException or ElementClickInterceptedException:
            return "Element is not clickable"
