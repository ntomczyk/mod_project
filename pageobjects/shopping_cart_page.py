import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement


class ShoppingCart(BasePage):

    SHOPPING_CART_TITLE = (By.CSS_SELECTOR, ".checkout-cart-items ._heading-h3")
    SHOPPING_CART_ITEM = (By.CSS_SELECTOR, ".items .shopping-cart-item-container")
    SHOPPING_CART_PRODUCT_BRAND_NAME = (
        By.CSS_SELECTOR,
        ".brand-name-md ._heading-strong",
    )
    SHOPPING_CART_PRODUCT_NAME = (By.CSS_SELECTOR, "[class='text-link name']")
    SHOPPING_CART_PRODUCT_SIZE = (By.CSS_SELECTOR, ".values > li:nth-of-type(1)")
    SHOPPING_CART_PRODUCT_COLOUR = (By.CSS_SELECTOR, ".values > li:nth-of-type(2)")
    SHOPPING_CART_PRODUCT_QUANTITY_AND_PRICE = (
        By.CSS_SELECTOR,
        ".values > li:nth-of-type(3)",
    )
    SHOPPING_CART_REGULAR_PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        ".item-price-md .price-with-discount .price",
    )
    SHOPPING_CART_DISCOUNT = (By.CSS_SELECTOR, ".item-price-md .discount-text")
    SHOPPING_CART_PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        ".item-price-md .final-price-wrapper .price",
    )
    SHOPPING_CART_SUMMARY_PRICE = (
        By.CSS_SELECTOR,
        ".summary-block .summary-row:nth-of-type(1) .price",
    )
    SHOPPING_CART_TOTAL_PRICE_WITH_TAX = (By.CSS_SELECTOR, ".total .price")
    SHOPPING_CART_PROCEED_TO_PAYMENT_BUTTON = (
        By.CSS_SELECTOR,
        "[data-test-id='cart-proceed-to-checkout']",
    )

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Get text of shopping cart title")
    def get_text_of_shopping_cart_title(self) -> str:
        """
        Get text of shopping cart title and number of items
        :return: str Shopping cart and  number of items
        """
        return self.get_text_of(self.SHOPPING_CART_TITLE)

    @allure.step("Get chosen item from shopping cart")
    def get_returned_item_from_shopping_cart_by_product_name(
        self, product_brand: str, product_name: str
    ) -> WebElement:
        """
        Get chosen item from shopping cart
        :param product_brand: str, name of product brand
        :param product_name: str, name of product name
        :return: parent WebElement
        """

        self.element_is_visible(self.SHOPPING_CART_ITEM)
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="get_items",
            attachment_type=AttachmentType.PNG,
        )
        long_product_name = product_brand.title() + " " + product_name
        item = (
            By.XPATH,
            f"//div[@class='brand-name brand-name-md']/a[@title='{long_product_name}']"
            f"/ancestor::div[@class='item-block-container']",
        )
        shopping_cart_item = self.find(item)
        return shopping_cart_item

    @allure.step("Get text of product brand name in shopping cart")
    def get_text_of_product_brand_name_in_shopping_cart(
        self, product_brand: str, product_name: str
    ) -> str:
        """
        Get text of product brand name in shopping cart
        :param product_brand: str, name of product brand
        :param product_name: str, name of product name
        :return: str of product brand name
        """
        shopping_cart_item = self.get_returned_item_from_shopping_cart_by_product_name(
            product_brand, product_name
        )
        return shopping_cart_item.find_element(
            *self.SHOPPING_CART_PRODUCT_BRAND_NAME
        ).text

    @allure.step("Get text of product name in shopping cart")
    def get_text_of_product_name_in_shopping_cart(
        self, product_brand: str, product_name: str
    ) -> str:
        """
        Get text of product name in shopping cart
        :param product_brand: str, name of product brand
        :param product_name: str, name of product name
        :return: str of product name in shopping cart
        """
        shopping_cart_item = self.get_returned_item_from_shopping_cart_by_product_name(
            product_brand, product_name
        )
        return shopping_cart_item.find_element(*self.SHOPPING_CART_PRODUCT_NAME).text

    @allure.step("Get text of product colour in shopping cart")
    def get_text_of_product_colour_in_shopping_cart(
        self, product_brand: str, product_name: str
    ) -> str:
        """
        Get text of product colour in shopping cart
        :param product_brand: str, name of product brand
        :param product_name: str, name of product name
        :return: str of product colour in shopping cart
        """
        shopping_cart_item = self.get_returned_item_from_shopping_cart_by_product_name(
            product_brand, product_name
        )
        return shopping_cart_item.find_element(*self.SHOPPING_CART_PRODUCT_COLOUR).text

    @allure.step("Get text of product size in shopping cart")
    def get_text_of_product_size_in_shopping_cart(
        self, product_brand: str, product_name: str
    ) -> str:
        """
        Get text of product size in shopping cart
        :param product_brand: str, name of product brand
        :param product_name: str, name of product name
        :return: str of product size
        """
        shopping_cart_item = self.get_returned_item_from_shopping_cart_by_product_name(
            product_brand, product_name
        )
        return shopping_cart_item.find_element(*self.SHOPPING_CART_PRODUCT_SIZE).text

    @allure.step("Get text of roduct quantity and price in shopping cart")
    def get_text_of_product_quantity_and__price_in_shopping_cart(
        self, product_brand: str, product_name: str
    ) -> str:
        """
        Get text of product quantity and price in shopping cart
        :param product_brand: str, name of product brand
        :param product_name: str, name of product name
        :return: str of product value price
        """
        shopping_cart_item = self.get_returned_item_from_shopping_cart_by_product_name(
            product_brand, product_name
        )
        return shopping_cart_item.find_element(
            *self.SHOPPING_CART_PRODUCT_QUANTITY_AND_PRICE
        ).text

    @allure.step("Get text of product regular price in shopping cart")
    def get_text_of_product_regular_price_in_shopping_cart(
        self, product_brand: str, product_name: str
    ) -> str:
        """
        Get text of product regular price in shopping cart before discount
        :param product_brand: str, name of product brand
        :param product_name: str, name of product name
        :return: str of product regularprice
        """
        shopping_cart_item = self.get_returned_item_from_shopping_cart_by_product_name(
            product_brand, product_name
        )
        return shopping_cart_item.find_element(
            *self.SHOPPING_CART_REGULAR_PRODUCT_PRICE
        ).text

    @allure.step("Get text of product price in shopping cart")
    def get_text_of_product_price_in_shopping_cart(
        self, product_brand: str, product_name: str
    ) -> str:
        """
        Get text of product price in shopping cart
        :param product_brand: str, name of product brand
        :param product_name: str, name of product name
        :return: str of product price
        """
        shopping_cart_item = self.get_returned_item_from_shopping_cart_by_product_name(
            product_brand, product_name
        )
        return shopping_cart_item.find_element(*self.SHOPPING_CART_PRODUCT_PRICE).text

    @allure.step("Get text of discount in shopping cart")
    def get_text_of_discount(self, product_brand: str, product_name: str) -> str:
        """
        Get text of discount in shopping cart
        :param product_brand: str, name of product brand
        :param product_name: str, name of product name
        :return: str of discount
        """
        shopping_cart_item = self.get_returned_item_from_shopping_cart_by_product_name(
            product_brand, product_name
        )
        return shopping_cart_item.find_element(*self.SHOPPING_CART_DISCOUNT).text

    @allure.step("Get text of products summary price in shopping cart")
    def get_text_of_products_summary_price_in_shopping_cart(self) -> str:
        """
        Get text of products summary price in shopping cart
        :return: str of products summary price
        """
        return self.get_text_of(self.SHOPPING_CART_SUMMARY_PRICE)

    @allure.step("Get text of products total price in shopping cart")
    def get_text_of_products_total_price_in_shopping_cart(self) -> str:
        """
        Get text of products total price with tax and discounts in shopping cart
        :return: str of products total price
        """
        return self.get_text_of(self.SHOPPING_CART_TOTAL_PRICE_WITH_TAX)

    @allure.step("Click on proceed to payment button in shopping cart")
    def click_on_proceed_to_payment_button(self):
        """Click on proceed to payment button in shopping cart"""
        self.click_on(self.SHOPPING_CART_PROCEED_TO_PAYMENT_BUTTON)
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="click_on_proceed_to_payment_button",
            attachment_type=AttachmentType.PNG,
        )
