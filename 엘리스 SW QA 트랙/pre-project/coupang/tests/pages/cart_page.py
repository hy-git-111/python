from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class MainPage:
    url = "https://www.coupang.com/vp/products/8529745461?itemId=24695444272&vendorItemId=86939243799&q=%EB%85%B8%ED%8A%B8%EB%B6%81&itemsCount=36&searchId=dbd6237f6026569&rank=1&searchRank=1&isAddedCart="
    SEARCH_INPUT_ID = "headerSearchKeyword"
    SEARCH_BUTTON_ID = "headerSearchBtn"

    # 객체 인스턴스화를 위한 세팅, 파이테스트의 'driver'를 받아 driver 객체에 넣는다.
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 상품 상세 페이지 열기
    def open(self):
        self.driver.get(self.url)

    # 수량 증가
    def quantity_plus(self):
        quantity_input = self.driver.find_element(By.CLASS_NAME, "prod-quantity__input")
        current_quantity = quantity_input.get_attribute("value")
        plus_btn = self.driver.find_element(By.CLASS_NAME, "prod-quantity__plus")

        if plus_btn.get_attribute("disabled") == None:
            return f"최대 구매 수량: {current_quantity}"
        
        plus_btn.click()
        return current_quantity
    
    # 수량 감소
    def quantity_minus(self):
        quantity_input = self.driver.find_element(By.CLASS_NAME, "prod-quantity__input")
        current_quantity = quantity_input.get_attribute("value")
        minus_btn = self.driver.find_element(By.CLASS_NAME, "prod-quantity__minus")

        if minus_btn.get_attribute("disabled") == None:
            return f"최소 구매 수량: {current_quantity}"
        
        minus_btn.click()
        return current_quantity
