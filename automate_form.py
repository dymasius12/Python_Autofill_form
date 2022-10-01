from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 

path = '/Users/dymasius/Sandbox/Python-Dev/development/python_autofill_form/chromedriver'
service = Service(executable_path = path)
website = 'https://forms.gle/CJf4QapkiA7s7HcZ7'
driver = webdriver.Chrome(service=service)

driver.get(website)