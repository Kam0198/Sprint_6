from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, url):
        self.driver.get(url)

    def find_element_located_click(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(
             EC.presence_of_element_located(locator),
             message=f'Element not found in {locator}')
        element.click()

    def find_element_scroll(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def find_element_located(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f'Element not found in {locator}')

    def find_window(self, time=10):
        return WebDriverWait(self.driver, time).until(EC.number_of_windows_to_be(2))

    def scroll_and_click(self, locator, time=10):
        element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                         message=f'Element no found in {locator}')
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    def switch_to_new_window(self):
        current_window = self.driver.current_window_handle
        self.find_window()
        all_windows = self.driver.window_handles
        new_window = next(window for window in all_windows if window != current_window)
        self.driver.switch_to.window(new_window)



