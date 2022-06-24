import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage


class WomenMenu(BasePage):
    CATEGORY_MENU = (By.CSS_SELECTOR, ".container-content > .category-tree")
    WOMEN_MENU_CATEGORY_CLOTHES = (
        By.CSS_SELECTOR,
        ".category-tree [class='navigation-item _level-1']:nth-of-type(4) > .navigation-item-content-wrapper .navigation-item-content",
    )

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click on women menu category clothes")
    def click_on_women_menu_category_clothes(self):
        """Go to women category - clothes."""

        self.element_is_visible(self.CATEGORY_MENU)
        self.element_is_visible(self.WOMEN_MENU_CATEGORY_CLOTHES)
        self.click_on(self.WOMEN_MENU_CATEGORY_CLOTHES)

        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="click_on_women_menu_category_clothes",
            attachment_type=AttachmentType.PNG,
        )
