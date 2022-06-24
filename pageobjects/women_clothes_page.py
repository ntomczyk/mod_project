import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage


class WomenClothes(BasePage):



    WOMEN_CLOTHES_TOPS_AND_SHIRTS = (By.CSS_SELECTOR, ".tree li:nth-of-type(6) .link")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click on women tops and shirts")
    def click_on_women_tops_and_shirts(self):
        """Go to women category - tops and shirts."""

        self.click_on(self.WOMEN_CLOTHES_TOPS_AND_SHIRTS)

        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="click_on_women_tops_and_shirts",
            attachment_type=AttachmentType.PNG,
        )
