"""
Упражнение 1. Клик по кнопке с CSS-классом
С исправлением SSL-ошибки и улучшенной обработкой исключений
"""

# Импорт необходимых модулей
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options  # Для настройки Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import (WebDriverException,
                                      NoSuchElementException,
                                      NoAlertPresentException)
import time


def setup_driver():
    """Настройка ChromeDriver с обработкой SSL-ошибок"""
    chrome_options = Options()

    # Добавляем опции для игнорирования SSL-ошибок
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument('--disable-gpu')

    # Инициализация драйвера с нашими настройками
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


def click_blue_button():
    """Основная функция для выполнения задания"""
    try:
        # 1. Настройка и запуск браузера
        driver = setup_driver()
        print("Браузер успешно запущен")

        # 2. Открытие целевой страницы
        driver.get("http://uitestingplayground.com/classattr")
        print("Страница успешно загружена")
        time.sleep(2)  # Ожидание загрузки

        # 3. Поиск и клик по кнопке
        try:
            blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
            blue_button.click()
            print("Клик по синей кнопке выполнен")
        except NoSuchElementException:
            print("Ошибка: Синяя кнопка не найдена")
            raise

        # 4. Обработка alert (если появится)
        try:
            alert = driver.switch_to.alert
            print(f"Обнаружено alert-окно: {alert.text}")
            alert.accept()
        except NoAlertPresentException:
            print("Alert-окно не появилось")

        # 5. Завершение работы
        time.sleep(1)
        driver.quit()
        print("Браузер закрыт. Скрипт выполнен успешно!")

    except WebDriverException as e:
        print(f"Ошибка WebDriver: {str(e)}")
        if 'driver' in locals():
            driver.quit()
    except Exception as e:
        print(f"Неожиданная ошибка: {str(e)}")
        if 'driver' in locals():
            driver.quit()


# Запуск скрипта
if __name__ == "__main__":
    print("=== Запуск скрипта ===")
    click_blue_button()

# python lesson05_task1.py
