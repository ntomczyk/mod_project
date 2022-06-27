import os
import re
import allure
import pytest
from pageobjects.main_page import MainPage
from pageobjects.women_menu_page import WomenMenu
from pageobjects.women_clothes_page import WomenClothes
from pageobjects.clothes_filters_page import ClothesFilters
from pageobjects.products_items_list_page import ProductsItemsList
from pageobjects.product_details_page import ProductsDetails
from pageobjects.modal_added_to_cart_confirmation_page import (
    ModalAddedToCardConfirmation,
)
from pageobjects.shopping_cart_page import ShoppingCart
from pageobjects.common_actions import CommonActions
from pageobjects.checkout_account_page import CheckoutAccount
from pageobjects.checkout_page import Checkout
from faker import Faker


@pytest.mark.usefixtures("setup")
class TestOrderProcess:
    @allure.title("Order Process - incorrect card number")
    @allure.description(
        "Check the full ordering process - choosing women's t-shirts, check prices, adding items to a shopping card,"
        " method of delivery and payment, entering the wrong card number"
    )
    @pytest.mark.test_id(1)
    def test_check_order_process_with_invalid_card_number(self, record_property):

        record_property(
            "Description",
            "Check the full ordering process - choosing women's t-shirts, check prices, adding items to a shopping card,"
            " method of delivery and payment, entering the wrong card number",
        )

        driver = self.driver
        main_page = MainPage(driver)
        women_menu = WomenMenu(driver)
        women_clothes = WomenClothes(driver)
        clothes_filters = ClothesFilters(driver)
        product_item_list = ProductsItemsList(driver)
        common_actions = CommonActions(driver)
        product_details = ProductsDetails(driver)
        modal_added_to_card_confirmation = ModalAddedToCardConfirmation(driver)
        shopping_cart = ShoppingCart(driver)
        checkout_account = CheckoutAccount(driver)
        checkout = Checkout(driver)
        fake = Faker(os.getenv("FAKER_LOCATE"))

        base_modivo_url = os.getenv("BASE_URL")
        size = "38"
        invalid_card_number = "4111 1111 1111 1111"

        # Open main modivo page and go to women clothes
        main_page.open_page(url=base_modivo_url)
        main_page.wait_for_expected_url(expected_url=base_modivo_url)
        main_page.close_modal_message_if_exists()
        current_url = self.driver.current_url
        main_page.click_on_women_in_top_menu()
        main_page.wait_for_page_loading(current_url)
        women_menu.click_on_women_menu_category_clothes()
        current_url = self.driver.current_url

        # Choose women_tops_and_shirts
        women_clothes.click_on_women_tops_and_shirts()
        common_actions.close_promotion_message_if_exists()
        main_page.wait_for_page_loading(current_url)
        assert (
            women_clothes.get_text_of_title_clothes_types()
            == common_actions.get_expression_from_language_dictionary(
                "title_women_tops_and_shirts"
            )
        )
        # Choose size
        clothes_filters.choose_filter_size()
        clothes_filters.choose_upper_clothing()
        clothes_filters.check_size(given_size="M:38")
        clothes_filters.click_on_apply_button()
        main_page.wait_for_page_loading(current_url)

        # Choose news
        clothes_filters.choose_filter_offer()
        current_url = self.driver.current_url
        clothes_filters.check_option_news()
        clothes_filters.click_on_apply_button()
        main_page.wait_for_page_loading(current_url)

        # Get text of given product data
        random_item = product_item_list.get_random_item()
        text_of_product_brand = product_item_list.get_text_of_product_brand(random_item)
        text_of_product_name = product_item_list.get_text_of_product_name(random_item)
        text_of_product_price = product_item_list.get_text_of_product_price(random_item)
        text_of_regular_price_before_discount = product_item_list.check_if_product_has_discount_and_get_text_of_regular_price(
            random_item
        )
        discount = (
            product_item_list.check_if_product_has_discount_and_get_text_of_discount(
                random_item
            )
        )

        # Go to product details and check data
        product_item_list.go_to_product_details(random_item)
        assert (
            text_of_product_brand
            == product_details.get_text_of_product_details_brand_name()
        )
        assert (
            text_of_product_name == product_details.get_text_of_product_details_name()
        )
        if text_of_regular_price_before_discount:
            assert (
                text_of_regular_price_before_discount
                == product_details.get_text_of_product_details_regular_price()
            )
            assert discount == product_details.get_text_of_product_details_discount()
            assert (
                text_of_product_price
                == product_details.get_text_of_product_details_final_price()
            )
        else:
            assert (
                text_of_product_price
                == product_details.get_text_of_product_details_price()
            )
        text_of_product_details_colour = (
            product_details.get_text_of_product_details_colour()
        )
        # Choose given size and add product to card
        product_details.click_on_choose_size_button()
        product_details.click_chosen_size_product_details(size=size)
        product_details.add_product_to_cart()
        modal_added_to_card_confirmation.click_on_go_to_cart_button()
        main_page.wait_for_expected_url(expected_url=base_modivo_url + "checkout/cart")

        # Check data in shopping cart
        text_of_shopping_cart_title = shopping_cart.get_text_of_shopping_cart_title()
        text_of_product_size_in_shopping_cart = (
            shopping_cart.get_text_of_product_size_in_shopping_cart(
                product_brand=text_of_product_brand, product_name=text_of_product_name
            )
        )
        assert (
            text_of_shopping_cart_title
            == common_actions.get_expression_from_language_dictionary(
                "shopping_card_title"
            )
            + " (1)"
        )
        assert (
            text_of_product_brand
            == shopping_cart.get_text_of_product_brand_name_in_shopping_cart(
                product_brand=text_of_product_brand, product_name=text_of_product_name
            )
        )
        assert (
            text_of_product_brand.title() + " " + text_of_product_name
            == shopping_cart.get_text_of_product_name_in_shopping_cart(
                product_brand=text_of_product_brand, product_name=text_of_product_name
            )
        )
        assert text_of_product_details_colour == re.sub(
            r"^\W*\w+\W*",
            "",
            shopping_cart.get_text_of_product_colour_in_shopping_cart(
                product_brand=text_of_product_brand, product_name=text_of_product_name
            ),
        )
        if text_of_regular_price_before_discount:
            assert (
                text_of_regular_price_before_discount
                == shopping_cart.get_text_of_product_regular_price_in_shopping_cart(
                    product_brand=text_of_product_brand,
                    product_name=text_of_product_name,
                )
            )
            assert discount == shopping_cart.get_text_of_discount(
                product_brand=text_of_product_brand, product_name=text_of_product_name
            )
            assert (
                text_of_product_price
                == shopping_cart.get_text_of_product_price_in_shopping_cart(
                    product_brand=text_of_product_brand,
                    product_name=text_of_product_name,
                )
            )
        else:
            assert (
                text_of_product_price
                == shopping_cart.get_text_of_product_price_in_shopping_cart(
                    product_brand=text_of_product_brand,
                    product_name=text_of_product_name,
                )
            )

        assert (
            text_of_product_price
            == shopping_cart.get_text_of_products_summary_price_in_shopping_cart()
        )
        assert (
            text_of_product_price
            == shopping_cart.get_text_of_products_total_price_in_shopping_cart()
        )

        # Go to account checkout
        shopping_cart.click_on_proceed_to_payment_button()
        main_page.wait_for_expected_url(
            expected_url=base_modivo_url + "checkout/account"
        )
        checkout_account.click_on_continue_as_guest_button()
        common_actions.wait_for_account_checkout_loader()
        main_page.wait_for_expected_url(expected_url=base_modivo_url + "checkout")

        # Product summary
        assert (
            text_of_product_brand
            == checkout.get_text_of_product_brand_name_in_summary(
                product_brand=text_of_product_brand, product_name=text_of_product_name
            )
        )
        assert (
            text_of_product_brand + " " + text_of_product_name
        ).title() == checkout.get_text_of_product_name_in_summary(
            product_brand=text_of_product_brand, product_name=text_of_product_name
        ).title()
        assert (
            text_of_product_size_in_shopping_cart
            == checkout.get_text_of_product_size_in_summary(
                product_brand=text_of_product_brand, product_name=text_of_product_name
            )
        )
        assert text_of_product_details_colour == re.sub(
            r"^\W*\w+\W*",
            "",
            checkout.get_text_of_product_colour_in_summary(
                product_brand=text_of_product_brand, product_name=text_of_product_name
            ),
        )
        assert (
            re.sub(
                r"^\W*\w+\W*",
                "",
                checkout.get_text_of_product_quantity(
                    product_brand=text_of_product_brand,
                    product_name=text_of_product_name,
                ),
            )
            == "1"
        )

        assert (
            text_of_product_price
            == checkout.get_text_of_all_products_price_in_summary()
        )
        assert text_of_product_price == checkout.get_text_of_total_price_in_summary()

        # Fill in customer data
        checkout.enter_customer_email(email=fake.ascii_email())
        checkout.enter_customer_phone(phone=fake.phone_number())
        checkout.enter_customer_name(name=fake.first_name())
        checkout.enter_customer_surname(surname=fake.last_name())
        checkout.enter_customer_street(street=fake.street_address())
        checkout.enter_customer_house_number(house_no=fake.building_number())
        checkout.enter_customer_apartment_number(apartment_no=fake.building_number())
        checkout.enter_customer_post_code(post_code=fake.postcode())
        checkout.enter_customer_city(city=fake.city())

        # Choose DHL as shipping method
        checkout.check_dhl_shipping_method()
        common_actions.wait_for_checkout_loader()

        # Choose card as payment method and fill in invalid card data
        checkout.check_payment_method_card()
        common_actions.wait_for_checkout_loader()
        # Switch to iframes

        checkout.enter_card_number(card_number=invalid_card_number)
        driver.switch_to.default_content()
        checkout.enter_card_expiration_date(card_date=fake.credit_card_expire())
        driver.switch_to.default_content()
        checkout.enter_cvv_code(cvv_code=fake.credit_card_security_code())
        driver.switch_to.default_content()
        # Check required terms

        checkout.check_required_terms()
