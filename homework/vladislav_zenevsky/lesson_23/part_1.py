from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver = webdriver.Chrome()
chrome_driver.maximize_window()
chrome_driver.get('https://www.qa-practice.com/elements/input/simple')

text_string = chrome_driver.find_element(By.ID, 'id_text_string')
text_string.send_keys('test')
text_string.submit()

result_text = chrome_driver.find_element(By.ID, 'result-text').text

print(result_text)
