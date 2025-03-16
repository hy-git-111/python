from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class ProdDetailPage:
    url = "https://www.coupang.com/vp/products/7295558262?itemId=20340965740&vendorItemId=86330525952&pickType=COU_PICK&q=%EB%A1%9C%EC%A7%80%ED%85%8D+%EB%B2%84%ED%8B%B0%EC%BB%AC+%EB%A7%88%EC%9A%B0%EC%8A%A4+lift&itemsCount=36&searchId=340fdcee36510541&rank=0&searchRank=0&isAddedCart="
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
    
    def option_change(self, optin_list, choice):
        option_container = self.driver.find_element(By.XPATH, optin_list)
        option_container.click()

        choice_option = self.driver.find_element(By.XPATH, choice)
        choice_option.click()

    def add_cart(self):
        ADD_CART_CLASS_NAME = "prod-cart-btn"
        add_cart_btn = self.driver.find_element(By.CLASS_NAME, ADD_CART_CLASS_NAME)
        add_cart_btn.click()
