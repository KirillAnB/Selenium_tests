import selenium
from selenium.webdriver.common.by import By
import time

base_url = "https://parsinger.ru/methods/5/index.html"

with selenium.webdriver.Chrome() as browser:
    browser.get(url=base_url)
    links = browser.find_elements(By.CLASS_NAME, 'urls')
    _list_links = [link.find_element(By.TAG_NAME, 'a').get_attribute('href') for link in links]
    result = []
    for link in _list_links:
        browser.get(url=link)
        page_cookie = browser.get_cookies()
        for item in page_cookie:
            result.append(item['expiry'])
        browser.back()
    print(min(result))

