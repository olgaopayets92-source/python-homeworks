import pickle
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://gitflic.ru/")

input("👉 Войдите под ВТОРЫМ аккаунтом (вручную), пройдите 2FA, затем нажмите Enter...")

with open("cookies_user2.pkl", "wb") as f:
    pickle.dump(driver.get_cookies(), f)

print("✅ Куки второго аккаунта сохранены в cookies_user2.pkl")
driver.quit()