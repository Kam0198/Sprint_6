from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import YaMainPage


class TestClickOnLogo():
    def test_click_on_logo_scooter(self, driver):
        logo_scooter = YaMainPage(driver)
        logo_scooter.go_to_site("https://qa-scooter.praktikum-services.ru/order")
        logo_scooter.click_logo_scooter()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    def test_click_on_logo_dzen(self, driver):
        logo_dzen = YaMainPage(driver)
        logo_dzen.go_to_site("https://qa-scooter.praktikum-services.ru/")
        logo_dzen.click_logo_yandex()
        current_window = driver.current_window_handle
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        all_windows = driver.window_handles
        new_window = next(window for window in all_windows if window != current_window)
        driver.switch_to.window(new_window)
        dzen_logo_locator = (By.CSS_SELECTOR,
                             '[class*="desktop-base-header__logoLink-aE"] [class*="desktop-base-header__logo-tA"]')
        logo_dzen.find_element_located(dzen_logo_locator)
        current_url = driver.current_url
        assert 'https://dzen.ru/?yredirect=true' in current_url
        driver.close()
        driver.switch_to.window(current_window)






