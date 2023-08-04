
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
import time

try:
    link = "https://frontend-superapp.emlife-dev.mvideoeldorado.ru/news"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(1)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.XPATH, "//input[@name='username']")
    input1.send_keys("31000000")
    input2 = browser.find_element(By.XPATH, "//input[@name='password']")
    input2.send_keys("z6gmkgYKBMDU")
    button = browser.find_element(By.XPATH, "//input[@type='submit']")
    button.click()
    time.sleep(2)
    button = browser.find_element(By.XPATH, "//button[@data-test='turn-off-push-notifications-button']")
    button.click()
    button = browser.find_element(By.XPATH, "//div[@class='nav__item nav__services']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
