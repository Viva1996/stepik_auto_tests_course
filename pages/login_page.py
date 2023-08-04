from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators import FirstPage


class LoginPage(BasePage):

    def  input_username(self, value):
        input_username = self.browser.find_element(*FirstPage.FIRST_INPUT)
        input_username.send_keys(value)

    def input_password(self, value):
        input_password = self.browser.find_element(By.XPATH, "//input[@name='password']")
        input_password.send_keys(value)

    def submit_button(self):
        submit_button =self.browser.find_element(By.XPATH, "//input[@type='submit']")
        submit_button.click()

def template(browser):
    Login = LoginPage(browser)
    Login.input_username("148376")
    Login.input_password("pBgB4trfar")
    Login.submit_button()
