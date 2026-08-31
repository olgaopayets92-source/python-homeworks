# from selenium import webdriver
# from time import sleep


# driver = webdriver.Chrome()
# driver.get("https://gitflic.ru/")
# sleep(2)


# # Получаем все cookies
# cookies = driver.get_cookies()

# for cookie in cookies:
#    print(f"{cookie['name']}: {cookie['value']}")

# driver.quit()
from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://gitflic.ru/")



# Добавляем cookie с токеном авторизации
driver.add_cookie({
   "name": "SESSION",
   "value": "MTg3YjU2ZTAtNzQwOS00MDUwLWI1ZmItOTNlYjI1NDEyZTQ2",
   "domain": "gitflic.ru"
})
# Добавляем cookie для окна подтверждения работы с cookie 
driver.add_cookie({
   "name": "cookiesAccepted",
   "value": "true",
   "domain": "gitflic.ru"
})
# Обновляем страницу, чтобы cookie применилась
driver.refresh()


# Теперь мы авторизованы!
# Можем сразу перейти в личный кабинет
driver.get("https://gitflic.ru/user/airsworld")
sleep(5)


# Удаляем все cookies (выходим из аккаунта)
driver.delete_all_cookies()


# Обновляем страницу
driver.refresh()
sleep(6)

driver.quit()