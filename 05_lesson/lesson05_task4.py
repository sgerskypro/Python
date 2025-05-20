# Форма авторизации
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

# Инициализация Firefox
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# Открытие страницы авторизации
driver.get("http://the-internet.herokuapp.com/login")

# Поиск и заполнение поля username
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")  # Ввод логина

# Поиск и заполнение поля password
password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")  # Ввод пароля

# Клик по кнопке Login (ищем по атрибуту type="submit")
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login_button.click()

# Небольшая пауза для загрузки страницы
time.sleep(2)

# Получение сообщения об успешной авторизации
flash_message = driver.find_element(By.ID, "flash").text

# Вывод первой строки сообщения (убираем символ ×)
print(flash_message.split("\n")[0])  # Пример: "You logged into a secure area!"

# Закрытие браузера
driver.quit()

"""
Комментарии:
1. Используем явные ожидания через time.sleep() для простоты
2. Локаторы ID стабильны и рекомендуются для форм
3. text.split("\n")[0] убирает лишние символы из сообщения
4. Выводим сообщение в консоль как требует задание
"""
