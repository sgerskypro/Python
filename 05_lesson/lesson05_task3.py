# Учимся работать с полем ввода на сайте (для начинающих)

# 1. Подключаем нужные инструменты
from selenium import webdriver  # для управления браузером
from selenium.webdriver.common.by import By  # для поиска элементов
from selenium.webdriver.firefox.service import Service  # для настройки Firefox
from webdriver_manager.firefox import GeckoDriverManager  # авто установка дров
import time  # для пауз

# 2. Настраиваем Firefox
try:
    print("Настраиваем Firefox...")
    # Автоматически скачиваем и устанавливаем драйвер
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    # 3. Открываем страницу с полем ввода
    print("Открываем страницу...")
    driver.get("http://the-internet.herokuapp.com/inputs")
    time.sleep(2)  # ждем загрузки страницы

    # 4. Находим поле ввода (единственное на странице)
    print("Ищем поле ввода...")
    input_field = driver.find_element(By.TAG_NAME, "input")

    # 5. Вводим текст "Sky"
    print("Вводим 'Sky'...")
    input_field.send_keys("Sky")
    time.sleep(1)  # ждем 1 секунду

    # 6. Очищаем поле
    print("Очищаем поле...")
    input_field.clear()
    time.sleep(1)

    # 7. Вводим текст "Pro"
    print("Вводим 'Pro'...")
    input_field.send_keys("Pro")
    time.sleep(1)

    print("Все действия выполнены успешно!")

except Exception as error:
    # Если что-то пошло не так
    print(f"Ой, произошла ошибка: {error}")

finally:
    # 8. Закрываем браузер в любом случае
    print("Закрываем браузер...")
    driver.quit()
    print("Работа завершена!")

# python lesson05_task3.py
