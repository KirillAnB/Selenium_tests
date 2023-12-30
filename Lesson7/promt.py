import selenium.webdriver
import time

url = 'http://parsinger.ru/blank/modal/1/index.html'

with selenium.webdriver.Chrome() as browser:
    browser.get(url=url)
    browser.find_element(selenium.webdriver.common.by.By.ID, 'prompt').click()
    time.sleep(2)
    prompt = browser.switch_to.alert
    prompt.send_keys('Pussy lover 777')
    prompt.accept()
    time.sleep(1)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# with webdriver.Chrome() as browser:
#     browser.get('http://parsinger.ru/blank/modal/1/index.html')
#     browser.find_element(By.ID, 'prompt').click()
#     time.sleep(2)
#     prompt = browser.switch_to.alert
#     prompt.send_keys('Введёный текст')
#     time.sleep(2)
#     prompt.accept()
#     time.sleep(.5)
#     print(browser.find_element(By.ID, 'result').text)
