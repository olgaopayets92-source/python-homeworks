import pickle
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://gitflic.ru/")

input("👉 Войдите под ПЕРВЫМ аккаунтом (airsworld) вручную, пройдите 2FA, затем нажмите Enter...")

with open("cookies.pkl", "wb") as f:
    pickle.dump(driver.get_cookies(), f)

print("✅ Куки первого аккаунта обновлены в cookies.pkl")
driver.quit()