# tests/test_api.py
"""API tests for Chitai-Gorod website."""
import allure
from data.test_data import test_data


@allure.feature("API Тесты")
class TestUserAPI:
    @allure.title("Тест структуры данных пользователя")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_user_profile_structure(self):
        user_data = test_data.USER_PROFILE_DATA

        required_fields = ["id", "email", "phone", "firstName", "lastName"]
        for field in required_fields:
            assert field in user_data, \
                f"Отсутствует обязательное поле: {field}"

        assert isinstance(user_data["id"], int), "ID должен быть integer"
        assert isinstance(user_data["email"], str), "Email должен быть строкой"
        assert isinstance(user_data["phone"], str), "Phone должен быть строкой"


@allure.feature("API Тесты")
class TestAuthAPI:
    @allure.title("Тест структуры авторизации")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_auth_credentials_structure(self):
        credentials = test_data.API_CREDENTIALS

        required_fields = ["username", "password", "email", "phone"]
        for field in required_fields:
            assert field in credentials, f"Отсутствует поле: {field}"

        for field in required_fields:
            assert credentials[field], f"Поле {field} не должно быть пустым"


@allure.feature("API Тесты")
class TestSearchAPI:
    @allure.title("Тест данных для поиска")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_data(self):
        assert test_data.SEARCH_AUTHOR, "Автор для поиска не задан"
        assert test_data.SEARCH_BOOK, "Книга для поиска не задана"
        assert test_data.TEST_PRODUCT_NAME, "Название продукта не задано"

        message = "Автор должен быть не пустой строкой"
        assert len(test_data.SEARCH_AUTHOR) > 0, message

        message = "Название книги должно быть не пустой строкой"
        assert len(test_data.SEARCH_BOOK) > 0, message


@allure.feature("API Тесты")
class TestDataValidation:
    @allure.title("Валидация тестовых данных")
    @allure.severity(allure.severity_level.NORMAL)
    def test_data_validation(self):
        """Валидация всех тестовых данных."""
        message = "Телефон должен начинаться с +"
        assert test_data.VALID_PHONE.startswith('+'), message

        message = "Телефон должен содержать минимум 11 цифр"
        assert len(test_data.VALID_PHONE) >= 11, message

        assert '@' in test_data.EMAIL, "Email должен содержать @"
        assert '.' in test_data.EMAIL, "Email должен содержать ."

        message = "Код должен содержать только цифры"
        assert test_data.CONFIRMATION_CODE.isdigit(), message

        message = "Код должен содержать 4 цифры"
        assert len(test_data.CONFIRMATION_CODE) == 4, message
