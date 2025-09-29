from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class MainPage(BasePage):
    LOGIN_ICON = (
        By.CSS_SELECTOR,
        "[aria-label*='войти'], [href*='login'], .header-controls__btn"
    )
    SEARCH_INPUT = (
        By.CSS_SELECTOR,
        ".search-form__input.search-form__input--search")
    SEARCH_BUTTON = (
        By.CSS_SELECTOR,
        ".search-form__submit")
    CART_ICON = (
        By.CSS_SELECTOR,
        "[aria-label*='Корзина'], .header-controls__btn")
    CART_INDICATOR = (
        By.CSS_SELECTOR,
        ".header-controls__indicator")
    ACCEPT_COOKIES = (
        By.CSS_SELECTOR,
        ".cookie-notice__accept, [data-testid='accept-cookies']"
    )
    USER_ICON = (
        By.CSS_SELECTOR,
        "[aria-label*='Профиль'], .header-controls__icon--user")

    @allure.step("Принять cookies")
    def accept_cookies(self):
        try:
            self.click(self.ACCEPT_COOKIES)
            allure.attach("Cookies приняты", name="cookies")
        except Exception:
            allure.attach("Кнопка cookies не найдена", name="cookies")

    @allure.step("Нажать на иконку входа")
    def click_login_icon(self):
        from pages.login_page import LoginPage
        self.click(self.LOGIN_ICON)
        return LoginPage(self.driver)

    @allure.step("Ввести поисковый запрос: {query}")
    def search_for(self, query):
        from pages.search_page import SearchPage
        self.type_text(self.SEARCH_INPUT, query)
        from selenium.webdriver.common.keys import Keys
        search_input = self.find_element(self.SEARCH_INPUT)
        search_input.send_keys(Keys.ENTER)
        return SearchPage(self.driver)

    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        from pages.cart_page import CartPage
        self.click(self.CART_ICON)
        return CartPage(self.driver)

    @allure.step("Получить количество товаров в корзине")
    def get_cart_items_count(self):
        try:
            indicator = self.find_element(self.CART_INDICATOR)
            count_text = indicator.text.strip()
            return int(count_text) if count_text.isdigit() else 0
        except Exception:
            return 0

    @allure.step("Проверить авторизацию пользователя")
    def is_user_logged_in(self):
        try:
            return self.is_visible(self.USER_ICON)
        except Exception:
            return False
