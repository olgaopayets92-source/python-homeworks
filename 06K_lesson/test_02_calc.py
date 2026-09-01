from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_calc():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    driver.get(url)

    delay_input = driver.find_element(By.ID, "delay")
    delay_input.clear()
    delay_input.send_keys("45")

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    wait = WebDriverWait(driver, 50)
    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), "15"
        )
    )

    result = driver.find_element(By.CSS_SELECTOR, ".screen")
    assert result.text == "15", f"Результат {result.text}, ожидалось 15"

    driver.quit()
