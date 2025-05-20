# Задание 2 - Переименовать кнопку
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Инициализация драйвера Chrome с правильным форматом для Selenium 4+
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # 1. Переход на страницу
    driver.get("http://uitestingplayground.com/textinput")

    # 2. Ввод текста в поле
    input_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
    input_field.clear()  # Очищаем поле перед вводом
    input_field.send_keys("SkyPro")

    # 3. Нажатие на синюю кнопку
    button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
    button.click()

    # 4. Получение и вывод текста кнопки
    # Добавляем небольшую задержку через неявное ожидание
    driver.implicitly_wait(2)  # Ждем до 2 секунд
    button_text = button.text
    print("Текст кнопки:", button_text)  # Должно быть "SkyPro"

finally:
    # Закрытие браузера
    driver.quit()
