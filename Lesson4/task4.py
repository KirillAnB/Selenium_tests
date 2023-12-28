import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


url = "https:ya.ru"

with webdriver.Chrome() as browser:
    browser.get(url=url)
    input_field = browser.find_element(By.ID, "text")
    input_field.send_keys('booty milf beach')
    button = browser.find_element(By.CLASS_NAME, "search3__button")
    action = ActionChains(browser)
    action.move_to_element(button)
    action.click()
    time.sleep(2)
    action.perform()




