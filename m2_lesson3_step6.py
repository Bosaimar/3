from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    btn1 = browser.find_element_by_css_selector('button')
    btn1.click()

    browser.switch_to.window(browser.window_handles[1])

    x_el = browser.find_element_by_css_selector('[id="input_value"]')
    x = int(x_el.text)
    z = str(math.log(abs(12*math.sin(x))))

    inpt = browser.find_element_by_css_selector('[id="answer"]')
    inpt.send_keys(z)
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
