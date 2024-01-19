import random

import allure
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderScooterPage(BasePage):
    def __int__(self, driver):
        super().__init__(driver)

    @allure.step("Скролл страницы до кнопки 'Заказать'")
    def scroll_to_element(self):
        self.find_element_scroll(MainPageLocators.ORDER_BUTTON_MIDDLE)

    @allure.step("Клик по кнопке 'Заказать' в хедере")
    def click_button_order_header(self):
        self.driver.find_element(*MainPageLocators.ORDER_BUTTON_HEADER).click()
        return

    @allure.step("Клик по кнопке 'Заказать' в подвале")
    def click_button_order_middle(self):
        self.driver.find_element(*MainPageLocators.ORDER_BUTTON_MIDDLE).click()
        return

    @allure.step("Заполнение поля 'Имя'")
    def enter_text_name(self, name):
        enter_name = self.driver.find_element(*OrderPageLocators.NAME_FIELD)
        enter_name.click()
        enter_name.send_keys(name)
        return enter_name

    @allure.step("Заполнение поля 'Фамилия'")
    def enter_text_surname(self, surname):
        enter_surname = self.driver.find_element(*OrderPageLocators.SURNAME_FIELD)
        enter_surname.click()
        enter_surname.send_keys(surname)
        return enter_surname

    @allure.step("Заполнение поля 'Адрес'")
    def enter_text_address(self, address):
        enter_address = self.driver.find_element(*OrderPageLocators.ADDRESS_FIELD)
        enter_address.click()
        enter_address.send_keys(address)
        return enter_address

    @allure.step("Выбор станции 'Метро' из выпадающего списка")
    def set_metro_station(self):
        self.driver.find_element(*OrderPageLocators.STATION_SELECTION).click()
        self.driver.find_element(By.XPATH, "//div[text()='Сокольники']").click()

    @allure.step("Заполнение поля 'Телефон'")
    def enter_phone(self):
        phone = f'+79{random.randint(100, 999999999)}'
        self.driver.find_element(*OrderPageLocators.PHONE_FIELD).send_keys(phone)
        return phone

    @allure.step("Клик по кнопке 'Далее'")
    def click_button_next(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_NEXT).click()
        return

    @allure.step("Выбор даты заказа из календаря")
    def choose_date_order(self):
        self.driver.find_element(*OrderPageLocators.DATE_SELECTION).click()
        self.driver.find_element(By.XPATH, "//div[text()='28']").click()

    @allure.step("Выбор срока аренды из выпадающего списка")
    def choose_rental_period(self):
        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD).click()
        self.driver.find_element(By.XPATH, "//div[text()='двое суток']").click()

    @allure.step("Клик по элементу чекбокса")
    def choose_color_scooter(self):
        self.driver.find_element(*OrderPageLocators.SCOOTER_COLOR_GREY_CHECKBOX).click()
        return

    @allure.step("Заполнение поля 'Комментарий для курьера'")
    def enter_comment(self, comment):
        enter_comment = self.driver.find_element(*OrderPageLocators.COMMENT_FIELD)
        enter_comment.click()
        enter_comment.send_keys(comment)
        return enter_comment

    @allure.step("Клик по кнопке 'Заказать'")
    def click_button_order(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_ORDER).click()
        return

    @allure.step("Клик по кнопке 'Да' для подтверждения заказа")
    def click_button_confirm(self):
        self.driver.find_element(*OrderPageLocators.CONFIRM_BUTTON).click()
        return

    @allure.step("Получение текста из модального окна после подтверждения заказа")
    def get_modal_header_text(self):
        modal_header_locator = OrderPageLocators.MODAL_WINDOW
        modal_header = self.find_element_located(modal_header_locator)
        return modal_header.text

    URL_ORDER = "https://qa-scooter.praktikum-services.ru/order"
