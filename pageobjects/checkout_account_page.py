import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage


class CheckoutAccount(BasePage):

    CONTINUE_AS_GUEST_BUTTON = (By.CSS_SELECTOR, "[data-test-id='continue-as-guest']")


    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click on continue as guest button")
    def click_on_continue_as_guest_button(self):

        """ Click on continue as guest button to go to the checkout page. """

        self.click_on(self.CONTINUE_AS_GUEST_BUTTON)
        allure.attach(self.driver.get_screenshot_as_png(), name="click_on_continue_as_guest_button",
                      attachment_type=AttachmentType.PNG)
