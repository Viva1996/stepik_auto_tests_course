import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")

    option1 = browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(y)

    option2 = browser.find_element(By.XPATH, "//label[@for='robotCheckbox']").click()

    option3 = browser.find_element(By.XPATH, "//label[@for='robotsRule']").click()

    button1 = browser.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
