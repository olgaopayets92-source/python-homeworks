from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    DELAY_INPUT = (By.ID, "delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self):
        url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        self.driver.get(url)
        return self

    def set_delay(self, seconds):
        delay_input = self.wait.until(
            EC.visibility_of_element_located(self.DELAY_INPUT)
        )
        delay_input.clear()
        delay_input.send_keys(str(seconds))
        return self

    def click_button(self, text):
        btn = self.driver.find_element(
            By.XPATH, f"//span[text()='{text}']"
        )
        btn.click()
        return self

    def wait_for_result(self, expected):
        self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, expected)
        )
        return self

    def get_result(self):
        return self.driver.find_element(*self.SCREEN).text
