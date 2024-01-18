from selenium.webdriver.chrome.service import Service
import pytest
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

#@pytest.fixture
#def driver():
#    service = Service(GeckoDriverManager().install())
#    driver = webdriver.Firefox(service=service)
#    yield driver
#    driver.quit()

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()
