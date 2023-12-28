from selenium.webdriver import Keys
import time
from selenium.webdriver.common.by import By
from selenium import webdriver


base_url = "http://parsinger.ru/scroll/1/"

with webdriver.Chrome() as browser:
    browser.get(url = base_url)
    tags = browser.find_elements(By.TAG_NAME, "input")
    for tag in tags:

        tag.send_keys(Keys.DOWN)
        tag.click()

