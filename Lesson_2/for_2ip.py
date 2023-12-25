from selenium import webdriver
import time
from selenium.webdriver.common.by import By


link = "https://2ip.ru"
proxy = ['13.81.217.201:80']
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--proxy-server=%s" % proxy)
with webdriver.Chrome(options=chrome_options) as browser:
    browser.get(link)
    ip = browser.find_element(By.ID, 'd_clip_button').text
    print(ip)
    time.sleep(5)

