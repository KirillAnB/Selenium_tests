from selenium import webdriver
import time


url = "http://parsinger.ru/selenium/2/2.html"
browser = webdriver.Chrome()

try:
    browser.get(url)
    element = browser.find_element(webdriver.common.by.By.PARTIAL_LINK_TEXT, '16243162441624').click()
    time.sleep(3)
    result = browser.find_element(webdriver.common.by.By.ID, 'result')
    print(result.text)
except:
    print("Oops")
finally:
    browser.quit()
    print("browser was closed")

