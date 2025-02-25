from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument('--window-size=400,1080')
chrome_driver = webdriver.Chrome(options=options)
chrome_driver.get('https://demoqa.com/automation-practice-form')

first_name_field = chrome_driver.find_element(By.ID, 'firstName')
first_name_field.send_keys('Vladislav')

last_name_field = chrome_driver.find_element(By.ID, 'lastName')
last_name_field.send_keys('Zenevsky')

email_field = chrome_driver.find_element(By.ID, 'userEmail')
email_field.send_keys('test@test.com')

male_gender_radio_button = chrome_driver.find_element(By.XPATH, '//*[@for="gender-radio-1"]')
male_gender_radio_button.click()

mobile_field = chrome_driver.find_element(By.ID, 'userNumber')
mobile_field.send_keys('4849903800')

date_of_birth_field = chrome_driver.find_element(By.ID, 'dateOfBirthInput')
date_of_birth_field.click()
date_picker_month_march = chrome_driver.find_element(
    By.XPATH,
    '//*[@class="react-datepicker__month-select"]/option[text()="March"]'
)
date_picker_month_march.click()
date_picker_year_1995 = chrome_driver.find_element(
    By.XPATH,
    '//*[@class="react-datepicker__year-select"]/option[text()="1995"]'
)
date_picker_year_1995.click()
date_picker_day_2 = chrome_driver.find_element(
    By.XPATH,
    '//*[@class="react-datepicker__day react-datepicker__day--002"]'
)
date_picker_day_2.click()
subjects_selector = chrome_driver.find_element(
    By.XPATH,
    '//*[@id="subjectsInput"]'
)

subjects_selector.send_keys('comp')
subjects_selector.send_keys(Keys.ENTER)

music_checkbox = chrome_driver.find_element(By.XPATH, '//label[@for="hobbies-checkbox-3"]')
music_checkbox.click()

current_address_field = chrome_driver.find_element(By.ID, 'currentAddress')
current_address_field.send_keys('Address')

state_selector = chrome_driver.find_element(
    By.XPATH,
    '//*[text()="Select State"]/..//input[@id="react-select-3-input"]'
)
state_selector.send_keys('NCR')
state_selector.send_keys(Keys.ENTER)

city_selector = chrome_driver.find_element(
    By.XPATH,
    '//*[text()="Select City"]/..//input[@id="react-select-4-input"]'
)
city_selector.send_keys('Noida')
city_selector.send_keys(Keys.ENTER)

submit_button = chrome_driver.find_element(By.ID, 'submit')
submit_button.click()
