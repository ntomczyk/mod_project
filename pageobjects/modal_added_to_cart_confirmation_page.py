import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage


class ModalAddedToCardConfirmation(BasePage):

    MODAL_ADDED_TO_CARD_CONFIRMATION = (By.ID, "modal-added-to-cart-confirmation")
    GO_TO_CARD_BUTTON = (
        By.CSS_SELECTOR,
        "[data-test-id='added-to-cart-go-to-cart-button']",
    )

    MODAL_ADDED_TO_CART_BRAND_NAME = (By.CSS_SELECTOR, "[class='text-link brand']")
    MODAL_ADDED_TO_CART_NAME = (
        By.CSS_SELECTOR,
        "[class='text-link name nuxt-link-exact-active nuxt-link-active']",
    )
    MODAL_ADDED_TO_CART_DISCOUNT_PRICE = (
        By.CSS_SELECTOR,
        ".extra-small .price-with-discount .price",
    )
    MODAL_ADDED_TO_CART_DISCOUNT = (By.CSS_SELECTOR, ".extra-small .discount-text")
    MODAL_ADDED_TO_CART_FINAL_PRICE = (
        By.CSS_SELECTOR,
        ".extra-small .final-price-wrapper .price",
    )
    MODAL_ADDED_TO_CART_PRICE = (By.CSS_SELECTOR, ".extra-small .price")
    MODAL_ADDED_TO_CART_SIZE = (By.XPATH, "//li[1]/span[@class='value-label']")
    MODAL_ADDED_TO_CART_COLOUR = (By.XPATH, "//li[2]/span[@class='value-label']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click on show card button")
    def click_on_go_to_cart_button(self):
        """Click on go to cart button. """

        self.click_on(self.GO_TO_CARD_BUTTON)
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="click_on_go_to_cart_button",
            attachment_type=AttachmentType.PNG,
        )
