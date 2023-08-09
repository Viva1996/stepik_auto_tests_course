from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By


class TestAbs(unittest.TestCase):
    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control first']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control second']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control third']")
        input3.send_keys("email.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(2)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "First test failed")

    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control first']")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control second']")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//div[@class='first_block']//input[@class='form-control third']")
        input3.send_keys("email.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(2)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Second test failed")


if __name__ == "__main__":
    unittest.main()