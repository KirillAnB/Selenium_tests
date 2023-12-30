from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

base_url = 'https://parsinger.ru/expectations/2/index.html'

with Chrome() as browser:
    browser.get(url=base_url)
    try:
        waited_element = WebDriverWait(browser, 10).until(EC.title_is('title_changed'))
        print(waited_element)
    except Exception as error:
        print("Title did not changed")

