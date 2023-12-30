from selenium import webdriver
import time

url = "https://google.ru"
with webdriver.Chrome() as browser:
    browser.get(url=url)
    browser.set_window_size(1200, 800)
    time.sleep(3)
