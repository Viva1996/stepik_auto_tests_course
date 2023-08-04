from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

class BasePage:

    def init(self, browser, url="https://frontend-superapp.emlife-dev.mvideoeldorado.ru/news"):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)