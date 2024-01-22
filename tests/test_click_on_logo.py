import allure

from locators.main_page_locators import MainPageLocators
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
        assert YaMainPage.URL_MAIN == driver.current_url

    @allure.feature("Проверка ссылок в лого Самоката и Яндекса")
    @allure.title("Проверка перехода на главную страницу Дзена после клика на лого 'Яндекс'")
    @allure.description("Проверка, что после того, как мы кликаем на логотип 'Яндекс', происходит открытие главной "
                        "страницы сайта 'https://dzen.ru/?yredirect=true' в новом окне")
    @allure.step("Открываем страницу заказа самоката и кликаем на логотип 'Яндекс'")
    def test_click_on_logo_yandex(self, driver):
        logo_dzen = YaMainPage(driver)
        logo_dzen.go_to_site(YaMainPage.URL_MAIN)
        logo_dzen.click_logo_yandex()
        logo_dzen.switch_to_new_window()
        logo_dzen.find_element_located(MainPageLocators.LOGO_DZEN)
        assert YaMainPage.URL_DZEN in driver.current_url






