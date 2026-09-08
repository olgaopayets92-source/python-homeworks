"""
Тесты для интернет-магазина (SauceDemo) с Allure-разметкой.
"""
import allure
from page_objects.login_page import LoginPage
from page_objects.inventory_page import InventoryPage
from page_objects.cart_page import CartPage
from page_objects.checkout_page import CheckoutPage


@allure.epic("UI-тесты")
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
class TestShop:

    @allure.id("SHOP-1")
    @allure.story("Покупка товаров")
    @allure.title("Оформление заказа с тремя товарами")
    @allure.description(
        "Авторизуемся, добавляем три товара, "
        "заполняем форму и проверяем итоговую сумму"
    )
    def test_shop(self, chrome_driver):
        with allure.step(
            "Открыть страницу авторизации и войти как standard_user"
        ):
            login = LoginPage(chrome_driver)
            login.open()
            login.login("standard_user", "secret_sauce")

        with allure.step("Добавить три товара в корзину"):
            inventory = InventoryPage(chrome_driver)
            items = [
                "Sauce Labs Backpack",
                "Sauce Labs Bolt T-Shirt",
                "Sauce Labs Onesie"
            ]
            for item in items:
                inventory.add_item_to_cart(item)

        with allure.step("Перейти в корзину"):
            inventory.go_to_cart()

        with allure.step("Нажать кнопку Checkout"):
            cart = CartPage(chrome_driver)
            cart.proceed_to_checkout()

        with allure.step("Заполнить форму оформления"):
            checkout = CheckoutPage(chrome_driver)
            checkout.fill_checkout_form("Иван", "Петров", "123456")

        with allure.step("Нажать Continue и получить итоговую сумму"):
            checkout.continue_checkout()
            total = checkout.get_total()

        with allure.step("Проверить, что итоговая сумма равна $58.29"):
            assert total == 58.29, (
                f"Ожидалось 58.29, получено {total}"
            )
