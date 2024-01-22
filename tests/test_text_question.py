import allure
import pytest

from locators.main_page_locators import FAQLocators
from pages.main_page import YaMainPage


def questions_block():
    return [
        (
            "Сколько это стоит? И как оплатить?",
            FAQLocators.FAQ_QUESTION_1
        ),
        (
            "Хочу сразу несколько самокатов! Так можно?",
            FAQLocators.FAQ_QUESTION_2
        ),
        (
            "Как рассчитывается время аренды?",
            FAQLocators.FAQ_QUESTION_3
        ),
        (
            "Можно ли заказать самокат прямо на сегодня?",
            FAQLocators.FAQ_QUESTION_4
        ),
        (
            "Можно ли продлить заказ или вернуть самокат раньше?",
            FAQLocators.FAQ_QUESTION_5
        ),
        (
            "Вы привозите зарядку вместе с самокатом?",
            FAQLocators.FAQ_QUESTION_6
        ),
        (
            "Можно ли отменить заказ?",
            FAQLocators.FAQ_QUESTION_7
        ),
        (
            "Я жизу за МКАДом, привезёте?",
            FAQLocators.FAQ_QUESTION_8
        ),
    ]


class TestTextQuestion:
    @allure.feature('Проверка текста в блоке FAQ на соответствие введенному нами тексту')
    @allure.title('Проверка текста в блоке "Вопрос"')
    @allure.description('Сравниваем текст в каждом заголовке "Вопрос" с ожидаемым текстом')
    @allure.step('Сравниваем каждый заголовок текста в блоке "Вопрос"')
    @pytest.mark.parametrize(("expected_text", "locator"), questions_block())
    def test_faq_question(self, driver, expected_text, locator):
        ya_main_page = YaMainPage(driver)
        ya_main_page.go_to_site(YaMainPage.URL_MAIN)
        ya_main_page.scroll_to_question()
        text_answer = ya_main_page.text_from_element(locator)
        assert text_answer == expected_text
