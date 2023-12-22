import time
from selenium import webdriver

options_for_chrome = webdriver.ChromeOptions()
options_for_chrome.add_extension("/home/kirill/.config/google-chrome/Default/Extensions/"
                                 "gkkmpbaijflcgbbdfjgihbgmpkhgpgof/0.2_0.crx")
url = "https://ya.ru"

with webdriver.Chrome(options=options_for_chrome) as browser:
    browser.get(url=url)
    time.sleep(60)
    browser.quit()
