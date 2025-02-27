import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver


def test_first(driver):
    driver.get('https://www.demoblaze.com/index.html')

    samsung_card_title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[text()="Samsung galaxy s6"]')))

    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL)
    actions.click(samsung_card_title)
    actions.key_up(Keys.CONTROL)
    actions.perform()

    tabs = driver.window_handles

    driver.switch_to.window(tabs[1])

    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[text()="Add to cart"]')))
    add_to_cart_button.click()

    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert.accept()

    driver.close()

    driver.switch_to.window(tabs[0])

    cart_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'cartur')))
    cart_link.click()

    product = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//*[text()="Samsung galaxy s6"]')
    ))

    assert product.text == "Samsung galaxy s6"


def test_second(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')

    products = driver.find_elements(By.CLASS_NAME, 'product-item')

    first_product = products[0]
    first_product_name = first_product.find_element(By.CLASS_NAME, 'name').text

    add_to_compare_button = WebDriverWait(first_product, 10).until(EC.presence_of_element_located(
        (By.CLASS_NAME, 'tocompare')))

    actions = ActionChains(driver)
    actions.move_to_element(first_product)
    actions.move_to_element(add_to_compare_button)
    actions.click()
    actions.perform()

    assert WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="compare-items"]//*[@class="product-item-link"]'))).text == first_product_name
