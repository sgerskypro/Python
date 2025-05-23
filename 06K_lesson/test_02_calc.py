# Калькулятор   pytest test_02_calc.py  -v
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_calculator(browser):
    # 1. Открыть страницу калькулятора
    url = "https://bonigarcia.dev/selenium-webdriver-java/" \
          "slow-calculator.html"
    browser.get(url)

    # 2. Установить задержку 45 секунд
    delay_input = browser.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys("45")

    # 3. Выполнить вычисление: 7 + 8
    buttons = ["7", "+", "8", "="]
    for btn in buttons:
        xpath = f"//span[text()='{btn}']"
        browser.find_element(By.XPATH, xpath).click()

    # 4. Проверить результат через 45 секунд
    result = WebDriverWait(browser, 46).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "screen"), "15"))
    assert result
