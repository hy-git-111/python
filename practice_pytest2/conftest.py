import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')

    driver = webdriver.Chrome()

    url = "https://demoqa.com/checkbox"
    driver.get(url)
    driver.maximize_window()

    yield driver

    driver.quit()