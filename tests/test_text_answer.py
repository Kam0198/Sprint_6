import allure
import pytest

from locators.main_page_locators import FAQLocators
from pages.base_page import BasePage
from pages.main_page import YaMainPage


def answer_block():
    return [
        (
            "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
            FAQLocators.FAQ_QUESTION_1,
            FAQLocators.FAQ_ANSWER_1
        ),

        (
            "Пока что у нас так: один заказ — один самокат. "
            "Если хотите покататься с друзьями, можете просто сделать несколько заказов "
            "— один за другим.",
            FAQLocators.FAQ_QUESTION_2,
            FAQLocators.FAQ_ANSWER_2
        ),

        (
            "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня."
            " Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру."
            " Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
            FAQLocators.FAQ_QUESTION_3,
            FAQLocators.FAQ_ANSWER_3
        ),

        (
            "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
            FAQLocators.FAQ_QUESTION_4,
            FAQLocators.FAQ_ANSWER_4
        ),

        (
            "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку "
            "по красивому номеру 1010.",
            FAQLocators.FAQ_QUESTION_5,
            FAQLocators.FAQ_ANSWER_5
        ),

        (
            "Самокат приезжает к вам с полной зарядкой. "
            "Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
            FAQLocators.FAQ_QUESTION_6,
            FAQLocators.FAQ_ANSWER_6
        ),

        (
            "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже "
            "не попросим. Все же свои.",
            FAQLocators.FAQ_QUESTION_7,
            FAQLocators.FAQ_ANSWER_7
        ),

        (
            "Да, обязательно. Всем самокатов! И Москве, и Московской области.",
            FAQLocators.FAQ_QUESTION_8,
            FAQLocators.FAQ_ANSWER_8
        ),
    ]


class TestAnswerText:
    @allure.feature('Проверка текста в блоке FAQ на соответствие введенному нами тексту')
    @allure.title('Проверка текста в "Ответе" на "Вопрос"')
    @allure.description('Сравниваем текст в каждом заголовке "Ответ" с ожидаемым текстом')
    @allure.step('Сравниваем каждый заголовок текста в блоке "Ответ"')
    @pytest.mark.parametrize(("expected_text", "question", "answer"), answer_block())
    def test_faq_answer(self, driver, expected_text, question, answer):
        ya_main_page = YaMainPage(driver)
        question_element = BasePage(driver)
        ya_main_page.go_to_site(YaMainPage.URL_MAIN)
        question_element.scroll_and_click(question)
        text_answer = ya_main_page.text_from_element(answer)
        assert text_answer == expected_text
