import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.chrome.service import Service


@pytest.fixture
def driver():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    yield driver
    driver.quit()