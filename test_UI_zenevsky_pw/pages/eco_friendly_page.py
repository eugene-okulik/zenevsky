import re
from typing import Literal

from test_UI_zenevsky_pw.pages.base_page import BasePage
from test_UI_zenevsky_pw.pages.locators import eco_friendly_locators as loc
from playwright.sync_api import expect

SortOption = Literal["Price", "Position", "Product Name"]


class EcoFriendlyPage(BasePage):
    page_url = '/collections/eco-friendly.html'

    def check_page_header_title_is(self, text):
        header_title = self.find(loc.header_title_loc)
        expect(header_title).to_have_text(text)

    def choose_the_size_28(self, item_number):
        items = self.find_all(loc.items)
        for item in items:
            expect(item).to_be_visible()
        if item_number >= len(items):
            raise ValueError(f"Item number {item_number} is out of range. Total items: {len(items)}")
        item = items[item_number]
        item.hover()
        item.page.get_by_test_id(loc.size_28).first.click()

    def choose_color_black(self, item_number):
        items = self.find_all(loc.items)
        for item in items:
            expect(item).to_be_visible()
        if item_number >= len(items):
            raise ValueError(f"Item number {item_number} is out of range. Total items: {len(items)}")
        item = items[item_number]
        item.hover()
        item.page.get_by_test_id(loc.color_black).first.click()

    def click_to_the_add_to_cart_button(self, item_number):
        items = self.find_all(loc.items)
        for item in items:
            expect(item).to_be_visible()
        if item_number >= len(items):
            raise ValueError(f"Item number {item_number} is out of range. Total items: {len(items)}")
        item = items[item_number]
        item.hover()
        add_to_cart_button = item.locator(loc.add_to_cart_button).first
        add_to_cart_button.hover()
        add_to_cart_button.click()

    def click_to_the_add_to_wishlist_button(self, item_number):
        items = self.find_all(loc.items)
        for item in items:
            expect(item).to_be_visible()
        if item_number >= len(items):
            raise ValueError(f"Item number {item_number} is out of range. Total items: {len(items)}")
        item = items[item_number]
        item.hover()
        add_to_wishlist_button = item.locator(loc.add_to_wishlist_button).first
        add_to_wishlist_button.hover()
        add_to_wishlist_button.click()

    def check_that_cart_is_not_empty(self):
        cart_counter = self.find(loc.cart_counter)
        expect(cart_counter).to_have_text('1')

    def choose_sorting_by(self, label: SortOption):
        if label not in ('Price', 'Position', 'Product Name'):
            raise ValueError(f'Invalid sort option: {label}. Must be "Price", "Position" or "Product Name"')
        items = self.find_all(loc.items)
        for item in items:
            expect(item).to_be_visible()
        sorter = self.page.get_by_label(loc.sort_by_selector)
        sorter.click()
        sorter.select_option(label=label)
        expect(self.page).to_have_url(re.compile('price'))

    def check_sorting_by_price(self):
        items = self.find_all(loc.items)
        prices = []
        for item in items:
            price_element = item.locator(loc.price)
            prices.append(price_element.text_content())
        price_nums = [float(i.strip('$')) for i in prices]
        assert price_nums == sorted(price_nums)
