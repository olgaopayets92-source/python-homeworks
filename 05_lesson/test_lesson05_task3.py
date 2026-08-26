from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.maximize_window()

    # 1. Открыть страницу со ссылками
    driver.get("https://httpbin.qa-territory.online/links/10")

    # 2. Найти все ссылки (<a>)
    links = driver.find_elements(By.TAG_NAME, "a")

    # 3. Проверить, что количество ссылок равно 9
    assert len(links) == 9, \
        f"Ожидалось 9 ссылок, найдено {len(links)}"

    # 4. Проверить, что все ссылки отображаются на странице
    for i, link in enumerate(links, 1):
        assert link.is_displayed(), f"Ссылка {i} не отображается"

    # 5. Проверить, что текст первой ссылки содержит "1"
    assert "1" in links[0].text, \
        f"Текст первой ссылки не содержит '1', текст: '{links[0].text}'"

    print("Все проверки пройдены")
    driver.quit()
