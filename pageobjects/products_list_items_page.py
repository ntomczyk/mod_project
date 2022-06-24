import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage


class ProductsListItems(BasePage):

    PRODUCT_ITEM = (By.CSS_SELECTOR, "[data-test-id='product-list-item']")
    PRODUCT_BASE_BADGE_OFFER = (By.CSS_SELECTOR,  ".base-badge.normal.tertiary")
    PRODUCT_BADGE_OFFER = (By.CSS_SELECTOR,  ".product-badge.product-badge-block")
    PRODUCT_BRAND_ITEM = (By.CSS_SELECTOR, ".brand.product-card-name")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".name.product.product-card-name")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".display-block .price")

    def __init__(self, driver):
        super().__init__(driver)


    @allure.step("Get items in list")
    def get_items(self) -> tuple:
        """
        Get items from the list and return them in the array
        :return [WebElement] of rows in list
        """
        self.element_is_visible(self.PRODUCT_ITEM)
        allure.attach(self.driver.get_screenshot_as_png(), name="get_items", attachment_type=AttachmentType.PNG)
        return self.find_elements(self.PRODUCT_ITEM)

    def get_returned_item(self, item: int) -> WebElement:
        """
        Get text of returned item in the given
        :param item from which data should be got
        :return: str of Returned Item
        """
        items = self.get_items()
        return items[item - 1]

    def get_text_of_product_badge_offer(self, item: int) -> str:
        """
        Get text of badge offer
        :param item: int from which product badge offer text should be got
        :return: str of badge offer
        """
        item= self.get_returned_item(item=item)
        return item.find_element(*self.PRODUCT_BADGE_OFFER).text

    def get_text_of_product_base_badge_offer(self, item: int) -> str:
        """
        Get text of base badge offer
        :param item: int from which product base badge offer text should be got
        :return: str of base badge offer
        """
        item= self.get_returned_item(item=item)
        return item.find_element(*self.PRODUCT_BASE_BADGE_OFFER).text

    def get_text_of_product_brand(self, item: int) -> str:
        """
        Get text of product brand
        :param item: int from which product brand should be got
        :return: str of product brand
        """
        item= self.get_returned_item(item=item)
        return item.find_element(*self.PRODUCT_BRAND_ITEM).text

    def get_text_of_product_name(self, item: int) -> str:
        """
        Get text of product name
        :param item: int from which product name text should be got
        :return: str of product name
        """
        item= self.get_returned_item(item=item)
        return item.find_element(*self.PRODUCT_NAME).text

    def get_text_of_product_price(self, item: int) -> str:
        """
        Get text of product price
        :param item: int from which product price text should be got
        :return: str of product price
        """
        item= self.get_returned_item(item=item)
        return item.find_element(*self.PRODUCT_PRICE).text

    def go_to_product_details(self, item: int) -> WebElement:
        """
        Click on item and go to product details
        :param int of chosen item
        """
        item = self.get_returned_item(item=item)
        item.click(*self.PRODUCT_ITEM)





