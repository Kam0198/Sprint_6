import allure

from locators.main_page_locators import MainPageLocators, FAQLocators
from pages.base_page import BasePage


class YaMainPage(BasePage):
    URL_MAIN = "https://qa-scooter.praktikum-services.ru/"
    URL_DZEN = "https://dzen.ru/?yredirect=true"

    @allure.step("Клик по логотипу 'Самокат'")
    def click_logo_scooter(self):
        self.find_element_located_click(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Клик по логотипу 'Яндекс'")
    def click_logo_yandex(self):
        self.find_element_located_click(MainPageLocators.LOGO_YANDEX)

    @allure.step("Скролл страницы до кнопки 'Заказать'")
    def scroll_to_button(self):
        self.scroll_and_click(MainPageLocators.ORDER_BUTTON_MIDDLE)

    @allure.step("Скролл страницы до блока 'Вопросы о важном'")
    def scroll_to_question(self):
        self.find_element_scroll(FAQLocators.FAQ_BLOCK)

    @allure.step("Получение текста из элемента'")
    def text_from_element(self, locator, time=10):
        element = self.find_element_located(locator, time)
        text = element.get_attribute('textContent')
        return text















