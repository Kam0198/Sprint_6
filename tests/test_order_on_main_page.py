import allure
import pytest

from pages.main_page import YaMainPage
from pages.order_page import OrderScooterPage


class TestOrderMainPage:
    @allure.title("Заполнение всех полей и подтверждение оформления заказа")
    @pytest.mark.parametrize("name, surname, address, comment",[
        ("Кам", "Габдрахманова", "г.Москва, ул.Ход.Бульвар 5", "Доставить после 12:00")
    ])
    def test_form_main_page(self, driver, name, surname, address, comment):
        order_scooter = OrderScooterPage(driver)
        main_page = YaMainPage(driver)
        main_page.go_to_site(YaMainPage.URL_MAIN)
        main_page.scroll_to_button()
        order_scooter.enter_text_name(name)
        order_scooter.enter_text_surname(surname)
        order_scooter.enter_text_address(address)
        order_scooter.set_metro_station()
        order_scooter.enter_phone()
        order_scooter.click_button_next()
        order_scooter.choose_date_order()
        order_scooter.choose_rental_period()
        order_scooter.choose_color_scooter()
        order_scooter.enter_comment(comment)
        order_scooter.click_button_order()
        order_scooter.click_button_confirm()
        modal_text = order_scooter.get_modal_header_text()
        expected_text = "Заказ оформлен"
        assert expected_text in modal_text, f"Expected '{expected_text}' in modal header, but got: {modal_text}"
