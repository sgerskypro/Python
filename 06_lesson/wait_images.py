# Задание 3 - Дождаться картинки
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    # 1. Инициализация драйвера
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # 2. Переход на страницу
        url = "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
        driver.get(url)

        # 3. Ожидание загрузки (исчезновение спиннера)
        WebDriverWait(driver, 15).until(
            EC.invisibility_of_element_located((By.ID, "spinner"))
        )

        # 4. Получение всех изображений
        images = driver.find_elements(
            By.CSS_SELECTOR, 
            "#image-container img"
        )

        # 5. Проверка загрузки
        if len(images) < 3:
            raise Exception("Не все картинки загрузились")

        # 6. Получение src третьей картинки
        third_img_src = images[2].get_attribute("src")
        print("SRC третьей картинки:", third_img_src)

    except Exception as e:
        print("Произошла ошибка:", str(e))
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
