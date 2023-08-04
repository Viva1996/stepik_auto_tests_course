import pytest
from selenium import webdriver
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

options = webdriver.ChromeOptions()

options.add_argument('--headless')
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("excludeSwitches", ['enable-automation'])
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,     # 1:allow, 2:block
    "profile.default_content_setting_values.media_stream_camera": 1,  # 1:allow, 2:block
    "profile.default_content_setting_values.geolocation": 1,          # 1:allow, 2:block
    "profile.default_content_setting_values.notifications": 1         # 1:allow, 2:block
  })


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()