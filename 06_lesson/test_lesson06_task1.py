from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # Находим и нажимаем кнопку Start (используем CSS-селектор)
    start_btn = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_btn.click()

    # Ждём появления текста "Hello World!"
    hello_element = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
    )

    # Делаем скриншот
    driver.save_screenshot("screenshots/hello_world.png")

    # Проверяем текст
    assert hello_element.text == "Hello World!", \
        f"Текст не совпадает! Ожидалось 'Hello World!', \
            получено '{hello_element.text}'"

    driver.quit()
