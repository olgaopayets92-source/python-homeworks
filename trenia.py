# from selenium import webdriver
# from selenium.webdriver.common.by import By

# def test_page_title():
#     driver = webdriver.Chrome()
#     driver.get("https://httpbin.qa-territory.online/")

#     title = driver.find_element(By.TAG_NAME, "h1")
#     assert "httpbin" in title.text.lower()

#     driver.quit()
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# def test_form_interaction():
#     driver = webdriver.Chrome()
#     driver.get("https://httpbin.qa-territory.online/forms/post")

#     # Заполните поле "custname" значением "Иван Иванов"
#     name_field = driver.find_element(By.NAME, "custname")
#     name_field.send_keys("Иван Иванов")

#     # Найдите кнопку отправки и кликните на нее
#     submit_btn = driver.find_element(By.XPATH, "//button[text()='Submit order']")
#     submit_btn.click()

#     driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_element_state():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/radio-button")

    # Найдите радио-кнопку "Yes" и проверьте:
    radio_btn = driver.find_element(By.ID, "yesRadio")

    # 1. Что она отображается
    assert radio_btn.is_displayed() == True

    # 2. Что она доступна для клика (через метку)
    label = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
    assert label.is_enabled() == True

    driver.quit()