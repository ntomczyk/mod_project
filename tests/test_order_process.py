import os
import time
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


@pytest.mark.usefixtures("setup")
class TestOrderProcess:
    @allure.title("Order Process - incorrect card number")
    @allure.description(
        "Check the full ordering process - choosing women's t-shirts, check prices, adding items to a shopping card, method of delivery and payment, entering the wrong card number"
    )
    @pytest.mark.test_id(1)
    def test_check_order_process_with_invalid_card_number(self, record_property):

        record_property(
            "Description",
            "Check the full ordering process - choosing women's t-shirts, check prices, adding items to a shopping card, method of delivery and payment, entering the wrong card number",
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
        checkout_account = CheckoutAccount()

        base_modivo_url = os.getenv("BASE_URL")
        size = "38"
        invalid_card_number = "4111 1111 1111 1111"

        map_38_size = ["38", "M"]
        dict_size_38 = {size: map_38_size}

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
        # TO DO
        assert (
            women_clothes.get_text_of_title_clothes_types()
            == "Bluzki i koszule damskie"
        )
        # Choose size
        clothes_filters.choose_filter_size()
        clothes_filters.choose_upper_clothing()
        clothes_filters.check_size(given_size="M:38")
        clothes_filters.click_on_apply_button()
        main_page.wait_for_page_loading(current_url)
        time.sleep(2)
        clothes_filters.choose_filter_offer()
        # Choose news
        clothes_filters.check_option_news()
        clothes_filters.click_on_apply_button()
        # Get text of given product data
        time.sleep(5)
        text_of_product_base_badge_offer = (
            product_item_list.get_text_of_product_base_badge_offer(1)
        )
        text_of_product_brand = product_item_list.get_text_of_product_brand(1)
        text_of_product_name = product_item_list.get_text_of_product_name(1)
        print(text_of_product_name)
        text_of_product_price = product_item_list.get_text_of_product_price(1)
        text_of_discount_price = product_item_list.check_if_product_has_discount_and_get_text_of_discount_price(
            1
        )
        text_of_discount = (
            product_item_list.check_if_product_has_discount_and_get_text_of_discount(1)
        )
        print(text_of_product_base_badge_offer)
        # assert "NOWOŚĆ" in text_of_product_base_badge_offer
        # # Go to product details and check data
        product_item_list.go_to_product_details(1)
        assert (
            text_of_product_brand
            == product_details.get_text_of_product_details_brand_name()
        )
        assert (
            text_of_product_name == product_details.get_text_of_product_details_name()
        )
        if text_of_discount_price:
            assert (
                text_of_discount_price
                == product_details.get_text_of_product_details_regular_price()
            )
            assert (
                text_of_discount
                == product_details.get_text_of_product_details_discount()
            )
            assert (
                text_of_product_price
                == product_details.get_text_of_product_details_final_price()
            )
        else:
            assert (
                text_of_product_price
                == product_details.get_text_of_product_details_price()
            )
        product_details.click_on_choose_size_button()
        product_details.click_chosen_size_product_details("38")
        product_details.add_product_to_cart()
        modal_added_to_card_confirmation.click_on_go_to_cart_button()
        main_page.wait_for_expected_url(expected_url=base_modivo_url + "checkout/cart")
        text_of_shopping_cart_title = shopping_cart.get_text_of_shopping_cart_title()
        shopping_cart.get_text_of_product_brand_name_in_shopping_cart()
        shopping_cart.get_text_of_product_name_in_shopping_cart()
        shopping_cart.get_text_of_product_colour_in_shopping_cart()
        shopping_cart.get_text_of_product_size_in_shopping_cart()
        shopping_cart.get_text_of_product_quantity_and__price_in_shopping_cart()
        shopping_cart.get_text_of_product_price_in_shopping_cart()
        shopping_cart.get_text_of_products_summary_price_in_shopping_cart()
        shopping_cart.get_text_of_products_total_price_in_shopping_cart()

        assert text_of_shopping_cart_title == "Koszyk (1)"
        text_of_brand_name_in_shopping_cart = (
            shopping_cart.get_text_of_brand_name_in_shopping_cart(
                product_brand=text_of_product_brand, product_name=text_of_product_name
            )
        )
        assert text_of_product_brand == text_of_brand_name_in_shopping_cart
        shopping_cart.click_on_proceed_to_payment_button()
        main_page.wait_for_expected_url(
            expected_url=base_modivo_url + "checkout/account"
        )
        checkout_account.click_on_continue_as_guest_button()
        main_page.wait_for_expected_url(
            expected_url=base_modivo_url + "checkout"
        )
