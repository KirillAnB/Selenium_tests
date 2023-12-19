import selenium
from selenium.webdriver.common.by import By
import time



url = "http://parsinger.ru/selenium/3/3.html"
x_path = "//div[@class='text']/p[2]"
x_path2 = "//div[@class='text']/p"
def summ1():
    try:
        browser = selenium.webdriver.Chrome()
        browser.get(url)
        time.sleep(3)
        p_tags = browser.find_elements(By.XPATH, x_path)
        p_sum = sum([int(p.text) for p in p_tags])
        print(p_sum)
    except:
        print("OOOPS")

    finally:
        browser.quit()
        print('Browser was closed')

def summ2():
    try:
        browser = selenium.webdriver.Chrome()
        browser.get(url)
        time.sleep(3)
        p_tags = browser.find_elements(By.XPATH, x_path2)
        p_list = sum([int(p.text) for p in p_tags])
        print(p_list)

    except:
        print("OOOPS")

    finally:
        browser.quit()
        print('Browser was closed')
summ1()
summ2()
