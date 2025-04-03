import json
import re

from playwright.sync_api import Page, expect, Route


def test_change_response(page: Page):
    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = 'яблокофон 16 про'
        body = json.dumps(body)
        route.fulfill(
            body=body
        )

    page.route(re.compile('/digital-mat'), handle_route)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.get_by_role("heading", name='iPhone 16 Pro & iPhone 16 Pro').click()
    title = page.locator('//*[@data-autom="DigitalMat-overlay-header-0-0"]')
    expect(title).to_have_text('яблокофон 16 про')
