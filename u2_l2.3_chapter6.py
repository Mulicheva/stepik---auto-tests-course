from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome("C:/chromedriver/chromedriver.exe")
try:
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn").click()
    # button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)
    browser.execute_script("window.scrollBy(0, 100);")
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(y)



    time.sleep(1)
    button1 = browser.find_element_by_css_selector("button.btn").click()
    #button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла