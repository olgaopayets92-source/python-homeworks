"""
Модуль с Page Object для страницы авторизации интернет-магазина.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage:
    """
    Класс для работы со страницей авторизации.

    Позволяет открыть страницу и выполнить вход.
    """

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы авторизации.

        :param driver: экземпляр WebDriver.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу авторизации")
    def open(self) -> "LoginPage":
        """
        Открыть страницу магазина.

        :return: текущий экземпляр страницы.
        """
        self.driver.get("https://www.saucedemo.com/")
        return self

    @allure.step("Выполнить вход с логином '{username}'")
    def login(self, username: str, password: str) -> "LoginPage":
        """
        Выполнить авторизацию с указанными учётными данными.

        :param username: логин.
        :param password: пароль.
        :return: текущий экземпляр страницы.
        """
        self.wait.until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        ).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
        )
        return self
