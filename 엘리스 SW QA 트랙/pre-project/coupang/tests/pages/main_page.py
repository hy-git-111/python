from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class MainPage:
    url = "https://www.coupang.com/"
    SEARCH_INPUT_ID = "headerSearchKeyword"
    SEARCH_BUTTON_ID = "headerSearchBtn"

    # 객체 인스턴스화를 위한 세팅, 파이테스트의 'driver'를 받아 driver 객체에 넣는다.
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 메인 페이지 열기
    def open(self):
        self.driver.get(self.url)

    # 검색창 찾기
    def search_single_item(self, item_name: str):
        search_input_box = self.driver.find_element(By.ID, self.SEARCH_INPUT_ID)
        # return search_input_box   # 검증 확인용
        search_input_box.send_keys(item_name)
        search_input_box.send_keys(Keys.ENTER) 

    def click_by_LINK_TEXT(self, link_text: str):
        login_button = self.driver.find_element(By.LINK_TEXT, link_text)
        login_button.click()

    def click_by_IMG_NAME(self, img_name: str):
        img_elements = self.driver.find_elements(By.TAG_NAME, "img")
        for img in img_elements:
            src = img.get_attribute("src")
            if src is None:
                continue

            if img_name in src:
                img.click()
                return
            
        raise ValueError(f"{img_name}의 이미지를 찾을 수 없습니다.")