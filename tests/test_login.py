import time

from pages.login_page import *
import pytest

def test_login(browser):
    template(browser)
    time.sleep(10)
