# pytest test_calculator.py -v
#  pytest test_calculator.py --alluredir=allure_results
import pytest
import allure
from selenium import webdriver
from calculator_page import CalculatorPage


@pytest.fixture
def browser():
    """Фикстура для инициализации и закрытия браузера.

    :yield: WebDriver - экземпляр веб-драйвера
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Тесты калькулятора")
@allure.story("Тест калькулятора с задержкой")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Проверка работы калькулятора с задержкой 45 секунд")
@allure.description("Тест проверяет корректность вычислений "
                    "калькулятора с установленной задержкой")
def test_calculator_with_delay(browser):
    with allure.step("Открыть страницу калькулятора"):
        browser.get("https://bonigarcia.dev/selenium-webdriver-java/"
                    "slow-calculator.html")

    with allure.step("Создать экземпляр Page Object"):
        calculator = CalculatorPage(browser)

    with allure.step("Установить задержку 45 секунд"):
        calculator.set_delay(45)

    with allure.step("Выполнить вычисление: 7 + 8 ="):
        calculator.click_button('7')
        calculator.click_button('+')
        calculator.click_button('8')
        calculator.click_button('=')

    with allure.step("Проверить результат вычислений"):
        result = calculator.get_result()
        expected_result = '15'
        assert result == expected_result, (
            f"Ожидался результат {expected_result}, но получено {result}"
        )
