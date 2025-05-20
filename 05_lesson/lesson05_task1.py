# Импорт необходимых модулей из Selenium Клик по кнопке с CSS-классом
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Инициализация Chrome браузера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Открытие целевой страницы
driver.get("http://uitestingplayground.com/classattr")

# Поиск синей кнопки по CSS-классу 'btn-primary'
# Точка перед именем класса означает поиск по классу в CSS
blue_button = driver.find_element(By.CSS_SELECTOR, ".btn-primary")

# Клик по найденной кнопке
blue_button.click()

# Закрытие браузера и завершение сессии
driver.quit()

"""
Примечания:
1. Используем ChromeDriverManager для автоматической загрузки драйвера
2. CSS_SELECTOR ".btn-primary" ищет элемент с классом btn-primary
3. Скрипт нужно запускать 3 раза вручную для проверки стабильности
"""
