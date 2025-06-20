from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage:
    """Класс для работы со страницей авторизации"""

    def __init__(self, driver):
        """Инициализация страницы авторизации.

        :param driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу авторизации")
    def open(self):
        """Открывает страницу авторизации.

        :return: LoginPage - текущий экземпляр страницы
        """
        self.driver.get("https://www.saucedemo.com/")
        return self

    @allure.step("Ввести имя пользователя '{username}'")
    def enter_username(self, username: str):
        """Вводит имя пользователя в поле ввода.

        :param username: str - имя пользователя
        :return: LoginPage - текущий экземпляр страницы
        """
        username_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, "user-name")))
        username_field.clear()
        username_field.send_keys(username)
        return self

    @allure.step("Ввести пароль")
    def enter_password(self, password: str):
        """Вводит пароль в поле ввода.

        :param password: str - пароль пользователя
        :return: LoginPage - текущий экземпляр страницы
        """
        password_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, "password")))
        password_field.clear()
        password_field.send_keys(password)
        return self

    @allure.step("Нажать кнопку входа")
    def click_login(self):
        """Нажимает кнопку входа.

        :return: InventoryPage - экземпляр страницы товаров
        """
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "login-button")))
        login_button.click()
        return InventoryPage(self.driver)


class InventoryPage:
    """Класс для работы со страницей товаров"""

    def __init__(self, driver):
        """Инициализация страницы товаров.

        :param driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Добавить товар с ID '{item_id}' в корзину")
    def add_item_to_cart(self, item_id: str):
        """Добавляет товар в корзину по его ID.

        :param item_id: str - ID товара (например, "sauce-labs-backpack")
        :return: InventoryPage - текущий экземпляр страницы
        """
        add_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, f"add-to-cart-{item_id}")))
        add_button.click()
        self.wait.until(
            EC.element_to_be_clickable((By.ID, f"remove-{item_id}")))
        return self

    @allure.step("Перейти в корзину")
    def navigate_to_cart(self):
        """Переходит в корзину.

        :return: ShoppingCartPage - экземпляр страницы корзины
        """
        cart_button = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
        cart_button.click()
        return ShoppingCartPage(self.driver)


class ShoppingCartPage:
    """Класс для работы со страницей корзины"""

    def __init__(self, driver):
        """Инициализация страницы корзины.

        :param driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Получить список товаров в корзине")
    def get_cart_items(self) -> list:
        """Возвращает список товаров в корзине.

        :return: list - список названий товаров
        """
        items = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "inventory_item_name")
            )
        )
        return [item.text for item in items]

    @allure.step("Нажать кнопку оформления заказа")
    def click_checkout_button(self):
        """Нажимает кнопку оформления заказа.

        :return: CheckoutPage - экземпляр страницы оформления заказа
        """
        checkout_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()
        return CheckoutPage(self.driver)


class CheckoutPage:
    """Класс для работы со страницей оформления заказа"""

    def __init__(self, driver):
        """Инициализация страницы оформления заказа.

        :param driver: WebDriver - экземпляр веб-драйвера
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Ввести имя '{first_name}'")
    def input_first_name(self, first_name: str):
        """Вводит имя в форму оформления.

        :param first_name: str - имя покупателя
        :return: CheckoutPage - текущий экземпляр страницы
        """
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "first-name"))
        ).send_keys(first_name)
        return self

    @allure.step("Ввести фамилию '{last_name}'")
    def input_last_name(self, last_name: str):
        """Вводит фамилию в форму оформления.

        :param last_name: str - фамилия покупателя
        :return: CheckoutPage - текущий экземпляр страницы
        """
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        return self

    @allure.step("Ввести почтовый индекс '{zip_code}'")
    def input_zip_code(self, zip_code: str):
        """Вводит почтовый индекс в форму оформления.

        :param zip_code: str - почтовый индекс
        :return: CheckoutPage - текущий экземпляр страницы
        """
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        return self

    @allure.step("Перейти к обзору заказа")
    def continue_to_overview(self):
        """Переходит к обзору заказа.

        :return: CheckoutPage - текущий экземпляр страницы
        """
        self.driver.find_element(By.ID, "continue").click()
        return self

    @allure.step("Получить итоговую сумму заказа")
    def get_total_amount(self) -> float:
        """Возвращает итоговую сумму заказа.

        :return: float - итоговая сумма заказа
        """
        total_element = self.wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "summary_total_label")
            )
        )
        return float(total_element.text.split("$")[1])

    @allure.step("Завершить оформление заказа")
    def complete_order(self):
        """Завершает оформление заказа.

        :return: CheckoutPage - текущий экземпляр страницы
        """
        self.driver.find_element(By.ID, "finish").click()
        return self
