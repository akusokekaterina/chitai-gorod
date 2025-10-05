from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class LoginPage(BasePage):
    PHONE_INPUT = (
        By.CSS_SELECTOR,
        "input[name='phone'], input[type='tel'], #phone")
    EMAIL_INPUT = (
        By.CSS_SELECTOR,
        "input[name='email'], input[type='email'], #email")
    LOGIN_BUTTON = (
        By.CSS_SELECTOR,
        ".auth-form__submit, button[type='submit'], .login-btn")
    CODE_INPUT = (
        By.CSS_SELECTOR,
        "input[name='code'], input[type='text'], #code")
    CONFIRM_BUTTON = (
        By.CSS_SELECTOR,
        ".code-form__submit, button[type='submit']")
    LOGIN_FORM = (
        By.CSS_SELECTOR,
        ".auth-form, form, .login-form")
    REGISTER_TAB = (
        By.CSS_SELECTOR,
        ".auth-tabs__item[data-tab='register'], [data-tab='register']"
    )

    @allure.step("Ввести номер телефона: {phone}")
    def enter_phone(self, phone):
        self.type_text(self.PHONE_INPUT, phone)
        return self

    @allure.step("Нажать кнопку входа")
    def click_login(self):
        self.click(self.LOGIN_BUTTON)
        return self

    @allure.step("Ввести код подтверждения: {code}")
    def enter_confirmation_code(self, code):
        self.type_text(self.CODE_INPUT, code)
        return self

    @allure.step("Нажать кнопку подтверждения")
    def click_confirm(self):
        from pages.main_page import MainPage
        self.click(self.CONFIRM_BUTTON)
        return MainPage(self.driver)

    @allure.step("Проверить, что открыта страница авторизации")
    def is_login_page_opened(self):
        checks = [
            self.is_visible(self.LOGIN_FORM),
            self.is_visible(self.PHONE_INPUT),
            self.is_visible(self.EMAIL_INPUT)
        ]
        return any(checks)
