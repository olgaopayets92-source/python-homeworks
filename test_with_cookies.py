import os
import pickle
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.makedirs("screenshots", exist_ok=True)

def close_cookie_banner(driver, wait):
    """Закрывает баннер cookie, если он есть (сначала клик, если не получается — через JS)"""
    try:
        # Ждём появления баннера (небольшой таймаут, чтобы не замедлять)
        cookie_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cookies-text .cookiesBtn")))
        # Прокручиваем к кнопке
        driver.execute_script("arguments[0].scrollIntoView(true);", cookie_btn)
        time.sleep(0.5)
        try:
            cookie_btn.click()
        except:
            # Если клик перехвачен — используем JavaScript
            driver.execute_script("arguments[0].click();", cookie_btn)
        time.sleep(1)
        return True
    except:
        # Баннер не появился — всё хорошо
        return False

driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 30)  # увеличенный таймаут

try:
    # 1. Загружаем куки и переходим на главную
    driver.get("https://gitflic.ru/")
    try:
        with open("cookies.pkl", "rb") as f:
            cookies = pickle.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
        time.sleep(2)
    except FileNotFoundError:
        print("⚠️ Файл cookies.pkl не найден. Возможно, нужно войти вручную.")

    # Закрываем баннер на главной
    close_cookie_banner(driver, wait)

    # 2. Переходим на страницу настроек
    driver.get("https://gitflic.ru/settings/profile")
    time.sleep(2)
    close_cookie_banner(driver, wait)
    driver.save_screenshot("screenshots/settings_page.png")
    print("📸 Страница настроек открыта")

    # 3. Заполняем поля
    name_input = wait.until(EC.presence_of_element_located((By.ID, "name")))
    name_input.clear()
    name_input.send_keys("Username")

    surname_input = driver.find_element(By.ID, "surname")
    surname_input.clear()
    surname_input.send_keys("Surname")

    # 4. Сохраняем (с прокруткой и JS-кликом)
    save_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".gf-button.--success")))
    driver.execute_script("arguments[0].scrollIntoView(true);", save_btn)
    time.sleep(1)
    try:
        save_btn.click()
    except:
        driver.execute_script("arguments[0].click();", save_btn)
    print("✅ Изменения сохранены")
    time.sleep(2)

    # 5. Переходим в публичный профиль для проверки
    driver.get("https://gitflic.ru/user/airsworld")
    time.sleep(2)
    close_cookie_banner(driver, wait)  # ОБЯЗАТЕЛЬНО закрываем баннер перед поиском
    driver.save_screenshot("screenshots/full_page_after.png")

    # 6. Ищем имя пользователя (с увеличенным таймаутом)
    user_name = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h6.mb-0")))
    user_name.screenshot("screenshots/user_name.png")

    # Сравниваем
    assert user_name.text == "Username Surname", f"Имя не совпадает: {user_name.text}"
    print("✅ Тест пройден!")

except Exception as e:
    print(f"❌ Ошибка: {e}")
    driver.save_screenshot("screenshots/error_screenshot.png")
    with open("screenshots/error_page.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    raise
finally:
    driver.quit()