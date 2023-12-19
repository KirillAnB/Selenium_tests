import sys

import selenium
from selenium.webdriver.common.by import By
import time

url = 'http://parsinger.ru/selenium/6/6.html'
browser = selenium.webdriver.Chrome()
def nums_maker(item):
    digits_only_num = ''
    for i in item:
        if i.isdigit():
            digits_only_num = digits_only_num + i
    return int(digits_only_num)

try:
    browser.get(url)
    nums = browser.find_elements(By.CLASS_NAME, 'num')
    nums_list = [nums_maker(num.text) for num in nums]
    num1, num2, num3, num4 = nums_list
    answer = str(((num1 * num2) * num3) + num4)
    print(answer)
    drop_elements = browser.find_elements(By.TAG_NAME, 'option')
    for element in drop_elements:
        if answer == element.text:
            element.click()
            time.sleep(3)
    button = browser.find_element(By.ID, 'sendbutton').click()
    time.sleep(3)
except:
    print(sys.exc_info())
finally:
    browser.quit()

# if __name__ == '__main__':
#     print(nums_maker('(123'))
