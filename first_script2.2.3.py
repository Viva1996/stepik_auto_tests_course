import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element1 = browser.find_element(By.XPATH, "//span[@id='num1']")
    x = x_element1.text
    x_element2 = browser.find_element(By.XPATH, "//span[@id='num2']")
    y = x_element2.text
    z = int(x)+int(y)

    select = Select(browser.find_element(By.XPATH, "//select[@id='dropdown']"))
    select.select_by_value(str(z))

    button1 = browser.find_element(By.XPATH, "//button[@type='submit']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()