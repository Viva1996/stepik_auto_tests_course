from selenium.webdriver.common.by import By

class FirstPage():

    FIRST_INPUT = (By.XPATH, "//input[@name='username']")
    SECOND_INPUT = (By.XPATH, "//input[@name='password']")
    SUBMIT = (By.XPATH, "//input[@type='submit']")