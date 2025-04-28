from src.utils.error_handler import Handler
from src.pages.main_page import MainPage
from selenium.webdriver.remote.webdriver import WebDriver

class TestMainPage():
    def test_header_search(self, driver):
        self.main_page = MainPage(driver)
        self.handler = Handler(driver)

        self.handler.start_log()

        try:
            header_el = self.main_page.header_search()

            assert header_el.text == "검색결과"
            assert "search.do?" in self.driver.current_url
        except:
            self.handler.error_handler()

        finally:
            self.handler.finish_log()