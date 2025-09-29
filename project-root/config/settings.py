import os


class Settings:

    BASE_URL = "https://www.chitai-gorod.ru"
    API_URL = "https://api.chitai-gorod.ru"

    BROWSER = os.environ.get("BROWSER", "chrome")
    HEADLESS = os.environ.get("HEADLESS", "False").lower() == "true"
    TIMEOUT = int(os.environ.get("TIMEOUT", "15"))

    API_TIMEOUT = int(os.environ.get("API_TIMEOUT", "10"))

    TEST_USER_ID = 22335519

    SCREENSHOTS_DIR = "screenshots"
    ALLURE_RESULTS_DIR = "allure-results"


settings = Settings()
