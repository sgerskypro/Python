# Автоматическая авторизация на сайте (для начинающих)

# 1. Подключаем нужные инструменты
from selenium import webdriver  # для управления браузером
from selenium.webdriver.common.by import By  # для поиска элементов
from selenium.webdriver.firefox.service import Service  # для настройки Firefox
from webdriver_manager.firefox import GeckoDriverManager  # автоя установка дров
import time  # для пауз

# 2. Настраиваем Firefox
try:
    print("Запускаем Firefox...")
    # Автоматически устанавливаем и настраиваем драйвер
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    # 3. Открываем страницу авторизации
    print("Открываем страницу входа...")
    driver.get("http://the-internet.herokuapp.com/login")
    time.sleep(2)  # ждем загрузки страницы

    # 4. Вводим логин
    print("Вводим логин...")
    username = driver.find_element(By.ID, "username")
    username.send_keys("tomsmith")  # стандартный логин с сайта

    # 5. Вводим пароль
    print("Вводим пароль...")
    password = driver.find_element(By.ID, "password")
    password.send_keys("SuperSecretPassword!")  # стандартный пароль

    # 6. Нажимаем кнопку входа
    print("Нажимаем кнопку Login...")
    login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_btn.click()
    time.sleep(2)  # ждем авторизации

    # 7. Получаем сообщение об успешном входе
    message = driver.find_element(By.ID, "flash").text
    print("Сообщение после входа:", message.split("\n")[0])

    print("Авторизация прошла успешно!")

except Exception as error:
    # Если что-то пошло не так
    print(f"Ошибка: {error}")

finally:
    # 8. Закрываем браузер в любом случае
    print("Закрываем Firefox...")
    driver.quit()
    print("Готово!")

# python lesson05_task4.py
