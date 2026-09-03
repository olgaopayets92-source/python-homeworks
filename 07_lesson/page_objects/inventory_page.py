from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_item_to_cart(self, item_name):
        item_id = item_name.lower().replace(" ", "-")
        btn_locator = (By.ID, f"add-to-cart-{item_id}")
        self.wait.until(
            EC.element_to_be_clickable(btn_locator)
        ).click()
        return self

    def go_to_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
        self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart_list"))
        )
        return self
