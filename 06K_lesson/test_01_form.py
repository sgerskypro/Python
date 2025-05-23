# Форма pytest test_01_form.py -v
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    # Инициализация браузера перед тестом
    driver = webdriver.Chrome()
    yield driver
    # Закрытие браузера после теста
    driver.quit()


def test_form_submission(browser):
    # 1. Открыть страницу
    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    browser.get(url)

    # Ожидание загрузки страницы
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.NAME, "first-name"))
    )

    # 2. Заполнить форму значениями
    fields_to_fill = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for field_name, value in fields_to_fill.items():
        browser.find_element(By.NAME, field_name).send_keys(value)

    # 3. Нажать кнопку Submit
    submit_locator = (By.CSS_SELECTOR, "button[type='submit']")
    submit_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(submit_locator)
    )
    submit_button.click()

    # Ожидание применения стилей
    zip_code_selector = "#zip-code.alert-danger"
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, zip_code_selector))
    )

    # 4. Проверить подсветку поля Zip code
    zip_code_field = browser.find_element(By.ID, "zip-code")
    assert "alert-danger" in zip_code_field.get_attribute("class")

    # 5. Проверить подсветку остальных полей
    green_fields = [
        "first-name", "last-name", "address",
        "e-mail", "phone", "city",
        "country", "job-position", "company"
    ]

    for field_id in green_fields:
        field = browser.find_element(By.ID, field_id)
        assert "alert-success" in field.get_attribute("class")
