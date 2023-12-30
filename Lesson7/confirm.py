import selenium.webdriver
import time

base_url = 'http://parsinger.ru/blank/modal/1/index.html'

with selenium.webdriver.Chrome() as browser:
    browser.get(url=base_url)
    browser.find_element(selenium.webdriver.common.by.By.ID, 'confirm').click()
    confirm_window = browser.switch_to.alert
    confirm_window.accept()
    time.sleep(2)
