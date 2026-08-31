from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def test_shop():
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    items = [
        ("Sauce Labs Backpack", "add-to-cart-sauce-labs-backpack"),
        ("Sauce Labs Bolt T-Shirt", "add-to-cart-sauce-labs-bolt-t-shirt"),
        ("Sauce Labs Onesie", "add-to-cart-sauce-labs-onesie"),
    ]
    for _, btn_id in items:
        driver.find_element(By.ID, btn_id).click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()

    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    driver.find_element(By.ID, "continue").click()

    total_element = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".summary_total_label")
        )
    )
    total_text = total_element.text
    total_value = total_text.split("$")[1]

    assert total_value == "58.29", (
        f"Итоговая сумма {total_value}, ожидалось 58.29"
    )

    driver.quit()
