from pages.base_page import BasePage


class Asserts(BasePage):
    def text_is_correct(self, text, locator):
        locator_type, locator_value = locator
        text_element = self.driver.find_element(locator_type, locator_value)
        assert text_element.text == text, f'Ожидаемый результат: {text}. Фактический результат: {text_element.text}'
        return True