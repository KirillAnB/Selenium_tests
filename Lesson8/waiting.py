import selenium.webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

base_url = 'https://parsinger.ru/expectations/1/index.html'

with selenium.webdriver.Chrome() as browser:
    browser.get(url=base_url)
    tricky_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'btn')))
    tricky_button.click()
    result = browser.find_element(By.ID, 'result').text
    print(result)


