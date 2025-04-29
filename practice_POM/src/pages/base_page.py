from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class BasePage():
    def __init__(self, driver):
        self.driver = driver

    # Explicit wite을 포함한 요소 탐색 함수
    def find_el(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
    
    # Explicit wite을 포함한 클릭 함수
    def click(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).click()

    # Explicit wite을 포함한 텍스트 입력 함수
    def input_text(self, locator, text):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        ).send_keys(text)

    # Explicit wite을 포함한 엔터 함수
    def send_enter_key(self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        ).send_keys(Keys.ENTER)