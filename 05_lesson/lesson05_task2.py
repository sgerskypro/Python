# Клик по кнопке без ID
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Инициализация Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Открытие страницы с динамическим ID
driver.get("http://uitestingplayground.com/dynamicid")

"""
Поиск кнопки по комбинации тега и класса:
- 'button' - ищем элемент <button>
- '.btn-primary' - с классом btn-primary
Это стабильный селектор, так как ID меняется при каждом обновлении
"""
dynamic_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
dynamic_button.click()

# Завершение работы
driver.quit()

"""
Важные моменты:
1. Не используем ID, так как оно динамическое
2. Комбинация тега+класса дает стабильный локатор
3. Как и в первом задании - запускаем 3 раза вручную
"""
