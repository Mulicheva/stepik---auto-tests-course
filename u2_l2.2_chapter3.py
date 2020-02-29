from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x1, x2):
  return int(x1)+int(x2);

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
try:
    browser.get(link)
    x1_element = browser.find_element_by_css_selector("#num1")
    x1 = x1_element.text

    x2_element = browser.find_element_by_css_selector("#num2")
    x2 = x2_element.text
    y = calc(x1, x2)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_visible_text(str(y))
    button = browser.find_element_by_css_selector("button.btn").click()
    #button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла