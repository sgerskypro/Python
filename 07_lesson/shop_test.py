# file: shop_test.py
# pytest shop_test.py -v
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from shop_pages import LoginPage, InventoryPage

@pytest.fixture
def browser():
    """Фикстура для инициализации и завершения работы браузера Firefox"""
    # Настройка опций Firefox
    options = Options()
    options.headless = False  # Для визуального наблюдения установите False

    # Инициализация драйвера Firefox
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()  # Максимизируем окно браузера

    yield driver  # Возвращаем драйвер тестовой функции

    # Завершаем работу после теста
    driver.quit()


def test_checkout_total(browser):
    """Тест проверки итоговой суммы заказа с использованием Firefox"""
    # 1. Открываем страницу авторизации
    browser.get("https://www.saucedemo.com")

    # 2. Авторизация
    login_page = LoginPage(browser)
    login_page.enter_username("standard_user") \
              .enter_password("secret_sauce") \
              .click_login()

    # 3. Добавление товаров в корзину
    product_page = InventoryPage(browser)
    product_page.add_item_to_cart("sauce-labs-backpack") \
                .add_item_to_cart("sauce-labs-bolt-t-shirt") \
                .add_item_to_cart("sauce-labs-onesie")

    # 4. Переход в корзину
    cart_page = product_page.navigate_to_cart()

    # 5. Оформление заказа
    checkout_page = cart_page.click_checkout_button()
    checkout_page.input_first_name("Иван") \
                .input_last_name("Иванов") \
                .input_zip_code("12345") \
                .continue_to_overview()

    # 6. Проверка итоговой суммы
    total = checkout_page.get_total_amount()
    assert total == 58.29, f"Ожидаемая сумма: 58.29, получено: {total}"

    # 7. Завершение заказа (опционально)
    checkout_page.complete_order()

    # pytest shop_test.py -v
