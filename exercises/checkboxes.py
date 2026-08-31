from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/checkboxes")

checkboxes = driver.find_elements(By.TAG_NAME, "input")

for i, checkbox in enumerate(checkboxes, 1):
    print(f"Чекбокс {i} выбрано: {checkbox.is_selected()}")

driver.quit()
