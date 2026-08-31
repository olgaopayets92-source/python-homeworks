# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.by import By


# driver = webdriver.Chrome()
# driver.get("https://gitflic.ru")

# sleep(2)

# click_button = driver.find_element(By.CLASS_NAME, "button-start")
# click_button.click()
# sleep(2)

# # Находим поле почты по ID и вводим логин
# input_login = driver.find_element(By.ID, "email")
# input_login.send_keys("in6vq@airsworld.net")

# # Находим поле пароля по ID и вводим пароль
# input_password = driver.find_element(By.ID, "passwordBasic")
# input_password.send_keys("12345Qwerty")

# # Нажимаем кнопку входа
# submit_button = driver.find_element(By.CLASS_NAME, "btn-success")
# submit_button.click()
# sleep(5)

# driver.quit()

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://gitflic.ru")
driver.maximize_window()  # Разворачиваем окно на весь экран

# Закрываем баннер с куки
driver.find_element(By.CLASS_NAME, "cookiesBtn").click()
sleep(2)

# Кликаем по кнопке "Начать работу"
click_button = driver.find_element(By.CLASS_NAME, "button-start")
click_button.click()
sleep(2)

# Вводим почту
input_login = driver.find_element(By.ID, "email")
input_login.send_keys("in6vq@airsworld.net")

# Вводим пароль
input_password = driver.find_element(By.ID, "passwordBasic")
input_password.send_keys("12345Qwerty")
sleep(3)

# Очищаем поле логина и пароля
# input_login.clear()
# input_password.clear()

# Нажимаем кнопку входа
submit_button = driver.find_element(By.CLASS_NAME, "btn-success")
submit_button.click()
sleep(5)

# Находим элемент с именем пользователя и выводим его текст
# user_name = driver.find_element(
#     By.CLASS_NAME, "profile-page__profile-name")
# print(user_name.text)

# Получаем имя пользователя
user_name = driver.find_element(By.CLASS_NAME, "profile-page__profile-name")
print(user_name.text)

# Находим поле поиска
search_input = driver.find_element(By.CSS_SELECTOR, "input.gf-custom-search__input")

# Получаем существующий атрибут placeholder
print(search_input.get_attribute("placeholder"))  # Что будем искать?

# Пробуем получить несуществующий атрибут
print(search_input.get_attribute("placeholder"))  # Вернет None

driver.quit()
