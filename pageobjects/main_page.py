import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage


class MainPage(BasePage):

    SELECTED_COUNTRY = (By.CSS_SELECTOR, ".countries-dropdown.dropdown.small > .select")
    COUNTRIES_IN_THE_LIST = (
        By.CSS_SELECTOR,
        ".options > .options-container > .option > span > span",
    )
    MENU_WOMEN = (
        By.XPATH,
        "//section[@class='header-main-category-menu']/ul[@class='list']/li[1]",
    )
    MARKETING_APPROVALS = (By.CSS_SELECTOR, "div#marketing-approvals > .modal")
    MARKETING_APPROVALS_CLOSE = (By.CSS_SELECTOR, ".close-icon-wrapper .svg")

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver = driver

    @allure.step("Check the language set")
    def check_language_set(self, language: str):
        """
        Check if correct language was set, if not select it.
        :param language: Country code e.g. PL
        """
        set_language = self.get_text_of(self.SELECTED_COUNTRY)
        if set_language is not language:
            self.click_on(self.SELECTED_COUNTRY)
            self.select_by_visible_text(language)

        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="check_language_set",
            attachment_type=AttachmentType.PNG,
        )

    @allure.step("Click on women in top menu")
    def click_on_women_in_top_menu(self):
        """Go to women items."""

        self.element_is_visible(self.MENU_WOMEN)
        self.click_on(self.MENU_WOMEN)

        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="click_on_women_in_top_menu",
            attachment_type=AttachmentType.PNG,
        )

    @allure.step("Close modal message if exist")
    def close_modal_message_if_exists(self):
        if self.check_if_exists(locator=self.MARKETING_APPROVALS, time_in_seconds=3):
            self.click_on(self.MARKETING_APPROVALS_CLOSE)
        else:
            pass
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="close_modal_message_if_exists",
            attachment_type=AttachmentType.PNG,
        )
