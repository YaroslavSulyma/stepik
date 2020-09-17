from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"100"))
    button = browser.find_element_by_id("book")
    button.click()

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(int(x))

    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(y)

    btn_submit = browser.find_element_by_id("solve")
    btn_submit.click()

except Exception as e:
    raise e

finally:
    # успеваем скопировать код за 15 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла