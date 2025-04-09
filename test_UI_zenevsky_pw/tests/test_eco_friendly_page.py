import pytest


@pytest.mark.critical
def test_add_to_cart_the_first_item(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.choose_the_size_28(item_number=0)
    eco_friendly_page.choose_color_black(item_number=0)
    eco_friendly_page.click_to_the_add_to_cart_button(item_number=0)
    eco_friendly_page.check_that_cart_is_not_empty()


@pytest.mark.medium
def test_try_to_add_to_wishlist_by_unauthorized_user(eco_friendly_page, login_page):
    eco_friendly_page.open_page()
    eco_friendly_page.click_to_the_add_to_wishlist_button(item_number=0)
    login_page.error_message_is('You must login or register to add items to your wishlist.')


@pytest.mark.medium
def test_check_sorting_by_price(eco_friendly_page):
    eco_friendly_page.open_page()
    eco_friendly_page.choose_sorting_by('Price')
    eco_friendly_page.check_sorting_by_price()
