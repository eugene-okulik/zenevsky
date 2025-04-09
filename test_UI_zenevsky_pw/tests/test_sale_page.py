import pytest


@pytest.mark.medium
def test_check_link_to_women_sale(sale_page, women_sale_page):
    sale_page.open_page()
    sale_page.click_to_the_women_sale_link()
    women_sale_page.check_page_header_title_is('Women Sale')


@pytest.mark.medium
def test_check_link_to_mens_bargains(sale_page, men_sale_page):
    sale_page.open_page()
    sale_page.click_to_the_mens_bargains_link()
    men_sale_page.check_page_header_title_is('Men Sale')


@pytest.mark.low
def test_check_t_shirts_block_title_text(sale_page):
    sale_page.open_page()
    sale_page.check_t_shirts_block_title_text_is("You can't have too many tees")
