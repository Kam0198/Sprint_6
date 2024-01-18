from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class YaMainPage(BasePage):
    def __int__(self, driver):
        super().__init__(driver)

    def click_logo_scooter(self):
        self.driver.find_element(*MainPageLocators.LOGO_SCOOTER).click()
        return

    def click_logo_yandex(self):
        self.driver.find_element(*MainPageLocators.LOGO_YANDEX).click()
        return

    def scroll_page_down(self):
        button_element = self.driver.find_element(By.TAG_NAME, 'body')
        self.driver.execute_script("arguments[0].scrollIntoView();", button_element)
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.ID, 'BUTTON_ORDER')))











