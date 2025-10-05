from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class CheckoutPage(BasePage):
    CHECKOUT_FORM = (By.CSS_SELECTOR, "[data-testid='checkout-form']")
    CUSTOMER_NAME = (By.CSS_SELECTOR, "[data-testid='customer-name']")
    CUSTOMER_PHONE = (By.CSS_SELECTOR, "[data-testid='customer-phone']")
    DELIVERY_ADDRESS = (By.CSS_SELECTOR, "[data-testid='delivery-address']")
    SUBMIT_ORDER_BUTTON = (By.CSS_SELECTOR, "[data-testid='submit-order']")

    @allure.step("Проверить, что открыта страница оформления заказа")
    def is_checkout_page_opened(self):
        return self.is_visible(self.CHECKOUT_FORM)

    @allure.step("Заполнить данные для оформления заказа")
    def fill_order_data(self, name, phone, address):
        self.type_text(self.CUSTOMER_NAME, name)
        self.type_text(self.CUSTOMER_PHONE, phone)
        self.type_text(self.DELIVERY_ADDRESS, address)
        return self

    @allure.step("Подтвердить заказ")
    def submit_order(self):
        self.click(self.SUBMIT_ORDER_BUTTON)
        return self
