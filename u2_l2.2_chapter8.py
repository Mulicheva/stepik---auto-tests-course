from selenium import webdriver
import time
import math
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
try:
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("kate")

    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("mimi")

    input3 = browser.find_element_by_name("email")
    input3.send_keys("nk")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    attach = browser.find_element_by_css_selector("#file")
    attach.send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn").click()
    #button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла