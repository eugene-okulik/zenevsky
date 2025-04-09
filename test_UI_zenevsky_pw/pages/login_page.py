from test_UI_zenevsky_pw.pages.base_page import BasePage
from test_UI_zenevsky_pw.pages.locators import login_locators as loc
from playwright.sync_api import expect


class LoginPage(BasePage):
    page_url = '/customer/account/login/'

    def check_page_header_title_is(self, text):
        header_title = self.find(loc.header_title_loc)
        expect(header_title).to_have_text(text)

    def error_message_is(self, text):
        error_message = self.find(loc.error_message)
        expect(error_message).to_have_text(text)
