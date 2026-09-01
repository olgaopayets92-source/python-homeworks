from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME_INPUT)
        ).send_keys(first_name)

        last_input = self.driver.find_element(*self.LAST_NAME_INPUT)
        last_input.send_keys(last_name)

        postal_input = self.driver.find_element(*self.POSTAL_CODE_INPUT)
        postal_input.send_keys(postal_code)
        return self

    def continue_checkout(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_LABEL)
        )
        return self

    def get_total(self):
        total_text = self.driver.find_element(*self.TOTAL_LABEL).text
        return float(total_text.split("$")[1])
