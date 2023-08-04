import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element ((By.XPATH, "//h5[@id='price']"), "$100"))
    btn = browser.find_element(By.XPATH, "//button[@id='book']")
    btn.click()

    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    option1 = browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(y)

    button2 = browser.find_element(By.XPATH, "//button[@id='solve']").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()
