import pytest


@pytest.mark.high
def test_check_email_already_exists_error(create_account_page):
    create_account_page.open_page()
    create_account_page.fill_login_form(
        first_name='first',
        last_name='last',
        email='test@test.ru',
        password='1234567890-aAa'
    )
    create_account_page.error_message_is(
        'There is already an account with this email address. '
        'If you are sure that it is your email address, '
        'click here to get your password and access your account.')


@pytest.mark.critical
def test_create_new_account(create_account_page, account_page):
    create_account_page.open_page()
    create_account_page.fill_login_form(
        first_name='first',
        last_name='last',
        password='1234567890-aAa'
    )
    account_page.success_message_is('Thank you for registering with Main Website Store.')


@pytest.mark.low
def test_check_bad_confirm_password_error_message(create_account_page):
    create_account_page.open_page()
    create_account_page.fill_first_name_field('first')
    create_account_page.fill_last_name_field('last')
    create_account_page.fill_email_field()
    create_account_page.fill_password_field('1234567890-aAa')
    create_account_page.fill_confirm_password_field('bad_password:(')
    create_account_page.click_to_the_create_an_account_button()
    create_account_page.password_confirmation_error_is('Please enter the same value again.')
