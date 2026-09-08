"""
Модуль с Page Object для страницы калькулятора с задержкой (Slow Calculator).
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    Класс для работы со страницей медленного калькулятора.

    Позволяет установить задержку перед вычислением, нажимать кнопки,
    ожидать результат и получать его значение.
    """

    # Локаторы элементов
    DELAY_INPUT = (By.ID, "delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы калькулятора.

        :param driver: экземпляр WebDriver (Chrome).
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self) -> "CalculatorPage":
        """
        Открыть страницу калькулятора в браузере.

        :return: текущий экземпляр страницы (для цепочки вызовов).
        """
        url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        self.driver.get(url)
        return self

    def set_delay(self, seconds: int) -> "CalculatorPage":
        """
        Установить задержку в поле ввода (в секундах).

        :param seconds: количество секунд задержки (целое число).
        :return: текущий экземпляр страницы.
        """
        delay_input = self.wait.until(
            EC.visibility_of_element_located(self.DELAY_INPUT)
        )
        delay_input.clear()
        delay_input.send_keys(str(seconds))
        return self

    def click_button(self, text: str) -> "CalculatorPage":
        """
        Нажать на кнопку калькулятора с указанным текстом.

        :param text: текст на кнопке (например, "7", "+", "=").
        :return: текущий экземпляр страницы.
        """
        btn = self.driver.find_element(
            By.XPATH, f"//span[text()='{text}']"
        )
        btn.click()
        return self

    def wait_for_result(self, expected: str) -> "CalculatorPage":
        """
        Ожидать появления указанного текста на экране калькулятора.

        :param expected: ожидаемый результат (строка, например, "15").
        :return: текущий экземпляр страницы.
        """
        self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, expected)
        )
        return self

    def get_result(self) -> str:
        """
        Получить текущий текст, отображаемый на экране калькулятора.

        :return: строка с результатом вычисления.
        """
        return self.driver.find_element(*self.SCREEN).text
