from selenium import webdriver

driver = webdriver.Chrome()  # Selenium Manager сам загрузит драйвер
driver.get("https://google.com")
print(driver.title)
driver.quit()