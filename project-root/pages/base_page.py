from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.settings import settings
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, settings.TIMEOUT)
        self.base_url = settings.BASE_URL

    @allure.step("Открыть страницу {url}")
    def open(self, url=""):
        full_url = f"{self.base_url}/{url}" if url else self.base_url
        self.driver.get(full_url)

    @allure.step("Найти элемент {locator}")
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Найти элементы {locator}")
    def find_elements(self, locator):
        return self.wait.until(EC.visibility_of_any_elements_located(locator))

    @allure.step("Кликнуть на элемент {locator}")
    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    @allure.step("Ввести текст '{text}' в элемент {locator}")
    def type_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента {locator}")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Проверить видимость элемента {locator}")
    def is_visible(self, locator):
        try:
            return self.find_element(locator).is_displayed()
        except TimeoutException:
            return False

    @allure.step("Сделать скриншот")
    def take_screenshot(self, name="screenshot"):
        screenshot_path = f"{settings.SCREENSHOTS_DIR}/{name}.png"
        self.driver.save_screenshot(screenshot_path)
        allure.attach.file(
            screenshot_path,
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
