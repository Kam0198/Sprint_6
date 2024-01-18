from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_FIELD = (By.CSS_SELECTOR, '[class*="Order_Form"] [placeholder="* Имя"]')
    SURNAME_FIELD = (By.CSS_SELECTOR, '[class*="Order_Form"] [placeholder="* Фамилия"]')
    ADDRESS_FIELD = (By.CSS_SELECTOR, '[class*="Order_Form"] [placeholder="* Адрес: куда привезти заказ"]')
    STATION_SELECTION = (By.CSS_SELECTOR, '[class*="Order_Form"] [placeholder="* Станция метро"]')
    PHONE_FIELD = (By.CSS_SELECTOR, '[class*="Order_Form"] [placeholder="* Телефон: на него позвонит курьер"]')
    BUTTON_NEXT = (By.XPATH, "// button[contains(text(), 'Далее')]")

    DATE_SELECTION = (By.CSS_SELECTOR, '[class*="Order_Form"] [placeholder="* Когда привезти самокат"]')
    RENTAL_PERIOD = (By.XPATH, "//div[contains(text(),'* Срок аренды')]")
    SCOOTER_COLOR_BLACK_CHECKBOX = (By.XPATH, "//input[@id='black']")
    SCOOTER_COLOR_GREY_CHECKBOX = (By.XPATH, "//input[@id='grey']")
    COMMENT_FIELD = (By.CSS_SELECTOR, '[class*="Order_Form"] [placeholder="Комментарий для курьера"]')

    BUTTON_ORDER = (By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[3]/button[2]")
    BUTTON_BACK = (By.XPATH, "//button[contains(text(),'Назад')]")
    CANCEL_BUTTON = (By.XPATH, "//button[contains(text(),'Нет')]")
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(),'Да')]")

    MODAL_WINDOW = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')
