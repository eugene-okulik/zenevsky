import pytest
from playwright.sync_api import Page, BrowserContext
from test_UI_zenevsky_pw.pages.sale_page import SalePage
from test_UI_zenevsky_pw.pages.create_account_page import CreateAccountPage
from test_UI_zenevsky_pw.pages.eco_friendly_page import EcoFriendlyPage
from test_UI_zenevsky_pw.pages.women_sale_page import WomenSalePage
from test_UI_zenevsky_pw.pages.men_sale_page import MenSalePage
from test_UI_zenevsky_pw.pages.login_page import LoginPage
from test_UI_zenevsky_pw.pages.account_page import AccountPage


@pytest.fixture()
def page(context: BrowserContext, playwright):
    playwright.selectors.set_test_id_attribute("id")
    page = context.new_page()
    page.set_viewport_size({'width': 1920, 'height': 1080})
    return page


@pytest.fixture()
def sale_page(page):
    return SalePage(page)


@pytest.fixture()
def create_account_page(page):
    return CreateAccountPage(page)


@pytest.fixture()
def eco_friendly_page(page):
    return EcoFriendlyPage(page)


@pytest.fixture()
def women_sale_page(page):
    return WomenSalePage(page)


@pytest.fixture()
def men_sale_page(page):
    return MenSalePage(page)


@pytest.fixture()
def login_page(page):
    return LoginPage(page)

@pytest.fixture()
def account_page(page):
    return AccountPage(page)