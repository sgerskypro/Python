# 07_lesson/shop_pages.py
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Класс для работы со страницей авторизации"""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Ожидание элементов до 10 сек

    def open(self):
        """Открывает страницу авторизации"""
        self.driver.get("https://www.saucedemo.com/")
        return self

    def enter_username(self, username):
        """Вводит имя пользователя в поле ввода"""
        username_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, "user-name")))
        username_field.clear()
        username_field.send_keys(username)
        return self

    def enter_password(self, password):
        """Вводит пароль в поле ввода"""
        password_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, "password")))
        password_field.clear()
        password_field.send_keys(password)
        return self

    def click_login(self):
        """Нажимает кнопку входа и возвращает следующую страницу"""
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "login-button")))
        login_button.click()
        return InventoryPage(self.driver)


class InventoryPage:
    """Класс для работы со страницей товаров"""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_item_to_cart(self, item_id):
        """
        Добавляет товар в корзину по его ID
        :param item_id: ID товара (например, "sauce-labs-backpack")
        :return: self для цепочного вызова методов
        """
        add_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, f"add-to-cart-{item_id}")))
        add_button.click()
        # Проверяем, что кнопка изменилась на "Remove"
        self.wait.until(
            EC.element_to_be_clickable((By.ID, f"remove-{item_id}")))
        return self  # Важно: возвращаем self для цепочных вызовов

    def navigate_to_cart(self):
        """Переходит в корзину и возвращает страницу корзины"""
        cart_button = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        cart_button.click()
        return ShoppingCartPage(self.driver)


class ShoppingCartPage:
    """Класс для работы со страницей корзины"""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_cart_items(self):
        """Возвращает список товаров в корзине"""
        items = self.wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_name")))
        return [item.text for item in items]
    
    def click_checkout_button(self):
        """Нажимает кнопку оформления заказа"""
        checkout_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()
        return CheckoutPage(self.driver)


class CheckoutPage:
    """Класс для работы со страницей оформления заказа"""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def input_first_name(self, first_name):
        """Вводит имя в форму оформления"""
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))).send_keys(first_name)
        return self

    def input_last_name(self, last_name):
        """Вводит фамилию в форму оформления"""
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        return self

    def input_zip_code(self, zip_code):
        """Вводит почтовый индекс в форму оформления"""
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        return self

    def continue_to_overview(self):
        """Переходит к обзору заказа"""
        self.driver.find_element(By.ID, "continue").click()
        return self

    def get_total_amount(self):
        """Возвращает итоговую сумму заказа"""
        total_element = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_total_label")))
        # Извлекаем число из строки типа "Total: $58.29"
        return float(total_element.text.split("$")[1])

    def complete_order(self):
        """Завершает оформление заказа"""
        self.driver.find_element(By.ID, "finish").click()
        return self


# Пример использования с pytest
if __name__ == "__main__":
    # Тест можно запустить и напрямую для отладки
    options = Options()
    options.headless = False  # Для визуальной проверки
    driver = Firefox(options=options)

    try:
        # Тестовый сценарий
        login_page = LoginPage(driver).open()
        inventory_page = login_page.enter_username("standard_user")\
                                  .enter_password("secret_sauce")\
                                  .click_login()

        # Добавляем товары по их ID
        inventory_page.add_item_to_cart("sauce-labs-backpack")
        inventory_page.add_item_to_cart("sauce-labs-bolt-t-shirt")
        inventory_page.add_item_to_cart("sauce-labs-onesie")

        # Переходим в корзину
        cart_page = inventory_page.navigate_to_cart()
        checkout_page = cart_page.click_checkout_button()

        # Заполняем данные и завершаем заказ
        checkout_page.input_first_name("Иван")\
                    .input_last_name("Иванов")\
                    .input_zip_code("12345")\
                    .continue_to_overview()

        # Проверяем итоговую сумму
        total = checkout_page.get_total_amount()
        print(f"Итоговая сумма заказа: ${total}")
        assert total == 58.29, f"Ожидалась сумма $58.29, получено ${total}"

    finally:
        driver.quit()
