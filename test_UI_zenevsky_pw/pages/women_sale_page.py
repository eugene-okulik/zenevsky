from test_UI_zenevsky_pw.pages.base_page import BasePage
from test_UI_zenevsky_pw.pages.locators import women_sale_locators as loc
from playwright.sync_api import expect


class WomenSalePage(BasePage):
    page_url = '/promotions/women-sale.html'

    def check_page_header_title_is(self, text):
        header_title = self.find(loc.header_title_loc)
        expect(header_title).to_have_text(text)
