import pytest
from selenium import webdriver
from config import BASE_URL

@pytest.fixture()
def driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--window-size=1920,1080')
    firefox_options.add_argument("--incognito")
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(BASE_URL)
    yield driver
    driver.quit()


