"""
Модуль с Page Object для главной страницы магазина (инвентарь).
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class InventoryPage:
    """
    Класс для работы со страницей товаров.
    Позволяет добавлять товары в корзину и переходить в корзину.
    """

    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы товаров.

        :param driver: экземпляр WebDriver.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Добавить товар '{item_name}' в корзину")
    def add_item_to_cart(self, item_name: str) -> "InventoryPage":
        """
        Добавить товар в корзину по его полному имени.

        :param item_name: полное название товара.
        :return: текущий экземпляр страницы.
        """
        item_id = item_name.lower().replace(" ", "-")
        btn_locator = (By.ID, f"add-to-cart-{item_id}")
        self.wait.until(
            EC.element_to_be_clickable(btn_locator)
        ).click()
        return self

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> "InventoryPage":
        """
        Нажать на иконку корзины и дождаться загрузки страницы корзины.

        :return: текущий экземпляр страницы.
        """
        self.driver.find_element(*self.CART_LINK).click()
        self.wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "cart_list")
            )
        )
        return self
