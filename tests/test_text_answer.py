import time

import pytest

from asserts.base_assert import Asserts
from locators.main_page_locators import FAQLocators
from pages.main_page import YaMainPage


class TestAnswerText:
    @pytest.mark.parametrize(("text", "question", "answer"),
                             [
                                 ("Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
                                  FAQLocators.FAQ_QUESTION_1, FAQLocators.FAQ_ANSWER_1),

                                 ("Пока что у нас так: один заказ — один самокат. "
                                  "Если хотите покататься с друзьями, можете просто сделать несколько заказов "
                                  "— один за другим.",
                                  FAQLocators.FAQ_QUESTION_2, FAQLocators.FAQ_ANSWER_2),

                                 ("Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. "
                                  "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. "
                                  "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
                                  FAQLocators.FAQ_QUESTION_3, FAQLocators.FAQ_ANSWER_3),

                                 ("Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
                                  FAQLocators.FAQ_QUESTION_4, FAQLocators.FAQ_ANSWER_4),

                                 ("Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку "
                                  "по красивому номеру 1010.",
                                  FAQLocators.FAQ_QUESTION_5, FAQLocators.FAQ_ANSWER_5),

                                 ("Самокат приезжает к вам с полной зарядкой. "
                                  "Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. "
                                  "Зарядка не понадобится.",
                                  FAQLocators.FAQ_QUESTION_6, FAQLocators.FAQ_ANSWER_6),

                                 ("Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже "
                                  "не попросим. Все же свои.",
                                  FAQLocators.FAQ_QUESTION_7, FAQLocators.FAQ_ANSWER_7),

                                 ("Да, обязательно. Всем самокатов! И Москве, и Московской области.",
                                  FAQLocators.FAQ_QUESTION_8, FAQLocators.FAQ_ANSWER_8),
                             ])
    def test_faq_answer(self, driver, text, question, answer):
        ya_main_page = YaMainPage(driver)
        asserts_instance = Asserts(driver)
        ya_main_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        ya_main_page.scroll_page_down()
        question_element = driver.find_element(*question)
        driver.execute_script("arguments[0].scrollIntoView(true);", question_element)
        time.sleep(1)
        question_element.click()
        time.sleep(1)
        locator_type, locator_value = answer
        assert asserts_instance.text_is_correct(text, (locator_type, locator_value))









