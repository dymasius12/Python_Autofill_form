from operator import contains
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
import time 

path = '/Users/dymasius/Sandbox/Python-Dev/development/python_autofill_form/chromedriver'
service = Service(executable_path = path)
website = 'https://forms.gle/CJf4QapkiA7s7HcZ7'
driver = webdriver.Chrome(service=service)

driver.get(website)
time.sleep(3)

# inputing the value for the find_element
value_input = '//div[contains(@data-params, "Address")]//input | //div[contains(@data-params, "Address")]//textarea'
value_submit = '//div[@role="button"]//span[text()="Submit"]'
# Basically trying to find the element
text_input = driver.find_element(by='xpath', value=value_input)
text_input.send_keys('Hello_World!')

submit_button = driver.find_element(by='xpath', value=value_submit)
submit_button.click()

driver.quit()