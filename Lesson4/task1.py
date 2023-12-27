import time
from selenium import webdriver


base_url = "http://parsinger.ru/scroll/1/"

with webdriver.Chrome() as browser:
    browser.get(base_url)
    time.sleep(2)
    browser.maximize_window()
    time.sleep(2)
    browser.execute_script("window.scrollBy(0,5000)")
    time.sleep(2)
    browser.execute_script("window.scrollBy(0,10000)")
    time.sleep(2)

