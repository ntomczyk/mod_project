import os
import allure
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from pageobjects.base_page import BasePage
import json


class CommonActions(BasePage):
    """
    Class containing common actions, for reusage
    """

    PROMOTION_POPUP = (By.CSS_SELECTOR, ".category > .promotion-widget")
    PROMOTION_POPUP_CLOSE = (By.CSS_SELECTOR, ".button-icon.close")
    ACCOUNT_CHECKOUT_LOADER = (By.CSS_SELECTOR, "div[class='loader']")
    CHECKOUT_LOADER = (By.ID, "code-loader")
    GLOBAL_LOADER = (By.CSS_SELECTOR, "div > svg > g > svg > path.animation-path")

    def __init__(self, driver):
        super().__init__(driver)

    def get_expression_from_language_dictionary(self, key_phrase):
        """
        Getting data from cells, extract the value of a particular data cell by querying into the Pandas dataframe:
        :param column: column name
        :param row: row
        :return: str data from given cell
        """
        translation_file = (
            "testing_data/translation_"
            + (os.getenv("LANGUAGE_VERSION")).lower()
            + ".json"
        )
        with open(translation_file) as jsonFile:
            jsonObject = json.load(jsonFile)
            jsonFile.close()
            return jsonObject[key_phrase]

    @allure.step("Close promotion message if exist")
    def close_promotion_message_if_exists(self):
        if self.check_if_exists(locator=self.PROMOTION_POPUP, time_in_seconds=3):
            self.click_on(self.PROMOTION_POPUP_CLOSE)
        else:
            pass
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="close_promotion_message_if_exists",
            attachment_type=AttachmentType.PNG,
        )

    @allure.step(
        "Wait for checkout loader to appear and disappear, for checking if action was performed to the end."
    )
    def wait_for_checkout_loader(self):
        """Wait for checkout loader to appear and disappear."""

        if self.check_if_exists(locator=self.CHECKOUT_LOADER, time_in_seconds=3):
            self.element_is_not_visible(self.CHECKOUT_LOADER)
        else:
            pass

    @allure.step(
        "Wait for account checkout loader to appear and disappear, for checking if action was performed to the end."
    )
    def wait_for_account_checkout_loader(self):
        """Wait for account checkout loader to appear and disappear."""

        if self.check_if_exists(
            locator=self.ACCOUNT_CHECKOUT_LOADER, time_in_seconds=3
        ):
            self.element_is_not_visible(self.ACCOUNT_CHECKOUT_LOADER)
        else:
            pass

    @allure.step("Check and wait for global loader to appear and disappear")
    def wait_for_global_loader(self):
        """Wait for global checkout loader to appear and disappear."""
        if self.check_if_exists(locator=self.GLOBAL_LOADER, time_in_seconds=3):
            self.element_is_not_visible(self.GLOBAL_LOADER)
        else:
            pass
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="close_promotion_message_if_exists",
            attachment_type=AttachmentType.PNG,
        )
