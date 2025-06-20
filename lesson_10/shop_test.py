# pytest shop_test.py -v
# pytest shop_test.py --alluredir=allure_results
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from shop_pages import LoginPage, InventoryPage


@pytest.fixture
def browser():
    """Фикстура для инициализации и завершения работы браузера Firefox.

    :yield: WebDriver - экземпляр веб-драйвера Firefox
    """
    options = Options()
    options.headless = False
    driver = webdriver.Firefox(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Тесты интернет-магазина")
@allure.story("Проверка итоговой суммы заказа")
@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Проверка корректности расчета итоговой суммы заказа")
@allure.description("Проверка, что сумма заказа рассчитывается корректно")
def test_checkout_total(browser):
    with allure.step("Открыть страницу авторизации"):
        browser.get("https://www.saucedemo.com")

    with allure.step("Авторизоваться под стандартным пользователем"):
        login_page = LoginPage(browser)
        login_page.enter_username("standard_user") \
                  .enter_password("secret_sauce") \
                  .click_login()

    with allure.step("Добавить три товара в корзину"):
        product_page = InventoryPage(browser)
        product_page.add_item_to_cart("sauce-labs-backpack") \
                    .add_item_to_cart("sauce-labs-bolt-t-shirt") \
                    .add_item_to_cart("sauce-labs-onesie")

    with allure.step("Перейти в корзину"):
        cart_page = product_page.navigate_to_cart()

    with allure.step("Оформить заказ"):
        checkout_page = cart_page.click_checkout_button()
        checkout_page.input_first_name("Светлана") \
                     .input_last_name("Геарсимова") \
                     .input_zip_code("12345") \
                     .continue_to_overview()

    with allure.step("Проверить итоговую сумму заказа"):
        total = checkout_page.get_total_amount()
        expected = 58.29
        assert total == expected, \
            f"Ожидаемая сумма: 58.29, получено: {total}"

    with allure.step("Завершить оформление заказа"):
        checkout_page.complete_order()
