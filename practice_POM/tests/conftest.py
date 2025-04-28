from selenium import webdriver
import pytest

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    url = "https://mall.ejeju.net/main/index.do"
    driver.get(url)
    driver.maximize_window()

    yield driver

    driver.quit()

