import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.XPATH, "//input[@name='firstname']").send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Petrov")
    input3 = browser.find_element(By.XPATH, "//input[@name='email']").send_keys("email.com")


    current_dir = os.path.abspath(os.path.dirname(__file__))
    # получаем путь к директории текущего исполняемого файла
    file_name = "file.txt"
    file_path = os.path.join(current_dir, 'file.txt')
    # добавляем к этому пути имя файла
    element = browser.find_element(By.XPATH, "//input[@id='file']")
    element.send_keys(file_path)

    button = browser.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(60)
    # закрываем браузер после всех манипуляций
    browser.quit()
