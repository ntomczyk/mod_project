import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from pageobjects.common_actions import CommonActions


class ClothesFilters(CommonActions):

    FILTERS = (By.CSS_SELECTOR, ".actions-container")
    SIZE = (By.CSS_SELECTOR, ".filter.nestedmultiselect .text")
    FILTER_WRAPPER_PANEL = (By.CSS_SELECTOR, ".filter-wrapper-panel")
    FILTER_SIZE_CATEGORY_OPTIONS = (By.CSS_SELECTOR, ".filter-size-category-options")
    FILTER_SIZE_CONTENT = (By.CSS_SELECTOR, "filter-size filter-content")
    UPPER_CLOTHING = (
        By.CSS_SELECTOR,
        "[data-test-id='filters-size-category-item-damskie_gorne_czesci_garderoby']",
    )
    OFFER = (
        By.CSS_SELECTOR,
        ".filter.multiselect:nth-of-type(3) .filter-wrapper-label",
    )
    NEWS = (By.CSS_SELECTOR, "[for='checkbox-nowosc']")
    APPLY_BUTTON = (By.CSS_SELECTOR, "[data-test-id='filters-apply-button']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Choose filter size")
    def choose_filter_size(self):
        """Choose filter size."""

        self.element_is_visible(self.FILTERS)
        self.click_on(self.SIZE)

        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="choose_filter_size",
            attachment_type=AttachmentType.PNG,
        )

    @allure.step("Choose upper clothing")
    def choose_upper_clothing(self):
        """In filter size choose upper clothing."""

        self.element_is_visible(self.FILTER_WRAPPER_PANEL)
        self.click_on(self.UPPER_CLOTHING)

        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="choose_upper_clothing",
            attachment_type=AttachmentType.PNG,
        )

    @allure.step("Check option size")
    def check_size(self, given_size: str):
        """
        Check checkbox of given size
        :param given_size: str, Basic sizes in format XXS, 7XL, Detailed sizes in format XS:XS or M:38
        """

        locator = f"[for='checkbox-damskie_gorne_czesci_garderoby:{given_size}']"
        size = (By.CSS_SELECTOR, locator)
        self.element_is_visible(self.FILTER_SIZE_CATEGORY_OPTIONS)
        self.element_is_visible(size)
        self.click_on(size)

        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="check_size",
            attachment_type=AttachmentType.PNG,
        )

    @allure.step("Choose filter offer")
    def choose_filter_offer(self):
        """Choose filter offer."""

        self.wait_for_global_loader()
        self.element_is_visible(self.FILTERS)
        self.click_on(self.OFFER)

        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="choose_filter_offer",
            attachment_type=AttachmentType.PNG,
        )

    @allure.step("Check option news")
    def check_option_news(self):
        """Check option news in offer."""

        self.element_is_visible(self.FILTER_WRAPPER_PANEL)
        self.click_on(self.NEWS)

        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="choose_filter_offer",
            attachment_type=AttachmentType.PNG,
        )

    @allure.step("Click on apply button")
    def click_on_apply_button(self):
        """Apply chosen filters clicking on button apply."""

        self.wait_for_global_loader()
        self.click_on(self.APPLY_BUTTON)

        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="click_on_apply_button",
            attachment_type=AttachmentType.PNG,
        )
