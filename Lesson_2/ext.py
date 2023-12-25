import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options_for_chrome = webdriver.ChromeOptions()
options_for_chrome.add_argument("--headless")
# options_for_chrome.add_extension("/home/kirill/.config/google-chrome/Default/Extensions/"
#                                  "gkkmpbaijflcgbbdfjgihbgmpkhgpgof/0.2_0.crx")
url = "https://ya.ru"

with webdriver.Chrome(options=options_for_chrome) as browser:
    browser.get(url=url)
    usd_span = browser.find_element(By.XPATH, '/html/body/main/div[3]/div/div/a[1]/span').text
    print(usd_span)
    time.sleep(5)
    browser.quit()

# /html/body/main/div[3]/div/div/a[1]/span
