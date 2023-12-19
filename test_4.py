from selenium.webdriver.common.by import By
import selenium
import time

url = "http://parsinger.ru/selenium/4/4.html"
browser = selenium.webdriver.Chrome()

try:
    browser.get(url)
    check_boxes = browser.find_elements(By.CLASS_NAME, 'check')
    for check_box in check_boxes:
        check_box.click()
    time.sleep(2)
    button = browser.find_element(By.XPATH, "/html/body/div/div[2]/input").click()
    result = browser.find_element(By.ID, 'result').text
    print("Result is {0}".format(result))

except:
    print("Exception happened!")

finally:
    browser.quit()
    print("test 4 finished")

