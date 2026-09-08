"""
Модуль с Page Object для страницы корзины интернет-магазина.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CartPage:
    """
    Класс для работы со страницей корзины.

    Позволяет перейти к оформлению заказа.
    """

    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы корзины.

        :param driver: экземпляр WebDriver.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Перейти к оформлению заказа")
    def proceed_to_checkout(self) -> "CartPage":
        """
        Нажать кнопку Checkout и дождаться загрузки страницы оформления.

        :return: текущий экземпляр страницы.
        """
        self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        ).click()
        self.wait.until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        return self
