from ..pages.base_page import BasePage
from utils import main_page_locators, search_page_locator
from src.utils.random_utils import RandomUtils

class MainPage():
    def __init__(self):
        self.base_page = BasePage()
        self.random_utils = RandomUtils()

    def click_search_btn(self, locator):
        self.base_page.click(locator)

    def input_keyword(self, locator, text):
        self.base_page.input_text(locator, text)

    def header_search(self):
        self.click_search_btn(main_page_locators.SEARCH_BTN)
        self.input_keyword(main_page_locators.SEARCH_INPUT, self.random_utils.generate_random_product())
        self.base_page.send_enter_key(main_page_locators.SEARCH_INPUT)
        
        return self.base_page.find_el(search_page_locator.TITLE)