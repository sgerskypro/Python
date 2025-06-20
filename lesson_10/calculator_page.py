from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException
)
import allure


class CalculatorPage:
    def __init__(self, driver):
        """Инициализация страницы калькулятора.

        :param driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_display = (By.CSS_SELECTOR, ".screen")
        self.buttons = {
            '7': (By.XPATH, "//span[text()='7']"),
            '8': (By.XPATH, "//span[text()='8']"),
            '+': (By.XPATH, "//span[text()='+']"),
            '=': (By.XPATH, "//span[text()='=']"),
        }

    @allure.step("Установить задержку вычислений на {seconds} секунд")
    def set_delay(self, seconds: int) -> None:
        """Устанавливает задержку вычислений в секундах.

        :param seconds: int - количество секунд задержки
        """
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    @allure.step("Нажать кнопку '{button}'")
    def click_button(self, button: str) -> None:
        """Нажимает указанную кнопку на калькуляторе.

        :param button: str - символ кнопки (например, '7', '+', '=')
        :raises ValueError: если кнопка не определена в локаторах
        """
        if button in self.buttons:
            self.driver.find_element(*self.buttons[button]).click()
        else:
            raise ValueError(f"Кнопка '{button}' не определена в локаторах")

    @allure.step("Получить результат вычислений")
    def get_result(self, timeout: int = 50) -> str:
        """Получает результат с калькулятора после выполнения вычислений.

        :param timeout: int - макс время ожидания в секундах (по умолчанию 50)
        :return: str - результат вычислений
        :raises TimeoutException: если результат не появился за указанное время
        :raises NoSuchElementException: если элемент результата не найден
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.find_element(
                    *self.result_display
                ).text.isdigit()
            )
            return self.driver.find_element(
                *self.result_display
            ).text
        except TimeoutException:
            current_text = self.driver.find_element(
                *self.result_display
            ).text
            raise TimeoutException(
                f"Результат не появился за {timeout} секунд. "
                f"Текущий текст: '{current_text}'"
            )
        except NoSuchElementException:
            raise NoSuchElementException(
                "Элемент результата не найден на странице"
            )
