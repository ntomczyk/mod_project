import allure
from allure_commons.types import AttachmentType
from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage
from random import randint


class ProductsItemsList(BasePage):

    PRODUCT_ITEM = (By.CSS_SELECTOR, "[data-test-id='product-list-item']")
    PRODUCT_BASE_BADGE_OFFER = (
        By.CSS_SELECTOR,
        "span[class='base-badge tertiary normal']",
    )
    PRODUCT_BADGE_OFFER = (By.CSS_SELECTOR, ".product-badge.product-badge-block")
    PRODUCT_BRAND_ITEM = (By.CSS_SELECTOR, ".brand.product-card-name")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".name.product.product-card-name")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".final-price-wrapper .price")
    PRODUCT_REGULAR_PRICE = (By.CSS_SELECTOR, ".price-with-discount .price")
    PRODUCT_DISCOUNT_TEXT = (By.CSS_SELECTOR, ".discount-text")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Get items in list")
    def get_items(self) -> list:
        """
        Get items from the product list and return them in the array
        :return [WebElement] of items in list
        """
        self.element_is_visible(self.PRODUCT_ITEM)
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="get_items",
            attachment_type=AttachmentType.PNG,
        )
        return self.find_elements(self.PRODUCT_ITEM)

    @allure.step("Get random item")
    def get_random_item(self) -> int:
        """
        Get random item from the product list
        :return int
        """

        len_items = len(self.get_items())
        return randint(1, len_items)

    @allure.step("Get chosen item from product list")
    def get_returned_item(self, item: int) -> WebElement:
        """
        Get returned item
        :param item from which data should be got
        :return: parent WebElement
        """
        items = self.get_items()
        return items[item - 1]

    @allure.step("Get text of filter tag")
    def get_text_of_filter_tag(self, filter_number: int) -> str:
        """
        Get text of filter tag
        :param filter_number: from which data should be got
        :return: str text of filter tag
        """
        filter_tag = (
            By.CSS_SELECTOR,
            f".base-tag-row > div:nth-of-type({filter_number})",
        )
        return self.get_text_of(filter_tag)

    @allure.step("Get text of product badge offer in product list")
    def get_text_of_product_badge_offer(self, item: int) -> str:
        """
        Get text of badge offer
        :param item: int from which product badge offer text should be got
        :return: str of badge offer
        """
        item = self.get_returned_item(item=item)
        return item.find_element(*self.PRODUCT_BADGE_OFFER).text

    @allure.step("Get text of product base badge offers in product list")
    def get_text_of_product_base_badge_offer(self, item: int) -> list[str]:
        """
        Get text of base badge offers
        :param item: int from which product base badge offers text should be got
        :return: str of base badge offers
        """
        item = self.get_returned_item(item=item)
        return item.find_element(*self.PRODUCT_BASE_BADGE_OFFER).text

    @allure.step("Get text of product brand in product list")
    def get_text_of_product_brand(self, item: int) -> str:
        """
        Get text of product brand
        :param item: int from which product brand should be got
        :return: str of product brand
        """
        item = self.get_returned_item(item=item)
        return item.find_element(*self.PRODUCT_BRAND_ITEM).text

    @allure.step("Get text of product name in product list")
    def get_text_of_product_name(self, item: int) -> str:
        """
        Get text of product name
        :param item: int from which product name text should be got
        :return: str of product name
        """
        item = self.get_returned_item(item=item)
        return item.find_element(*self.PRODUCT_NAME).text

    @allure.step("Get text of product price in product list")
    def get_text_of_product_price(self, item: int) -> str:
        """
        Get text of product price
        :param item: int from which product price text should be got
        :return: str of product price
        """
        item = self.get_returned_item(item=item)
        return item.find_element(*self.PRODUCT_PRICE).text

    @allure.step(
        "Check if product has discount and get text of regular price in product list"
    )
    def check_if_product_has_discount_and_get_text_of_regular_price(
        self, item: int) -> str:
        """
        Check id product has discount and get text of product regular price before discount
        :param item: int from which product regular price before discount text should be got
        :return: str of product regular price before discount
        """
        item = self.get_returned_item(item=item)

        try:
            item.find_element(*self.PRODUCT_REGULAR_PRICE)
            return item.find_element(*self.PRODUCT_REGULAR_PRICE).text
        except NoSuchElementException:
            pass

    @allure.step(
        "Check if product has discount and get text of discount in product list"
    )
    def check_if_product_has_discount_and_get_text_of_discount(self, item: int) -> str:
        """
        Check id product has discount and get text of product discount
        :param item: int from which product discount text should be got
        :return: str of product discount
        """
        item = self.get_returned_item(item=item)
        try:
            item.find_element(*self.PRODUCT_DISCOUNT_TEXT)
            discount_text = item.find_element(*self.PRODUCT_DISCOUNT_TEXT).text
            return discount_text
        except NoSuchElementException:
            pass

    def go_to_product_details(self, item: int):
        """
        Click on item and go to product details
        :param item: int of chosen item
        """
        item = self.get_returned_item(item=item)
        item.click()
