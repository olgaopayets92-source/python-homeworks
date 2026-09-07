"""
Модуль с Page Object для страницы оформления заказа.
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CheckoutPage:
    """
    Класс для работы со страницей оформления заказа.

    Позволяет заполнить форму, продолжить и получить итоговую сумму.
    """

    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы оформления.

        :param driver: экземпляр WebDriver.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Заполнить форму оформления заказа")
    def fill_checkout_form(
        self,
        first_name: str,
        last_name: str,
        postal_code: str
    ) -> "CheckoutPage":
        """
        Заполнить поля формы: имя, фамилия, почтовый индекс.

        :param first_name: имя покупателя.
        :param last_name: фамилия покупателя.
        :param postal_code: почтовый индекс.
        :return: текущий экземпляр страницы.
        """
        self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME_INPUT)
        ).send_keys(first_name)

        last_input = self.driver.find_element(*self.LAST_NAME_INPUT)
        last_input.send_keys(last_name)

        postal_input = self.driver.find_element(*self.POSTAL_CODE_INPUT)
        postal_input.send_keys(postal_code)
        return self

    @allure.step("Нажать кнопку Continue")
    def continue_checkout(self) -> "CheckoutPage":
        """
        Нажать кнопку Continue и дождаться загрузки итоговой страницы.

        :return: текущий экземпляр страницы.
        """
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_LABEL)
        )
        return self

    @allure.step("Получить итоговую сумму")
    def get_total(self) -> float:
        """
        Получить итоговую стоимость заказа.

        :return: сумма в виде числа с плавающей точкой.
        """
        total_text = self.driver.find_element(*self.TOTAL_LABEL).text
        return float(total_text.split("$")[1])
