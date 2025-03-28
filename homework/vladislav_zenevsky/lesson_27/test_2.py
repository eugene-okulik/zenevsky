from playwright.sync_api import Page, expect, BrowserContext


def test_new_tab(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    link = page.get_by_role('link', name='Click')
    with context.expect_page() as new_page_event:
        link.click()
    new_page = new_page_event.value
    result_text = new_page.locator('#result-text')
    expect(result_text).to_have_text('I am a new page in a new tab')
    expect(link).to_be_enabled()
