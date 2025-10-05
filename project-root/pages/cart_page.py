from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class CartPage(BasePage):
    CART_ITEMS = (
        By.CSS_SELECTOR,
        ".cart-item, .basket-item, [data-testid='cart-item']")
    ITEM_TITLE = (
        By.CSS_SELECTOR,
        ".cart-item__title, .item-title, [data-testid='item-title']")
    ITEM_AUTHOR = (
        By.CSS_SELECTOR,
        ".cart-item__author, .item-author")
    ITEM_PRICE = (
        By.CSS_SELECTOR,
        ".cart-item__price, .item-price")
    ITEM_QUANTITY = (
        By.CSS_SELECTOR,
        ".cart-item__quantity, .item-quantity")
    CHECKOUT_BUTTON = (
        By.CSS_SELECTOR,
        ".cart__checkout-button, .checkout-btn, ["
        "data-testid='checkout-button']"
    )
    EMPTY_CART_MESSAGE = (
        By.CSS_SELECTOR,
        ".cart__empty-message, .empty-cart, [data-testid='empty-cart']"
    )
    TOTAL_PRICE = (
        By.CSS_SELECTOR,
        ".cart__total-price, .total-price, [data-testid='total-price']")
    CART_HEADER = (
        By.CSS_SELECTOR,
        ".cart__title, .basket-title, h1")

    @allure.step("Проверить, что товар '{title}' находится в корзине")
    def is_product_in_cart(self, title):
        items = self.find_elements(self.CART_ITEMS)
        for item in items:
            try:
                item_title = item.find_element(*self.ITEM_TITLE).text
                if title.lower() in item_title.lower():
                    return True
            except Exception:
                continue
        return False

    @allure.step("Получить количество товаров в корзине")
    def get_cart_items_count(self):
        return len(self.find_elements(self.CART_ITEMS))

    @allure.step("Получить информацию о товаре в корзине: {title}")
    def get_cart_item_info(self, title):
        items = self.find_elements(self.CART_ITEMS)
        for item in items:
            try:
                item_title = item.find_element(*self.ITEM_TITLE).text
                if title.lower() in item_title.lower():
                    author = item.find_element(*self.ITEM_AUTHOR).text
                    price = item.find_element(*self.ITEM_PRICE).text
                    quantity = item.find_element(
                        *self.ITEM_QUANTITY).get_attribute("value")
                    return {
                        "title": item_title,
                        "author": author,
                        "price": price,
                        "quantity": quantity
                    }
            except Exception:
                continue
        return None

    @allure.step("Нажать кнопку оформления заказа")
    def proceed_to_checkout(self):
        from pages.checkout_page import CheckoutPage
        self.click(self.CHECKOUT_BUTTON)
        return CheckoutPage(self.driver)

    @allure.step("Проверить, что корзина пуста")
    def is_cart_empty(self):
        return self.is_visible(self.EMPTY_CART_MESSAGE)

    @allure.step("Получить общую стоимость заказа")
    def get_total_price(self):
        return self.get_text(self.TOTAL_PRICE)
