import random

import allure
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderScooterPage(BasePage):
    URL_ORDER = "https://qa-scooter.praktikum-services.ru/order"

    @allure.step("Клик по кнопке 'Заказать' в хедере")
    def click_button_order_header(self):
        self.find_element_located(MainPageLocators.ORDER_BUTTON_HEADER).click()

    @allure.step("Клик по кнопке 'Заказать' в подвале")
    def click_button_order_middle(self):
        self.find_element_located(MainPageLocators.ORDER_BUTTON_MIDDLE).click()

    @allure.step("Заполнение поля 'Имя'")
    def enter_text_name(self, name):
        enter_name = self.find_element_located(OrderPageLocators.NAME_FIELD)
        enter_name.click()
        enter_name.send_keys(name)

    @allure.step("Заполнение поля 'Фамилия'")
    def enter_text_surname(self, surname):
        enter_surname = self.find_element_located(OrderPageLocators.SURNAME_FIELD)
        enter_surname.click()
        enter_surname.send_keys(surname)

    @allure.step("Заполнение поля 'Адрес'")
    def enter_text_address(self, address):
        enter_address = self.find_element_located(OrderPageLocators.ADDRESS_FIELD)
        enter_address.click()
        enter_address.send_keys(address)

    @allure.step("Выбор станции 'Метро' из выпадающего списка")
    def set_metro_station(self):
        self.find_element_located(OrderPageLocators.STATION_SELECTION).click()
        self.find_element_located(OrderPageLocators.METRO_STATION_NAME).click()

    @allure.step("Заполнение поля 'Телефон'")
    def enter_phone(self):
        phone = f'+79{random.randint(100, 999999999)}'
        self.find_element_located(OrderPageLocators.PHONE_FIELD).send_keys(phone)

    @allure.step("Клик по кнопке 'Далее'")
    def click_button_next(self):
        self.find_element_located(OrderPageLocators.BUTTON_NEXT).click()

    @allure.step("Выбор даты заказа из календаря")
    def choose_date_order(self):
        self.find_element_located(OrderPageLocators.DATE_SELECTION).click()
        self.find_element_located(OrderPageLocators.CHOOSE_DATE_FIELD).click()

    @allure.step("Выбор срока аренды из выпадающего списка")
    def choose_rental_period(self):
        self.find_element_located(OrderPageLocators.RENTAL_PERIOD).click()
        self.find_element_located(OrderPageLocators.CHOOSE_RENTAL_PERIOD).click()

    @allure.step("Клик по элементу чекбокса")
    def choose_color_scooter(self):
        self.find_element_located(OrderPageLocators.SCOOTER_COLOR_GREY_CHECKBOX).click()

    @allure.step("Заполнение поля 'Комментарий для курьера'")
    def enter_comment(self, comment):
        enter_comment = self.find_element_located(OrderPageLocators.COMMENT_FIELD)
        enter_comment.click()
        enter_comment.send_keys(comment)

    @allure.step("Клик по кнопке 'Заказать'")
    def click_button_order(self):
        self.find_element_located(OrderPageLocators.BUTTON_ORDER).click()

    @allure.step("Клик по кнопке 'Да' для подтверждения заказа")
    def click_button_confirm(self):
        self.find_element_located(OrderPageLocators.CONFIRM_BUTTON).click()

    @allure.step("Получение текста из модального окна после подтверждения заказа")
    def get_modal_header_text(self):
        modal_header_locator = OrderPageLocators.MODAL_WINDOW
        modal_header = self.find_element_located(modal_header_locator)
        return modal_header.text

