# from selenium import webdriver
# from selenium.webdriver.common.by import By


# def test_image_loading():
#     driver = webdriver.Chrome()
#     driver.implicitly_wait(30)
#     driver.get(
#         "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

#     image1 = driver.find_element(By.ID, "compass")
#     image2 = driver.find_element(By.ID, "calendar")
#     image3 = driver.find_element(By.ID, "award")
#     image4 = driver.find_element(By.ID, "landscape")

#     images = [image1, image2, image3, image4]

#     expected_files = [
#         "compass.png",
#         "calendar.png",
#         "award.png",
#         "landscape.png"
#     ]

#     for i, img in enumerate(images):
#         src = img.get_attribute("src")
#         assert expected_files[i] in src
#         assert img.is_displayed()

#     driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_image_loading():
    driver = webdriver.Chrome()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Ждем завершения загрузки
    WebDriverWait(driver, 30).until(
        EC.text_to_be_present_in_element((By.ID, "text"), "Done!")
    )

    # Находим все изображения
    images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")

    # Проверяем изображения
    assert len(images) == 4

    expected_files = [
        "compass.png",
        "calendar.png",
        "award.png",
        "landscape.png"
    ]

    for i, img in enumerate(images):
        src = img.get_attribute("src")
        assert expected_files[i] in src
        assert img.is_displayed()

    driver.quit()
