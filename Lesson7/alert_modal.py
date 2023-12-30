from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
import time

url = 'http://parsinger.ru/blank/modal/1/index.html'
with Chrome() as browser:
    browser.get(url=url)
    button = browser.find_element(By.ID, 'alert')
    time.sleep(2)
    button.click()
    time.sleep(2)
    allert = browser.switch_to.alert.text
    time.sleep(2)
    print(allert)
