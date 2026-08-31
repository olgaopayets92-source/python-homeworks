from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check_profile(profile_path, username):
    options = webdriver.ChromeOptions()
    options.add_argument(f"--user-data-dir={profile_path}")
    driver = webdriver.Chrome(options=options)
    driver.get("https://gitflic.ru/")
    input(f"Нажмите Enter, когда страница загрузится для {username}...")
    driver.save_screenshot(f"{username}_check.png")
    print(f"Скриншот сохранён как {username}_check.png")
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".user-menu")))
        print(f"✅ {username} – авторизация распознана (.user-menu)")
    except:
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".user-profile")))
            print(f"✅ {username} – авторизация распознана (.user-profile)")
        except:
            print(f"❌ {username} – не удалось найти элементы авторизации.")
    driver.quit()

# Проверяем оба профиля
check_profile("C:/selenium_profile_airsworld", "airsworld")
check_profile("C:/selenium_profile_olgaopayets92", "olgaopayets92")