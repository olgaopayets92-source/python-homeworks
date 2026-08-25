from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.maximize_window()

    # 1. Открыть главную страницу
    driver.get("https://httpbin.qa-territory.online/")
    sleep(2)

    # 2. Найти ссылку "HTML Form" и кликнуть
    link = driver.find_element(By.LINK_TEXT, "HTML Form")
    link.click()
    sleep(2)

    # 3. Проверить, что URL изменился (содержит /forms/post)
    current_url = driver.current_url
    assert "/forms/post" in current_url, \
        f"URL не содержит /forms/post, текущий URL: {current_url}"
    print("URL изменился корректно")

    # 4. Вернуться назад
    driver.back()
    sleep(2)

    # 5. Проверить, что вернулись на исходный URL
    assert driver.current_url == "https://httpbin.qa-territory.online/", \
        f"Не удалось вернуться на главную, текущий URL: {driver.current_url}"
    print("Вернулись на главную страницу")

    driver.quit()
