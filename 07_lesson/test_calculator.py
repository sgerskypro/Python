# Python\07_lesson\test_calculator.py
# pytest test_calculator.py -v
import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def browser():
    """Фикстура для инициализации и закрытия браузера."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator_with_delay(browser):
    """Тест проверяет работу калькулятора с задержкой."""
    # 1. Открываем страницу калькулятора
    browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    # 2. Создаем экземпляр Page Object
    calculator = CalculatorPage(browser)

    # 3. Устанавливаем задержку 45 секунд
    calculator.set_delay(45)

    # 4. Выполняем вычисление: 7 + 8 =
    calculator.click_button('7')
    calculator.click_button('+')
    calculator.click_button('8')
    calculator.click_button('=')

    # 5. Получаем результат и проверяем его
    result = calculator.get_result()
    expected_result = '15'
    assert result == expected_result, (
        f"Ожидался результат {expected_result}, но получено {result}"
    )

# pytest test_calculator.py -v
