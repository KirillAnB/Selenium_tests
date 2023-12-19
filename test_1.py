from selenium.webdriver.common.by import By
import selenium
import time

browser = selenium.webdriver.Chrome()
user_data = ['Kirill', 'Andreev', 'Borisovich', 39, 'Sain-Petersburg', 'pussylover777@bk.ru']

try:
    browser.get("https://parsinger.ru/selenium/1/1.html")
    input_fields = browser.find_elements(By.CLASS_NAME, 'form')
    for k, v in zip(input_fields, user_data):
        k.send_keys(v)
    time.sleep(2)
    result_button = browser.find_element(By.ID, 'btn').click()
    result = browser.find_element(By.ID, 'result').text
except:
    print("Something went wrong")
finally:
    print("Done")
    print(result)
    browser.quit()

