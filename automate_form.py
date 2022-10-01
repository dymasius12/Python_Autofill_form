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

value = '//div[contains(@data-params, "Address")]//input | //div[contains(@data-params, "Address")]//textarea'

# Basically trying to find the element
text_input = driver.find_element(by='xpath', value=value)

text_input.send_keys('Hello_World!')