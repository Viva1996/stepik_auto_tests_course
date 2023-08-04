import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.XPATH, "//button[@class='trollface btn btn-primary']").click()
    time.sleep(1)
    new_window = browser.window_handles[1]

    browser.switch_to.window(new_window)

    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    option1 = browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(y)

    button2 = browser.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(60)
    # закрываем браузер после всех манипуляций
    browser.quit()
