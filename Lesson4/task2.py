from selenium import webdriver
from time import sleep


get_height_script = "return document.body.scrollHeight"
get_window_height_script = "return window.innerHeight"
base_url = 'http://parsinger.ru/scroll/1/'

with webdriver.Chrome() as browser:
    browser.get(base_url)
    height = browser.execute_script(get_height_script)
    window = browser.execute_script(get_window_height_script)
    start = 0
    while start <= height:
        browser.execute_script(f"window.scrollBy(0,{window})")
        start += window
        sleep(0.0025)
    sleep(2)
    browser.execute_script(f"window.scrollBy(0, -{height})")
    sleep(2)


