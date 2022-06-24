import pandas as pd
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType
from pageobjects.base_page import BasePage

class CommonActions(BasePage):
    """
    Class containing common actions, for reusage
    """

    PROMOTION_POPUP = (By.CSS_SELECTOR, ".category > .promotion-widget")
    PROMOTION_POPUP_CLOSE = (By.CSS_SELECTOR, ".button-icon.close")

    def __init__(self, driver):
        super().__init__(driver)

    def get_expression_from_language_dictionary(self, language_cod, keys):
        # Get Client order number from XLS
        order_import_list_path = "testing_data/orderlist.xlsx"
        csv = pd.read_excel(order_import_list_path)
        client_order_number = csv["client_order_number "][0]



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

