import allure
from page_objects.calculator_page import CalculatorPage


@allure.epic("UI-тесты")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
class TestCalculator:

    @allure.id("CALC-1")
    @allure.story("Сложение чисел с задержкой")
    @allure.title("Проверка работы калькулятора с задержкой 45 секунд")
    @allure.description(
        "Вводим выражение 7 + 8, ждём 45 секунд и проверяем результат 15"
    )
    def test_calculator(self, chrome_driver):
        """
        Тест проверяет, что калькулятор корректно вычисляет 7 + 8
        при установленной задержке 45 секунд.
        """
        with allure.step("Открыть страницу калькулятора"):
            calc = CalculatorPage(chrome_driver)
            calc.open()

        with allure.step("Установить задержку 45 секунд"):
            calc.set_delay(45)

        with allure.step("Ввести выражение 7 + 8"):
            calc.click_button("7")
            calc.click_button("+")
            calc.click_button("8")

        with allure.step("Нажать кнопку ="):
            calc.click_button("=")

        with allure.step("Дождаться результата 15"):
            calc.wait_for_result("15")
            result = calc.get_result()

        with allure.step("Проверить, что результат равен 15"):
            assert result == "15", f"Ожидалось 15, получено {result}"
