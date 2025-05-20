# Работа с полем ввода
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Инициализация Firefox
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

# Открытие страницы с полем ввода
driver.get("http://the-internet.herokuapp.com/inputs")

# Поиск поля ввода по тегу <input>
input_field = driver.find_element(By.TAG_NAME, "input")

# Ввод текста "Sky"
input_field.send_keys("Sky")

# Очистка поля
input_field.clear()

# Ввод текста "Pro"
input_field.send_keys("Pro")

# Закрытие браузера
driver.quit()

"""
Особенности:
1. Используем Firefox вместо Chrome (по условию задания)
2. Поиск по тегу <input> так как это единственное поле на странице
3. Метод clear() очищает поле перед новым вводом
4. Метод send_keys() имитирует ввод с клавиатуры
"""
