import selenium
from selenium.webdriver.common.by import By

url = "https://parsinger.ru/methods/1/index.html"

with selenium.webdriver.Chrome() as browser:
    browser.get(url=url)
    while True:
        result = browser.find_element(By.ID, 'result')
        if result.text.isdigit():
            print(result.text)
            break
        else:
            browser.refresh()



