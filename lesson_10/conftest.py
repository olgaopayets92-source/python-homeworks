"""
Модуль с фикстурами pytest для WebDriver.
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def chrome_driver() -> webdriver.Chrome:
    """
    Фикстура для создания драйвера Google Chrome.

    :yield: экземпляр WebDriver Chrome.
    """
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def firefox_driver() -> webdriver.Firefox:
    """
    Фикстура для создания драйвера Mozilla Firefox.

    :yield: экземпляр WebDriver Firefox.
    """
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()
