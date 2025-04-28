from src.pages.base_page import BasePage
from utils import main_page_locators, search_page_locator
from src.utils.random_utils import RandomUtils

class MainPage():
    def __init__(self, driver):
        self.base_page = BasePage(driver)
        self.random_utils = RandomUtils()

    def click_search_btn(self, locator):
        self.base_page.click(locator)

    def input_keyword(self, locator, text):
        self.base_page.input_text(locator, text)


        self.base_page.send_enter_key(main_page_locators.SEARCH_INPUT)
        
        return self.base_page.find_el(search_page_locator.TITLE)