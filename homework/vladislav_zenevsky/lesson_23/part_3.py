import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--window-size=1920,1080')
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver


def test_result_text(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    language_selector = driver.find_element(By.ID, 'id_choose_language')
    language_selector.click()

    python_option = driver.find_element(By.XPATH, '//*[@id="id_choose_language"]/option[text()="Python"]')
    python_option.click()

    submit_button = driver.find_element(By.ID, 'submit-id-submit')
    submit_button.click()

    result_text = driver.find_element(By.ID, 'result-text').text
    assert result_text == 'Python'


def test_hello_world(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    start_button = driver.find_element(By.XPATH, '//*[@id="start"]//button')
    start_button.click()
    result_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="finish"]//h4[text()="Hello World!"]')))
    assert result_text.text == 'Hello World!'
