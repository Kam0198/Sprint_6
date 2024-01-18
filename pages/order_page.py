import random
from selenium.webdriver.common.by import By
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderScooterPage(BasePage):
    def __int__(self, driver):
        super().__init__(driver)

    def scroll_to_element(self):
        self.find_element_scroll(MainPageLocators.ORDER_BUTTON_MIDDLE)

    def click_button_order_header(self):
        self.driver.find_element(*MainPageLocators.ORDER_BUTTON_HEADER).click()
        return

    def click_button_order_middle(self):
        self.driver.find_element(*MainPageLocators.ORDER_BUTTON_MIDDLE).click()
        return

    def enter_text_name(self, name):
        enter_name = self.driver.find_element(*OrderPageLocators.NAME_FIELD)
        enter_name.click()
        enter_name.send_keys(name)
        return enter_name

    def enter_text_surname(self, surname):
        enter_surname = self.driver.find_element(*OrderPageLocators.SURNAME_FIELD)
        enter_surname.click()
        enter_surname.send_keys(surname)
        return enter_surname

    def enter_text_address(self, address):
        enter_address = self.driver.find_element(*OrderPageLocators.ADDRESS_FIELD)
        enter_address.click()
        enter_address.send_keys(address)
        return enter_address

    def set_metro_station(self):
        self.driver.find_element(*OrderPageLocators.STATION_SELECTION).click()
        self.driver.find_element(By.XPATH, "//div[text()='Черкизовская']").click()

    def enter_phone(self):
        phone = f'+79{random.randint(100, 999999999)}'
        self.driver.find_element(*OrderPageLocators.PHONE_FIELD).send_keys(phone)
        return phone

    def click_button_next(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_NEXT).click()
        return

    def choose_date_order(self):
        self.driver.find_element(*OrderPageLocators.DATE_SELECTION).click()
        self.driver.find_element(By.XPATH, "//div[text()='28']").click()

    def choose_rental_period(self):
        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD).click()
        self.driver.find_element(By.XPATH, "//div[text()='двое суток']").click()

    def choose_color_scooter(self):
        self.driver.find_element(*OrderPageLocators.SCOOTER_COLOR_GREY_CHECKBOX).click()

    def enter_comment(self, comment):
        enter_comment = self.driver.find_element(*OrderPageLocators.COMMENT_FIELD)
        enter_comment.click()
        enter_comment.send_keys(comment)
        return enter_comment

    def click_button_order(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_ORDER).click()
        return

    def click_button_confirm(self):
        self.driver.find_element(*OrderPageLocators.CONFIRM_BUTTON).click()
        return

    def get_modal_header_text(self):
        modal_header_locator = OrderPageLocators.MODAL_WINDOW
        modal_header = self.find_element_located(modal_header_locator)
        return modal_header.text