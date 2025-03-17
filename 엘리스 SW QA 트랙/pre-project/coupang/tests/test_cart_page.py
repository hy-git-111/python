from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from pages.search_result_page import SearchResultPage
from urllib import parse
import logging
import random
import pytest
import time


random_wait = random.randrange(1, 6)

@pytest.mark.usefixtures("driver")
class TestProductDetailPage:

# 검색결과 페이지에서 가격 필터 적용
    def test_filtering_by_range(self, driver: WebDriver):
        try:
            
            

            assert "minPrice=50000"in driver.current_url and "maxPrice=150000" in driver.current_url
            driver.save_screenshot("검색결과페이지_가격필터_적용_성공.png")
            logging.info("검색결과페이지 가격 필터 적용 성공")
            assert "500,000" in selected_price_filter.text
            driver.save_screenshot("선택한_필터에_최소가격_표시.png")
            logging.info("선택한 필터에 최소가격 표시 성공")
            assert "1,000,000" in selected_price_filter.text
            driver.save_screenshot("선택한_필터에_최대가격_표시.png")
            logging.info("선택한 필터에 최대가격 표시 성공")
            time.sleep(random_wait)

        except NoSuchElementException as e:
            logging.exception(f"error:{e}")
            driver.save_screenshot('검색결과페이지_범위필터_적용_실패_NoSuchElementException.png')
            assert False

        except TimeoutException as e:
            logging.exception(f"error:{e}")
            driver.save_screenshot('검색결과페이지_범위필터_적용_실패_TimeoutException.png')
            assert False