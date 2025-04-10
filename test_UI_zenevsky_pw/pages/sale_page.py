from test_UI_zenevsky_pw.pages.base_page import BasePage
from test_UI_zenevsky_pw.pages.locators import sale_locators as loc
from playwright.sync_api import expect


class SalePage(BasePage):
    page_url = '/sale.html'

    def click_to_the_women_sale_link(self):
        self.find(loc.women_sale_link).click()

    def click_to_the_mens_bargains_link(self):
        self.find(loc.mens_bargains).click()

    def check_t_shirts_block_title_text_is(self, text):
        expect(self.find(loc.t_shirts_block_title)).to_have_text(text)
