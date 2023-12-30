from selenium import webdriver

with webdriver.Chrome() as browser:
    browser.get(url="https://google.com")
    size = browser.get_window_size()
    print(f"Window size is {size['width']} for {size['height']}")
