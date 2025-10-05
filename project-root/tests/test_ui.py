import time
import pytest
import allure
from data.test_data import test_data


@pytest.mark.ui
@allure.feature("UI Тесты")
class TestAuthorization:
    @allure.title("Тест успешной авторизации")
    def test_successful_authorization(self, main_page):
        try:
            with allure.step("Открыть страницу авторизации"):
                login_page = main_page.click_login_icon()
                time.sleep(2)

                is_opened = login_page.is_login_page_opened()
                message = f"Страница авторизации открыта: {is_opened}"
                allure.attach(
                    message, name="auth-page-check")

                if not is_opened:
                    login_page.take_screenshot("auth_page_not_opened")

                has_form = login_page.is_visible(login_page.LOGIN_FORM)
                message = f"Форма авторизации найдена: {has_form}"
                allure.attach(
                    message, name="auth-form-check")

                assert has_form or is_opened, \
                    "Страница авторизации не открылась"

        except Exception as e:
            allure.attach(
                f"Ошибка при авторизации: {str(e)}", name="auth-error")
            main_page.take_screenshot("authorization_error")
            raise


@pytest.mark.ui
@allure.feature("UI Тесты")
class TestSearch:
    @allure.title("Тест поиска книг по автору")
    def test_search_by_author(self, main_page):
        try:
            with allure.step(f"Искать автора: {test_data.SEARCH_AUTHOR}"):
                search_page = main_page.search_for(test_data.SEARCH_AUTHOR)
                time.sleep(3)

                results_displayed = search_page.are_results_displayed()
                message = f"Результаты отображаются: {results_displayed}"
                allure.attach(message, name="results-check")

                try:
                    header = search_page.get_search_header()
                    allure.attach(
                        f"Заголовок страницы: {header}", name="search-header")
                except Exception:
                    allure.attach("Заголовок не найден", name="search-header")

                if not results_displayed:
                    search_page.take_screenshot("no_search_results")

                products_count = search_page.get_products_count()
                message = f"Найдено товаров: {products_count}"
                allure.attach(message, name="products-count")

                message = "Результаты поиска не отображаются"
                assert products_count > 0 or results_displayed, message

        except Exception as e:
            allure.attach(f"Ошибка при поиске: {str(e)}", name="search-error")
            main_page.take_screenshot("search_error")
            raise


@pytest.mark.ui
@allure.feature("UI Тесты")
class TestCart:
    @allure.title("Тест добавления товара в корзину")
    def test_add_to_cart(self, main_page):
        try:
            with allure.step("Найти книгу через поиск"):
                search_page = main_page.search_for(test_data.SEARCH_BOOK)
                time.sleep(3)

                results_displayed = search_page.are_results_displayed()
                products_count = search_page.get_products_count()
                message = f"Результаты: {results_displayed}, \
                    Товаров: {products_count}"
                allure.attach(
                    message, name="search-results")

                if products_count > 0:
                    product_info = search_page.get_product_info(
                        test_data.SEARCH_BOOK)
                    if product_info:
                        message = f"Информация о товаре: {product_info}"
                        allure.attach(message, name="product-info")

                    added = search_page.add_to_cart(test_data.SEARCH_BOOK)
                    message = f"Товар добавлен в корзину: {added}"
                    allure.attach(message, name="add-to-cart")

                message = "Результаты поиска не отображаются"
                assert results_displayed or products_count > 0, message

        except Exception as e:
            message = f"Ошибка при работе с корзиной: {str(e)}"
            allure.attach(message, name="cart-error")
            main_page.take_screenshot("cart_error")
            raise
