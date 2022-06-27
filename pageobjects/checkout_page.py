import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement


class Checkout(BasePage):

    # SUMMARY
    SUMMARY_ITEMS = (By.CSS_SELECTOR, ".order-item-container")
    SUMMARY_BRAND = (By.XPATH, "//span[@class='brand']")
    SUMMARY_PRODUCT_NAME = (By.XPATH, "//a[@class='text-link name']")
    SUMMARY_PRODUCT_SIZE = (By.CSS_SELECTOR, ".values > li:nth-of-type(1)")
    SUMMARY_PRODUCT_COLOUR = (By.CSS_SELECTOR, ".values > li:nth-of-type(2)")
    SUMMARY_PRODUCT_QUANTITY = (By.CSS_SELECTOR, ".values > li:nth-of-type(3)")
    SUMMARY_PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        ".display-inline.item-price.product-price.small .price",
    )
    SUMMARY_ALL_PRODUCTS_PRICE = (
        By.CSS_SELECTOR,
        ".summary .summary-row:nth-child(2) .price",
    )
    SUMMARY_SHIPPING_PRICE = (
        By.CSS_SELECTOR,
        ".summary .summary-row:nth-child(3) .price",
    )
    SUMMARY_TOTAL_PRICE = (By.CSS_SELECTOR, ".total .price")

    # Customer data
    CUSTOMER_DATA_SECTION = (By.ID, "relative-element")
    EMAIL = (By.CSS_SELECTOR, ".email")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[data-test-id='billing__email']")
    PHONE = (By.CSS_SELECTOR, ".input-field.phone")
    PHONE_INPUT = (By.CSS_SELECTOR, "input[data-test-id='billing__telephone']")
    NAME = (By.CSS_SELECTOR, ".firstname")
    NAME_INPUT = (By.ID, "billing__firstname")
    SURNAME = (By.CSS_SELECTOR, ".lastname")
    SURNAME_INPUT = (By.ID, "billing__lastname")
    STREET = (By.CSS_SELECTOR, ".street")
    STREET_INPUT = (By.CSS_SELECTOR, "input[data-test-id='billing__street-0']")
    HOUSE_NO = (By.CSS_SELECTOR, ".house-no")
    HOUSE_NO_INPUT = (By.CSS_SELECTOR, "input[data-test-id='billing__street-1']")
    APARTMENT_NO = (By.CSS_SELECTOR, ".apartment-no")
    APARTMENT_NO_INPUT = (By.ID, "billing__street-2")
    POST_CODE = (By.CSS_SELECTOR, ".postcode")
    POST_CODE_INPUT = (By.ID, "billing__postcode")
    CITY = (By.CSS_SELECTOR, "div>[for='billing__city']")
    CITY_INPUT = (By.CSS_SELECTOR, "input[data-test-id='billing__city']")

    # Shipping method
    SHIPPING_METHOD_SECTION = (By.CSS_SELECTOR, ".checkout-shipping-methods")
    DHL_SHIPPING_METHOD = (By.CSS_SELECTOR, "[for='modivo_store_custom02']")

    # Payment methods
    PAY_CARD = (By.CSS_SELECTOR, "[for='payu_gateway_card']")
    VALIDATION_MESSAGE_PAY_CARD = (By.CSS_SELECTOR, ".paragraph.validation-error")

    # Iframe
    IFRAME_CARD_NUMBER = (
        By.CSS_SELECTOR,
        "div#payu-card-number > iframe[name='_PayuFormIframe_1']",
    )
    IFRAME_CARD_DATE = (
        By.CSS_SELECTOR,
        "div#payu-card-date > iframe[name='_PayuFormIframe_2']",
    )
    IFRAME_CARD_CVV = (
        By.CSS_SELECTOR,
        "div#payu-card-cvv > iframe[name='_PayuFormIframe_3']",
    )
    CARD_NUMBER = (By.ID, "card-number")
    CARD_DATE = (By.CSS_SELECTOR, "input[name='expDate']")
    CARD_CVV = (By.CSS_SELECTOR, "input[name='cvv']")

    # Required terms
    AGREEMENTS_SECTION = (By.CSS_SELECTOR, ".agreements-form .form-group")
    TERMS = (By.CSS_SELECTOR, "[for='check-all']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click on continue as guest button")
    def click_on_continue_as_guest_button(self):

        """Click on continue as guest button to go to the checkout page."""

        self.click_on(self.CONTINUE_AS_GUEST_BUTTON)
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="click_on_continue_as_guest_button",
            attachment_type=AttachmentType.PNG,
        )

    @allure.step("Enter customer email")
    def enter_customer_email(self, email: str):
        """
        Enter customer email.
        :param email: str, customer email
        """
        self.element_is_visible(self.CUSTOMER_DATA_SECTION)
        self.click_on(self.EMAIL)
        self.enter_text(self.EMAIL_INPUT, email)

        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="enter_customer_email",
            attachment_type=AttachmentType.PNG,
        )

    @allure.step("Enter customer phone")
    def enter_customer_phone(self, phone: str):
        """
        Enter customer phone.
        :param phone: str, customer phone
        """
        self.click_on(self.PHONE)
        self.enter_text(self.PHONE_INPUT, phone)
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="enter_customer_phone",
            attachment_type=AttachmentType.PNG,
        )

    @allure.step("Enter customer name")
    def enter_customer_name(self, name: str):
        """
        Enter customer name.
        :param name: str, customer name
        """
        self.click_on(self.NAME)
        self.enter_text(self.NAME_INPUT, name)
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="enter_customer_name",
            attachment_type=AttachmentType.PNG,
        )

    @allure.step("Enter customer surname")
    def enter_customer_surname(self, surname: str):
        """
        Enter customer surname.
        :param surname: str, customer surname
        """
        self.click_on(self.SURNAME)
        self.enter_text(self.SURNAME_INPUT, surname)
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="enter_customer_surname",
            attachment_type=AttachmentType.PNG,
        )

    @allure.step("Enter customer street")
    def enter_customer_street(self, street: str):
        """
        Enter customer street.
        :param street: str, customer street
        """
        self.click_on(self.STREET)
        self.enter_text(self.STREET_INPUT, street)
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="enter_customer_street",
            attachment_type=AttachmentType.PNG,
        )

    @allure.step("Enter customer house number")
    def enter_customer_house_number(self, house_no: str):
        """
        Enter customer house number.
        :param house_no: str, customer house number
        """
        self.click_on(self.HOUSE_NO)
        self.enter_text(self.HOUSE_NO_INPUT, house_no)
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="enter_customer_house_no",
            attachment_type=AttachmentType.PNG,
        )

    @allure.step("Enter customer apartment number")
    def enter_customer_apartment_number(self, apartment_no: str):
        """
        Enter customer apartment number.
        :param apartment_no: str, customer apartment number
        """
        self.click_on(self.APARTMENT_NO)
        self.enter_text(self.APARTMENT_NO_INPUT, apartment_no)
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="enter_customer_apartment_number",
            attachment_type=AttachmentType.PNG,
        )

    @allure.step("Enter customer post code")
    def enter_customer_post_code(self, post_code: str):
        """
        Enter customer post code.
        :param post_code: str, customer post_code
        """
        self.click_on(self.POST_CODE)
        self.enter_text(self.POST_CODE_INPUT, post_code)
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="enter_customer_post_code",
            attachment_type=AttachmentType.PNG,
        )

    @allure.step("Enter customer city")
    def enter_customer_city(self, city: str):
        """
        Enter customer city.
        :param city: str, customer city
        """
        self.click_on(self.CITY)
        self.enter_text(self.CITY_INPUT, city)
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="enter_customer_city",
            attachment_type=AttachmentType.PNG,
        )

    @allure.step("Check DHL shipping method")
    def check_dhl_shipping_method(self):

        """Check checkbox with DHL shipping method."""

        self.click_on(self.SHIPPING_METHOD_SECTION)
        self.click_on(self.DHL_SHIPPING_METHOD)
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="check_dhl_shipping_method",
            attachment_type=AttachmentType.PNG,
        )

    @allure.step("Check payment method -card")
    def check_payment_method_card(self):
        """Check checkbox with card payment method."""

        self.click_on(self.PAY_CARD)
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="check_payment_method_card",
            attachment_type=AttachmentType.PNG,
        )

    @allure.step("Enter card number")
    def enter_card_number(self, card_number: str):
        """
        Enter customer card number.
        :param card_number: str, customer card number
        """
        self.switch_to_iframe(self.IFRAME_CARD_NUMBER)
        self.enter_text(self.CARD_NUMBER, card_number)
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="enter_card_number",
            attachment_type=AttachmentType.PNG,
        )

    @allure.step("Enter card expiration date8")
    def enter_card_expiration_date(self, card_date: str):
        """
        Enter customer card expiration date.
        :param card_date: str, customer card date
        """
        self.switch_to_iframe(self.IFRAME_CARD_DATE)
        self.enter_text(self.CARD_DATE, card_date)
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="enter_card_expiration_date",
            attachment_type=AttachmentType.PNG,
        )

    @allure.step("Enter cvv code")
    def enter_cvv_code(self, cvv_code: str):
        """
        Enter customer card cvv code.
        :param cvv_code: str, customer card cvv code
        """
        self.switch_to_iframe(self.IFRAME_CARD_CVV)
        self.enter_text(self.CARD_CVV, cvv_code)
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="enter_cvv_code",
            attachment_type=AttachmentType.PNG,
        )

    @allure.step("Check required terms")
    def check_required_terms(self):
        """Check checkbox with required terms."""

        self.element_is_visible(self.AGREEMENTS_SECTION)
        self.element_is_visible(self.TERMS)
        self.click_on(self.TERMS)
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="check_required_terms",
            attachment_type=AttachmentType.PNG,
        )

    @allure.step("Check required terms")
    def check_required_terms(self):
        """Check checkbox with required terms."""

        self.element_is_visible(self.AGREEMENTS_SECTION)
        self.element_is_visible(self.TERMS)
        self.click_on(self.TERMS)
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="check_required_terms",
            attachment_type=AttachmentType.PNG,
        )

    @allure.step("Get chosen item from summary")
    def get_returned_item_from_summary_by_product_name(
        self, product_brand: str, product_name: str
    ) -> WebElement:
        """
        Get chosen item from summary
        :param product_brand: str, name of product brand
        :param product_name: str, name of product name
        :return: parent WebElement
        """

        allure.attach(
            self.driver.get_screenshot_as_png(),
            name="get_items",
            attachment_type=AttachmentType.PNG,
        )
        long_product_name = product_brand.title() + " " + product_name
        item = (
            By.XPATH,
            f"//a[@title='{long_product_name}']/ancestor::div[@class='item-container order-item-container']",
        )
        summary_item = self.find(item)
        return summary_item

    @allure.step("Get text of product brand name in summary")
    def get_text_of_product_brand_name_in_summary(
        self, product_brand: str, product_name: str
    ) -> str:
        """
        Get text of product brand name in summary
        :param product_brand: str, name of product brand
        :param product_name: str, name of product name
        :return: str of product brand name
        """

        summary_item = self.get_returned_item_from_summary_by_product_name(
            product_brand, product_name
        )
        return summary_item.find_element(*self.SUMMARY_BRAND).text

    @allure.step("Get text of product name in summary")
    def get_text_of_product_name_in_summary(
        self, product_brand: str, product_name: str
    ) -> str:
        """
        Get text of product name in summary
        :param product_brand: str, name of product brand
        :param product_name: str, name of product name
        :return: str of product name in summary
        """
        shopping_cart_item = self.get_returned_item_from_summary_by_product_name(
            product_brand, product_name
        )
        return shopping_cart_item.find_element(*self.SUMMARY_PRODUCT_NAME).text

    @allure.step("Get text of product colour in summary")
    def get_text_of_product_colour_in_summary(
        self, product_brand: str, product_name: str
    ) -> str:
        """
        Get text of product colour in summary
        :param product_brand: str, name of product brand
        :param product_name: str, name of product name
        :return: str of product colour in summary
        """
        shopping_cart_item = self.get_returned_item_from_summary_by_product_name(
            product_brand, product_name
        )
        return shopping_cart_item.find_element(*self.SUMMARY_PRODUCT_COLOUR).text

    @allure.step("Get text of product size in summary")
    def get_text_of_product_size_in_summary(
        self, product_brand: str, product_name: str
    ) -> str:
        """
        Get text of product size in summary
        :param product_brand: str, name of product brand
        :param product_name: str, name of product name
        :return: str of product size
        """
        shopping_cart_item = self.get_returned_item_from_summary_by_product_name(
            product_brand, product_name
        )
        return shopping_cart_item.find_element(*self.SUMMARY_PRODUCT_SIZE).text

    @allure.step("Get text of product quantity in summary")
    def get_text_of_product_quantity(
        self, product_brand: str, product_name: str
    ) -> str:
        """
        Get text of product quantity  in summary
        :param product_brand: str, name of product brand
        :param product_name: str, name of product name
        :return: str of product quantity
        """
        shopping_cart_item = self.get_returned_item_from_summary_by_product_name(
            product_brand, product_name
        )
        return shopping_cart_item.find_element(*self.SUMMARY_PRODUCT_QUANTITY).text

    @allure.step("Get text of product price in summary")
    def get_text_of_product_price_in_summary(
        self, product_brand: str, product_name: str
    ) -> str:
        """
        Get text of product price in summary
        :param product_brand: str, name of product brand
        :param product_name: str, name of product name
        :return: str of product price
        """
        shopping_cart_item = self.get_returned_item_from_summary_by_product_name(
            product_brand, product_name
        )
        return shopping_cart_item.find_element(*self.SUMMARY_PRODUCT_PRICE).text

    @allure.step("Get text of all products price in summary")
    def get_text_of_all_products_price_in_summary(self) -> str:
        """
        Get text of all products price in summary
        :return: str of all products price
        """
        return self.get_text_of(self.SUMMARY_ALL_PRODUCTS_PRICE)

    @allure.step("Get text of shipping price in summary")
    def get_text_of_shipping_price_in_summary(self) -> str:
        """
        Get text of shipping price in summary
        :return: str of shipping price
        """
        return self.get_text_of(self.SUMMARY_SHIPPING_PRICE)

    @allure.step("Get text of total price in summary")
    def get_text_of_total_price_in_summary(self) -> str:
        """
        Get text of total price in summary
        :return: str of total price
        """
        return self.get_text_of(self.SUMMARY_TOTAL_PRICE)

    @allure.step("Get text of validation error in payment method with card")
    def get_text_of_validation_message_pay_card(self) -> str:
        """
        Get text of validation error in payment method with card.
        :return: str of validation error
        """
        return self.get_text_of(self.VALIDATION_MESSAGE_PAY_CARD)
