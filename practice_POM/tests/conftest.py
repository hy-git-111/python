from selenium import webdriver
import pytest

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    url = "https://mall.ejeju.net/main/index.do"

    yield driver.get(url)

    driver.quit()

