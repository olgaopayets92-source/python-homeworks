from page_objects.calculator_page import CalculatorPage


def test_calculator(chrome_driver):
    calc = CalculatorPage(chrome_driver)
    calc.open()
    calc.set_delay(45)
    calc.click_button("7")
    calc.click_button("+")
    calc.click_button("8")
    calc.click_button("=")
    calc.wait_for_result("15")
    result = calc.get_result()
    assert result == "15", f"Ожидалось 15, получено {result}"
