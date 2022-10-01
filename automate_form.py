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


# Reading the data from fake data
import pandas as pd

df = pd.read_csv('fake_data.csv')
print(df)

number_of_row = len(df)

for i in range(0, number_of_row):
    for column in df.columns:
        # Basically trying to find the element

        # inputing the value for the find_element
        value_input = f'//div[contains(@data-params, "{column}")]//input | //div[contains(@data-params, "{column}")]//textarea'
        value_submit = f'//div[@role="button"]//span[text()="Submit"]'

        text_input = driver.find_element(by='xpath', value=value_input)
        text_input.send_keys(df.loc[i, column])

    #Clicking the submit button
    submit_button = driver.find_element(by='xpath', value=value_submit)
    submit_button.click()

driver.quit()