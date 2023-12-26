import selenium
from selenium.webdriver.common.by import By
from pprint import pprint

base_url = "https://parsinger.ru/methods/3/index.html"

with selenium.webdriver.Chrome() as browser:
    browser.get(url=base_url)
    _dicts = browser.get_cookies()
    result = 0
    for _dict in _dicts:
        result += int(_dict['value'])
    print(result)
    
