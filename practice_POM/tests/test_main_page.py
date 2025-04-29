from src.utils.error_handler import Handler
from src.pages.main_page import MainPage
from src.utils.random_utils import RandomUtils
from urllib.parse import quote

class TestMainPage():
    def test_header_search(self, driver):
        self.main_page = MainPage(driver)
        self.handler = Handler(driver)
        self.random_utils = RandomUtils()

        self.handler.start_log()

        try:
            keyword = self.random_utils.generate_random_product()
            header_el = self.main_page.header_search(keyword)

            assert header_el.text == "검색결과"
            assert quote(keyword) in driver.current_url

        except Exception as e:
            self.handler.error_handler(e)

        finally:
            self.handler.finish_log()