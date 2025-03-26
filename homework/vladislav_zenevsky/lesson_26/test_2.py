from playwright.sync_api import Page


def test_submit_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.get_by_placeholder('First Name').fill('Vladislav')
    page.get_by_placeholder('Last Name').fill('Zenevsky')
    page.locator('//*[@id="userEmail"]').fill('test@test.ru')
    page.locator('//*[@for="gender-radio-1"]').click()
    page.get_by_role('textbox', name='Mobile Number').fill('4849903800')
    page.locator('//*[@id="dateOfBirthInput"]').fill('02.03.1995')
    subjects_input = page.locator('//*[@id="subjectsInput"]')
    subjects_input.fill('comp')
    subjects_input.press(key='Enter')
    page.get_by_text('Music').click()
    page.get_by_placeholder('Current Address').fill('Current Address')
    page.get_by_text('Select State').click()
    page.get_by_text('NCR', exact=True).click()
    page.get_by_text('Select City').click()
    page.get_by_text('Noida', exact=True).click()
    page.get_by_role('button', name='Submit').click()
