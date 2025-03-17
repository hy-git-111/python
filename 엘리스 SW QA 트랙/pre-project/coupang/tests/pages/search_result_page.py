from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class SearchResultPage:
    url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
    PRICERANGE_INPUT_CLASS = "param-pricerange"

    # 객체 인스턴스화를 위한 세팅, 파이테스트의 'driver'를 받아 driver 객체에 넣는다.
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self):
        self.driver.get(self.url)

    def click_by_LINK_TEXT(self, link_text: str):
        filter_button = self.driver.find_element(By.LINK_TEXT, link_text)
        filter_button.click()

    def item_range_filtering(self, min_price, max_price: int):
        input_elements = self.driver.find_elements(By.CLASS_NAME, self.PRICERANGE_INPUT_CLASS)
        for element in input_elements:
            title = element.get_attribute("title")
            if title == None:
                continue

            if title == "minPrice":
                element.send_keys(min_price)
                continue
            
            if title == "maxPrice":
                element.send_keys(max_price)
                element.send_keys(Keys.ENTER)
                return
                        
        raise ValueError

