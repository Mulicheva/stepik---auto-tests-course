from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
try:
    browser.get(link)
    x_element = browser.find_element_by_css_selector("#treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)

    checkbox = browser.find_element_by_css_selector("#robotCheckbox")
    checkbox.click()

    radiobttn = browser.find_element_by_css_selector("[value='robots']")
    radiobttn.click()

    time.sleep(1)
    button = browser.find_element_by_css_selector("button.btn").click()
    #button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла