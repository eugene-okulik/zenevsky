from playwright.sync_api import expect
from test_UI_zenevsky_pw.pages.base_page import BasePage
from test_UI_zenevsky_pw.pages.locators import account_locators as loc


class AccountPage(BasePage):
    page_url = '/customer/account'

    def check_page_header_title_is(self, text):
        header_title = self.find(loc.header_title_loc)
        expect(header_title).to_have_text(text)

    def success_message_is(self, text):
        success_message = self.find(loc.success_message)
        expect(success_message).to_have_text(text)
