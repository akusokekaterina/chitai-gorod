import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.settings import settings


@pytest.fixture(scope="function")
def driver():
    options = Options()
    if settings.HEADLESS:
        options.add_argument("--headless")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-extensions")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    try:
        service = Service(ChromeDriverManager().install())
        driver_instance = webdriver.Chrome(service=service, options=options)
    except Exception:
        driver_instance = webdriver.Chrome(options=options)

    driver_instance.implicitly_wait(settings.TIMEOUT)

    yield driver_instance

    driver_instance.quit()


@pytest.fixture(scope="function")
def main_page(driver):
    from pages.main_page import MainPage
    page = MainPage(driver)
    page.open()
    page.accept_cookies()
    return page
