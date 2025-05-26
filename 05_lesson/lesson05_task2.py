#  Клик по кнопке с динамическим ID (для начинающих)

# 1. Импортируем нужные библиотеки
from selenium import webdriver  # для управления браузером
from selenium.webdriver.common.by import By  # для поиска элементов
from selenium.webdriver.chrome.service import Service  # для настройки Chrome
from webdriver_manager.chrome import ChromeDriverManager  # авто установка дров
import time  # для пауз

# 2. Настраиваем браузер
try:
    # Автоматически скачиваем и устанавливаем драйвер Chrome
    service = Service(ChromeDriverManager().install())

    # Создаем окно браузера
    driver = webdriver.Chrome(service=service)

    # 3. Открываем нужную страницу
    print("Открываем страницу...")
    driver.get("http://uitestingplayground.com/dynamicid")
    time.sleep(2)  # ждем 2 секунды чтобы страница загрузилась

    # 4. Ищем кнопку по тегу и классу
    # Ищем элемент <button> с классом "btn-primary"
    print("Ищем кнопку...")
    button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")

    # 5. Кликаем по кнопке
    print("Кликаем по кнопке...")
    button.click()
    print("Успешно кликнули!")

    # 6. Ждем 3 секунды чтобы увидеть результат
    time.sleep(3)

except Exception as error:
    # Если что-то пошло не так
    print(f"Произошла ошибка: {error}")

finally:
    # 7. Закрываем браузер в любом случае
    print("Закрываем браузер...")
    driver.quit()
    print("Готово!")

# python lesson05_task2.py
