import selenium
from selenium.webdriver.common.by import By
import time

url ="http://parsinger.ru/selenium/7/7.html"
browser = selenium.webdriver.Chrome()

try:
    browser.get(url)
    drop_elements = browser.find_elements(By.TAG_NAME, 'option')
    total = sum([int(i.text) for i in drop_elements])
    print(total)
    result_window = browser.find_element(By.ID, 'input_result').send_keys(total)
    time.sleep(3)
    button = browser.find_element(By.ID, 'sendbutton').click()


except:
    print("Something gone realy bad")

finally:
    print("Job done")
    browser.quit()
