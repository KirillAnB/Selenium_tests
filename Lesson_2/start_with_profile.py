from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
base_url = "https://ya.ru"
user_profile = "/home/kirill/.config/google-chrome/Default"
options.add_argument(user_profile)

try:
    browser = webdriver.Chrome(options=options)
    browser.get(base_url)
    time.sleep(15)

except:
    print("Something went wrong")

finally:
    browser.quit()

