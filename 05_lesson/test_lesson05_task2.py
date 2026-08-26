from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.maximize_window()

    # 1. Открыть страницу формы
    driver.get("https://httpbin.qa-territory.online/forms/post")
    sleep(2)

    # 2. Найти поле "custname" и ввести имя
    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Ольга Опаец")
    sleep(1)

    # 3. Найти кнопку "Submit order" и кликнуть
    submit_btn = driver.find_element(
        By.XPATH, "//button[text()='Submit order']")
    submit_btn.click()
    sleep(2)

    # 4. Проверяем, что URL изменился
    expected_url = "https://httpbin.qa-territory.online/forms/post"
    assert driver.current_url != expected_url, (
        "URL не изменился после отправки формы"
    )
    print("URL изменился успешно")

    driver.quit()
