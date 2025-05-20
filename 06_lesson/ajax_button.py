#   Задание 1 - Нажать на кнопку
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time  # Добавляем для отладки

# Инициализация драйвера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # 1. Открываем страницу
    print("Открываем страницу...")
    driver.get("http://uitestingplayground.com/ajax")

    # 2. Находим и кликаем кнопку
    print("Ищем кнопку...")
    ajax_button = driver.find_element(By.ID, "ajaxButton")
    ajax_button.click()
    print("Кнопка нажата")

    # 3. Ожидаем появления зеленой плашки (добавляем проверки)
    print("Ожидаем сообщение...")
    start_time = time.time()

    try:
        message_element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "p.bg-success"))
        )
        print(f"Сообщение найдено за {time.time()-start_time:.2f} сек")

        # 4. Получаем и выводим текст
        message = message_element.text
        print("Текст сообщения:", message)

    except Exception as e:
        print("Ошибка при ожидании элемента:", str(e))
        print("Текущий HTML страницы:")
        print(driver.page_source[:1000])  # Выводим часть HTML для отладки

finally:
    # Закрываем браузер
    driver.quit()
    print("Браузер закрыт")
