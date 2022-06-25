import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage


class ProductsDetails(BasePage):

    PRODUCT_DETAILS_BRAND_NAME = (By.CSS_SELECTOR, "[data-test-id='product-name'] a")
    PRODUCT_DETAILS_NAME = (By.CSS_SELECTOR, "[data-test-id='product-name'] ._heading-h4")
    PRODUCT_DETAILS_REGULAR_PRICE = (By.CSS_SELECTOR, ".price-regular .price")
    PRODUCT_DETAILS_FINAL_PRICE = (By.CSS_SELECTOR, ".final-price-wrapper .price")
    PRODUCT_DETAILS_PRICE = (By.CSS_SELECTOR, ".price-container .price")
    PRODUCT_DETAILS_PRODUCT_DISCOUNT_TEXT = (By.CSS_SELECTOR, ".discount-text")
    PRODUCT_DETAILS_CHOOSE_SIZE = (By.CSS_SELECTOR, "[data-test-id='choose-product-size']")

    CHOOSE_SIZE_BUTTON = (By.CSS_SELECTOR, ".choose-size-button .content")
    SIZES = (By.CSS_SELECTOR, "[data-test-id='product-size']")
    PRODUCT_DETAILS_ADD_TO_CARD = (By.CSS_SELECTOR, "[data-test-id='add-to-cart-button']")

    def __init__(self, driver):
        super().__init__(driver)



    @allure.step("Get text of brand name in section product details")
    def get_text_of_product_details_brand_name(self) -> str:
        """
        Get text of brand name in section product details
        :return: str of brand name
        """
        return self.get_text_of(self.PRODUCT_DETAILS_BRAND_NAME)

    @allure.step("Get text of product name in section product details")
    def get_text_of_product_details_name(self) -> str:
        """
        Get text of product name in section product details
        :return: str of product name
        """
        return self.get_text_of(self.PRODUCT_DETAILS_NAME)

    @allure.step("Get text of product price in section product details")
    def get_text_of_product_details_price(self) -> str:
        """
        Get text of product price (without discount) in section product details
        :return: str of product price
        """
        return self.get_text_of(self.PRODUCT_DETAILS_PRICE)

    @allure.step("Get text of product regular price in section product details")
    def get_text_of_product_details_regular_price(self) -> str:
        """
        Get text of product regular price (before discount) in section product details
        :return: str of product regular price
        """
        return self.get_text_of(self.PRODUCT_DETAILS_REGULAR_PRICE)


    @allure.step("Get text of product final price in section product details")
    def get_text_of_product_details_final_price(self) -> str:
        """
        Get text of product final price (after discount) in section product details
        :return: str of product discount price
        """
        return self.get_text_of(self.PRODUCT_DETAILS_FINAL_PRICE)

    @allure.step("Get text of product discount in section product details")
    def get_text_of_product_details_discount(self) -> str:
        """
        Get text of product discount in section product details
        :return: str of product discount
        """
        return self.get_text_of(self.PRODUCT_DETAILS_PRODUCT_DISCOUNT_TEXT)

    @allure.step("Choose size in product details")
    def click_chosen_size_product_details(self, given_size):
        """
        Choose size in product details
        :param given_size: str e.g. S, 38, 7XXL
        """
        self.click_on(self.SIZES)
        # sizes = self.find_elements(self.SIZES)
        #
        # for size in sizes:
        #     print(size.text)
            # if given_size in size.text:
            #     print(size.text)
            #     print(type(size.text))
            #     size.click()

        # [size.click() for size in sizes if given_size in size]
        allure.attach(self.driver.get_screenshot_as_png(), name="click_chosen_size_product_details", attachment_type=AttachmentType.PNG)


    @allure.step("Clisk on choose size button")
    def click_on_choose_size_button(self):

        """ Choose size of item """

        self.click_on(self.CHOOSE_SIZE_BUTTON)
        allure.attach(self.driver.get_screenshot_as_png(), name="click_on_choose_size_button", attachment_type=AttachmentType.PNG)

    @allure.step("Add product to cart")
    def add_product_to_cart(self):

        """ Add product to shopping cart """

        self.click_on(self.PRODUCT_DETAILS_ADD_TO_CARD)
        allure.attach(self.driver.get_screenshot_as_png(), name="add_product_to_cart", attachment_type=AttachmentType.PNG)




