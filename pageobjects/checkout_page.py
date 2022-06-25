import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from pageobjects.base_page import BasePage


class Checkout(BasePage):

    # Customer data
    EMAIL = (By.CSS_SELECTOR, "[data-test-id='billing__email']")
    PHONE = (By.CSS_SELECTOR, "[data-test-id='billing__telephone']")
    NAME = (By.ID, "billing__firstname")
    SURNAME = (By.ID, "billing__lastname")
    STREET = (By.CSS_SELECTOR, "[data-test-id='billing__street-0']")
    HOUSE_NO = (By.CSS_SELECTOR, "[data-test-id='billing__street-1']")
    FLAT_NO = (By.CSS_SELECTOR, "[billing__street-2']")
    POST_CODE = (By.ID, "billing__postcode")
    CITY = (By.CSS_SELECTOR, "[data-test-id='billing__city']")

    # Shipping method
    DHL_CARRIER = (By.ID, "modivo_store_custom02")

    # Payment methods
    PAY_CARD = (By.ID, "payu_gateway_card")
    CARD_NUMBER = (By.ID, "card-number")
    CARD_DATE = (By.NAME, "expDate")
    CARD_CVV = (By.NAME, "cvv")

    # Required terms
    TERMS = (By.ID, "terms")



    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Click on continue as guest button")
    def click_on_continue_as_guest_button(self):

        """ Click on continue as guest button to go to the checkout page. """

        self.click_on(self.CONTINUE_AS_GUEST_BUTTON)
        allure.attach(self.driver.get_screenshot_as_png(), name="click_on_continue_as_guest_button",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Enter customer email")
    def enter_customer_email(self, email: str):
        """
        Enter customer email.
        :param email: str, customer email
        """
        self.enter_text(self.EMAIL, email)
        allure.attach(self.driver.get_screenshot_as_png(), name="enter_customer_email",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Enter customer email")
    def enter_customer_email(self, email: str):
        """
        Enter customer email.
        :param email: str, customer email
        """
        self.enter_text(self.PHONE, email)
        allure.attach(self.driver.get_screenshot_as_png(), name="enter_customer_email",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Enter customer name")
    def enter_customer_name(self, name: str):
        """
        Enter customer name.
        :param name: str, customer name
        """
        self.enter_text(self.NAME, name)
        allure.attach(self.driver.get_screenshot_as_png(), name="enter_customer_name",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Enter customer surname")
    def enter_customer_surname(self, surname: str):
        """
        Enter customer surname.
        :param surname: str, customer surname
        """
        self.enter_text(self.SURNAME, surname)
        allure.attach(self.driver.get_screenshot_as_png(), name="enter_customer_surname",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Enter customer street")
    def enter_customer_street(self, street: str):
        """
        Enter customer street.
        :param street: str, customer street
        """
        self.enter_text(self.STREET, street)
        allure.attach(self.driver.get_screenshot_as_png(), name="enter_customer_street",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Enter customer house number")
    def enter_customer_email(self, house_no: str):
        """
        Enter customer house number.
        :param house_no: str, customer house number
        """
        self.enter_text(self.HOUSE_NO, house_no)
        allure.attach(self.driver.get_screenshot_as_png(), name="enter_customer_house_no",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Enter customer flat number")
    def flat_no(self, flat_no: str):
        """
        Enter customer flat number.
        :param flat_no: str, customer flat number
        """
        self.enter_text(self.FLAT_NO, flat_no)
        allure.attach(self.driver.get_screenshot_as_png(), name="flat_no",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Enter customer post code")
    def enter_customer_post_code(self, post_code: str):
        """
        Enter customer post code.
        :param post_code: str, customer post_code
        """
        self.enter_text(self.POST_CODE, post_code)
        allure.attach(self.driver.get_screenshot_as_png(), name="enter_customer_post_code",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Enter customer city")
    def enter_customer_email(self, city: str):
        """
        Enter customer city.
        :param city: str, customer city
        """
        self.enter_text(self.CITY, city)
        allure.attach(self.driver.get_screenshot_as_png(), name="enter_customer_city",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Check DHL carrier")
    def check_dhl_carrier(self):

        """ Check checkbox with DHL shipping method. """

        self.click_on(self.DHL_CARRIER)
        allure.attach(self.driver.get_screenshot_as_png(), name="check_dhl_carrier",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Check payment method -card")
    def check_payment_method_card(self):
        """ Check checkbox with card payment method. """

        self.click_on(self.PAY_CARD)
        allure.attach(self.driver.get_screenshot_as_png(), name="check_payment_method_card",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Enter card number")
    def enter_card_number(self, card_number: str):
        """
        Enter customer card number.
        :param card_number: str, customer card number
        """
        self.enter_text(self.CARD_NUMBER, card_number)
        allure.attach(self.driver.get_screenshot_as_png(), name="enter_card_number",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Enter card expiration date8")
    def enter_card_expiration_date(self, card_date: str):
        """
        Enter customer card expiration date.
        :param card_date: str, customer card date
        """
        self.enter_text(self.CARD_DATE, card_date)
        allure.attach(self.driver.get_screenshot_as_png(), name="enter_card_expiration_date",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Enter cvv code")
    def enter_cvv_code(self, cvv_code: str):
        """
        Enter customer card cvv code.
        :param cvv_code: str, customer card cvv code
        """
        self.enter_text(self.CARD_CVV, cvv_code)
        allure.attach(self.driver.get_screenshot_as_png(), name="enter_cvv_code",
                      attachment_type=AttachmentType.PNG)

    @allure.step("Check required terms")
    def check_required_terms(self):
        """ Check checkbox with required terms. """

        self.click_on(self.TERMS)
        allure.attach(self.driver.get_screenshot_as_png(), name="check_required_terms",
                      attachment_type=AttachmentType.PNG)
