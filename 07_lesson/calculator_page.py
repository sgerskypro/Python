# Python\07_lesson\calculator_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException
)


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_display = (By.CSS_SELECTOR, ".screen")

        self.buttons = {
            '7': (By.XPATH, "//span[text()='7']"),
            '8': (By.XPATH, "//span[text()='8']"),
            '+': (By.XPATH, "//span[text()='+']"),
            '=': (By.XPATH, "//span[text()='=']"),
        }

    def set_delay(self, seconds):
        delay_field = self.driver.find_element(*self.delay_input)
        delay_field.clear()
        delay_field.send_keys(str(seconds))

    def click_button(self, button):
        if button in self.buttons:
            self.driver.find_element(*self.buttons[button]).click()
        else:
            raise ValueError(
                f"Кнопка '{button}' не определена в локаторах"
            )

    def get_result(self, timeout=50):
        """
        Получает результат с калькулятора после выполнения вычислений.
        Ждет, пока на экране отобразится только результат (число).

       timeout: Максимальное время ожидания в секундах

        возвращает str: Результат вычислений

        Raises:
            TimeoutException: Если результат не появился за указанное время
            NoSuchElementException: Если элемент результата не найден
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
