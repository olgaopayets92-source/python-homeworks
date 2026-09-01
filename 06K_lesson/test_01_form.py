from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def test_form():
    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service)
    wait = WebDriverWait(driver, 10)

    url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    driver.get(url)

    wait.until(EC.presence_of_element_located((By.NAME, "first-name")))
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "zip-code").clear()
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    try:
        driver.switch_to.alert.dismiss()
    except Exception:
        pass

    zip_element = wait.until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )
    assert "alert-danger" in zip_element.get_attribute("class"), (
        "Zip code не подсвечен красным"
    )

    success_elements = driver.find_elements(
        By.CSS_SELECTOR, ".alert-success"
    )
    assert len(success_elements) == 9, (
        f"Найдено {len(success_elements)} зелёных, ожидалось 9"
    )

    driver.quit()
