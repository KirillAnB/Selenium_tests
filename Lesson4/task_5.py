import selenium
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# xpath = "//*[@id="scroll-container"]"
#scroll-container

url = 'https://parsinger.ru/infiniti_scroll_2/'
with selenium.webdriver.Chrome() as browser:
    browser.get(url=url)
    action = ActionChains(browser)
    scroll = browser.find_element(By.CLASS_NAME, 'scroll-container')
    while True:
        action.move_to_element(scroll)
        action.scroll_by_amount(0, 500)
        action.perform()
