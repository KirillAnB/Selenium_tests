import time
from selenium.webdriver import Chrome


with Chrome() as browser:
    browser.get('https://yandex.ru')
    time.sleep(1)
    browser.execute_script('window.open("https://google.com");')
    time.sleep(1)
    browser.execute_script('window.open("https://mail.ru");')
    time.sleep(1)
    titles = []
    for item in browser.window_handles:
        browser.switch_to.window(item)
        titles.append(browser.execute_script('return document.title;'))
        time.sleep(1)
    print(titles)
