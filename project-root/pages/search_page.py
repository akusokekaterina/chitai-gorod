from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class SearchPage(BasePage):
    SEARCH_RESULTS = (
        By.CSS_SELECTOR,
        ".products-list, .search-results, [data-testid='search-results']"
    )
    PRODUCT_CARD = (
        By.CSS_SELECTOR,
        ".product-card, .product-item, [data-testid='product-card']"
    )
    PRODUCT_TITLE = (
        By.CSS_SELECTOR,
        ".product-card__title, .product-title, [data-testid='product-title']"
    )
    PRODUCT_AUTHOR = (
        By.CSS_SELECTOR,
        ".product-card__subtitle, .product-author, ["
        "data-testid='product-author']"
    )
    BUY_BUTTON = (
        By.CSS_SELECTOR,
        ".product-card__buy, .buy-button, [data-testid='buy-button']"
    )
    PRICE = (
        By.CSS_SELECTOR,
        ".product-price__value, .price, [data-testid='price']")
    SEARCH_HEADER = (
        By.CSS_SELECTOR,
        ".search-page__title, .search-header, h1")

    @allure.step("Проверить, что отображаются результаты поиска")
    def are_results_displayed(self):
        return self.is_visible(self.SEARCH_RESULTS)

    @allure.step("Получить количество найденных товаров")
    def get_products_count(self):
        return len(self.find_elements(self.PRODUCT_CARD))

    @allure.step("Найти товар с названием: {title}")
    def find_product_by_title(self, title):
        products = self.find_elements(self.PRODUCT_CARD)
        for product in products:
            try:
                product_title = product.find_element(*self.PRODUCT_TITLE).text
                if title.lower() in product_title.lower():
                    return product
            except Exception:
                continue
        return None

    @allure.step("Добавить товар в корзину: {product_title}")
    def add_to_cart(self, product_title):
        product = self.find_product_by_title(product_title)
        if product:
            try:
                buy_button = product.find_element(*self.BUY_BUTTON)
                buy_button.click()
                message = f"Товар '{product_title}' добавлен в корзину"
                allure.attach(message, name="product-added")
                return True
            except Exception as e:
                message = f"Ошибка при добавлении товара: {str(e)}"
                allure.attach(message, name="add-to-cart-error")
                return False
        return False

    @allure.step("Получить информацию о товаре: {product_title}")
    def get_product_info(self, product_title):
        product = self.find_product_by_title(product_title)
        if product:
            try:
                title = product.find_element(*self.PRODUCT_TITLE).text
                author = product.find_element(*self.PRODUCT_AUTHOR).text
                price = product.find_element(*self.PRICE).text
                return {
                    "title": title,
                    "author": author,
                    "price": price
                }
            except Exception:
                return None
        return None

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        from pages.main_page import MainPage
        main_page = MainPage(self.driver)
        return main_page.go_to_cart()
