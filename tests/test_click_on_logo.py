import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import YaMainPage
from pages.order_page import OrderScooterPage


class TestClickOnLogo:
    @allure.feature("Проверка ссылок в лого Самоката и Яндекса")
    @allure.title("Проверка перехода на главную страницу Самоката после клика на лого 'Самокат'")
    @allure.description("Проверка, что после того, как мы кликаем на логотип 'Самокат', "
                        "нам открывается главная страница сайта 'https://qa-scooter.praktikum-services.ru/'")
    @allure.step("Открываем страницу заказа самоката и кликаем на логотип 'Самокат'")
    def test_click_on_logo_scooter(self, driver):
        logo_scooter = YaMainPage(driver)
        url_order = OrderScooterPage(driver)
        url_order.go_to_site(OrderScooterPage.URL_ORDER)
        logo_scooter.click_logo_scooter()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @allure.feature("Проверка ссылок в лого Самоката и Яндекса")
    @allure.title("Проверка перехода на главную страницу Дзена после клика на лого 'Яндекс'")
    @allure.description("Проверка, что после того, как мы кликаем на логотип 'Яндекс', происходит открытие главной "
                        "страницы сайта 'https://dzen.ru/?yredirect=true' в новом окне")
    @allure.step("Открываем страницу заказа самоката и кликаем на логотип 'Яндекс'")
    def test_click_on_logo_dzen(self, driver):
        logo_dzen = YaMainPage(driver)
        logo_dzen.go_to_site(YaMainPage.URL_MAIN)
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
        assert "https://dzen.ru/?yredirect=true" in current_url
        driver.close()
        driver.switch_to.window(current_window)






