from page_objects.login_page import LoginPage
from page_objects.inventory_page import InventoryPage
from page_objects.cart_page import CartPage
from page_objects.checkout_page import CheckoutPage


def test_shop(firefox_driver):
    login = LoginPage(firefox_driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(firefox_driver)
    items = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]
    for item in items:
        inventory.add_item_to_cart(item)
    inventory.go_to_cart()

    cart = CartPage(firefox_driver)
    cart.proceed_to_checkout()

    checkout = CheckoutPage(firefox_driver)
    checkout.fill_checkout_form("Иван", "Петров", "123456")
    checkout.continue_checkout()

    total = checkout.get_total()
    assert total == 58.29, f"Ожидалось 58.29, получено {total}"
