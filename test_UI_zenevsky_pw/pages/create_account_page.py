from random import randint

from test_UI_zenevsky_pw.pages.base_page import BasePage
from test_UI_zenevsky_pw.pages.locators import create_account_locators as loc
from playwright.sync_api import expect


class CreateAccountPage(BasePage):
    page_url = '/customer/account/create/'

    def check_page_header_title_is(self, text):
        header_title = self.page.get_by_role(loc.header_title_loc)
        expect(header_title).to_have_text(text)

    def fill_login_form(self, first_name, last_name, password, email=None):
        self.fill_first_name_field(first_name)
        self.fill_last_name_field(last_name)
        self.fill_email_field(email)
        self.fill_password_field(password)
        self.fill_confirm_password_field(password)
        self.click_to_the_create_an_account_button()

    def fill_first_name_field(self, first_name):
        first_name_field = self.page.get_by_test_id(loc.first_name_field)
        first_name_field.fill(first_name)

    def fill_last_name_field(self, last_name):
        last_name_field = self.page.get_by_test_id(loc.last_name_field)
        last_name_field.fill(last_name)

    def fill_email_field(self, email=None):
        email = email if email else f'test{randint(10000000000, 9999999999999)}@test.com'
        email_field = self.page.get_by_test_id(loc.email_field)
        email_field.fill(email)

    def fill_password_field(self, password):
        password_field = self.page.get_by_test_id(loc.password_field)
        password_field.fill(password)

    def fill_confirm_password_field(self, password):
        confirm_password_field = self.page.get_by_test_id(loc.confirm_password_field)
        confirm_password_field.fill(password)

    def click_to_the_create_an_account_button(self):
        self.find(loc.create_an_account_button).click()

    def error_message_is(self, text):
        error_message = self.find(loc.error_message)
        expect(error_message).to_have_text(text)

    def password_confirmation_error_is(self, text):
        password_confirmation_error = self.page.get_by_test_id(loc.password_confirmation_error)
        expect(password_confirmation_error).to_have_text(text)
