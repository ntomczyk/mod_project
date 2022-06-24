import os
import time
import allure
import pytest
from pageobjects.main_page import MainPage
from pageobjects.women_menu_page import WomenMenu
from pageobjects.women_clothes_page import WomenClothes
from pageobjects.clothes_filters import ClothesFilters
from pageobjects.products_list_items_page import  ProductsListItems
from common_actions import CommonActions

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
        product_list_item = ProductsListItems(driver)
        common_actions = CommonActions(driver)

        base_modivo_url = os.getenv("BASE_URL")

        main_page.open_page(url=base_modivo_url)
        main_page.wait_for_expected_url(expected_url=base_modivo_url)
        main_page.close_modal_message_if_exists()
        current_url = self.driver.current_url
        main_page.click_on_women_in_top_menu()
        main_page.wait_for_page_loading(current_url)
        time.sleep(3)
        women_menu.click_on_women_menu_category_clothes()
        current_url = self.driver.current_url
        women_clothes.click_on_women_tops_and_shirts()
        common_actions.close_promotion_message_if_exists()
        main_page.wait_for_page_loading(current_url)
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
        # product_list_item.get_returned_item(1)
        text_of_badge_offer = product_list_item.get_text_of_product_badge_offer(1)
        text_of_product_base_badge_offer = product_list_item.get_text_of_product_base_badge_offer(1)
        text_of_product_brand = product_list_item.get_text_of_product_brand(1)
        text_of_product_name = product_list_item.get_text_of_product_name(1)
        text_of_product_price = product_list_item.get_text_of_product_price(1)
        product_list_item.go_to_product_details(1)




