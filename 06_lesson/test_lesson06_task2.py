import os
import pickle
from selenium import webdriver


def test_session_storage_auth():
    os.makedirs("screenshots", exist_ok=True)
    driver = webdriver.Chrome()
    driver.get("https://gitflic.ru/")

    # Первый пользователь (airsworld)
    with open("cookies.pkl", "rb") as f:
        cookies1 = pickle.load(f)
    for cookie in cookies1:
        driver.add_cookie(cookie)
    driver.refresh()
    driver.get("https://gitflic.ru/user/airsworld")
    url1 = driver.current_url
    print(f"URL первого пользователя: {url1}")

    # Второй пользователь (olgaopayets92)
    driver.delete_all_cookies()
    driver.get("https://gitflic.ru/")
    with open("cookies_user2.pkl", "rb") as f:
        cookies2 = pickle.load(f)
    for cookie in cookies2:
        driver.add_cookie(cookie)
    driver.refresh()
    driver.get("https://gitflic.ru/user/olgaopayets92")
    url2 = driver.current_url
    print(f"URL второго пользователя: {url2}")

    assert url1 != url2, f"URL совпадают: {url1} == {url2}"
    print("✅ Тест пройден")

    driver.quit()
