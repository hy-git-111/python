from src.pages.base_page import BasePage
from src.pages import main_page_locators, search_page_locator

class MainPage():
    def __init__(self, driver):
        self.base_page = BasePage(driver)
        self.main_page_locators = main_page_locators
        self.search_page_locators = search_page_locator

    # 검색버튼 클릭 함수
    def click_search_btn(self, locator):
        self.base_page.click(locator)

    # 키워드 입력 함수
    def input_keyword(self, locator, keyword):
        self.base_page.input_text(locator, keyword)

    # 헤더 검색 함수
    def header_search(self, keyword):
        self.click_search_btn(self.main_page_locators.SEARCH_BTN)
        self.input_keyword(self.main_page_locators.SEARCH_INPUT, keyword)
        self.base_page.send_enter_key(self.main_page_locators.SEARCH_INPUT)
        
        return self.base_page.find_el(self.search_page_locators.TITLE)