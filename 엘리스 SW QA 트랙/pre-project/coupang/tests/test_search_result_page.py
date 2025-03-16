# 프록시 우회하여 테스트 해야함..

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
# @pytest.mark.skip(reason="테스트 못함..")
class TestSearchResultPage:

# 검색결과 페이지에서 가격 필터 적용
    def test_filtering_by_range(self, driver: WebDriver):
        try:
            ITEM_XPATH = "//form//ul/li"
            SELECTED_FILTER_XPATH = "//dl/dd/a"
    
            search_result_page = SearchResultPage(driver)
            search_result_page.open()
            time.sleep(random_wait)

            # 검색결과 페이지 진입
            wait = ws(driver, 10)
            wait.until(EC.url_contains("coupang.com/np/search?"))

            item_name =parse.quote("노트북")
            assert item_name in driver.current_url
            time.sleep(random_wait)

            # 가격 필터 적용
            search_result_page.item_range_filtering(500000, 1000000)
            wait.until(EC.presence_of_element_located((By.XPATH, ITEM_XPATH)))
            selected_price_filter = driver.find_element(By.XPATH, SELECTED_FILTER_XPATH)

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

# 검색결과 페이지에서 브랜드, 평점 필터 적용

    #@pytest.mark.skip(reason="테스트 실행 대기중")
    def test_filtering_by_single(self, driver: WebDriver):
        try:
            ITEM_XPATH = "//form//ul/li"
            SELECTED_FILTER_XPATH = "//dl/dd/a"
            DELETE_FILTER_XPATH = "//dl/dd/a[1]/span"
            SELECTED_FILTER_LIST_XPATH = '//dt[contains(text(), "선택한 필터")]'
    
            search_result_page = SearchResultPage(driver)
            search_result_page.open()
            time.sleep(random_wait)

            # 검색결과 페이지 진입
            wait = ws(driver, 10)
            wait.until(EC.url_contains("coupang.com/np/search?"))

            item_name =parse.quote("노트북")
            assert item_name in driver.current_url
            time.sleep(random_wait)

            # 평점 필터 적용
            search_result_page.click_by_LINK_TEXT("4점 이상")
            wait.until(EC.presence_of_element_located((By.XPATH, ITEM_XPATH)))
            selected_rating_filter = driver.find_element(By.XPATH, SELECTED_FILTER_XPATH)
            
            assert "rating=4" in driver.current_url
            driver.save_screenshot(f"검색결과페이지_평점필터_적용_성공.png")
            logging.info("검색결과페이지 평점필터 적용 성공")
            assert "4점 이상" in selected_rating_filter.text
            driver.save_screenshot("검색결과페이지_선택한_필터에_평점_표시.png")
            logging.info("선택한 필터에 평점 표시 성공")
            time.sleep(random_wait)

            # 선택한 필터 삭제
            delete_filter = driver.find_element(By.XPATH, DELETE_FILTER_XPATH)
            delete_filter.click()
            wait.until(EC.url_contains("coupang.com/np/search?"))
        
            assert "coupang.com/np/search?" in driver.current_url
            selected_filter_list = driver.find_elements(By.XPATH, SELECTED_FILTER_LIST_XPATH)
            assert len(selected_filter_list) == 0
            driver.save_screenshot(f"검색결과페이지_선택한필터_삭제_성공.png")
            logging.info("검색결과페이지 선택한 필터 삭제 성공")
            time.sleep(random_wait)

            # 브랜드 필터 적용
            search_result_page.click_by_LINK_TEXT("삼성전자")
            wait.until(EC.presence_of_element_located((By.XPATH, ITEM_XPATH)))
            selected_brand_filter = driver.find_element(By.XPATH, SELECTED_FILTER_XPATH)

            assert "brand=258" in driver.current_url
            driver.save_screenshot(f"검색결과페이지_브랜드필터_적용_성공.png")
            logging.info("검색결과페이지 브랜드필터 적용 성공")
            assert "삼성전자" in selected_brand_filter.text
            driver.save_screenshot(f"선택한_필터에_브랜드_표시.png")
            logging.info("선택한 필터에 브랜드 표시 성공")
            time.sleep(random_wait)

        except NoSuchElementException as e:
            logging.exception(f"error:{e}")
            driver.save_screenshot('검색결과페이지_체크박스필터_적용_실패_NoSuchElementException.png')
            assert False

        except TimeoutException as e:
            logging.exception(f"error:{e}")
            driver.save_screenshot('검색결과페이지_체크박스필터_적용_실패_TimeoutException.png')
            assert False

    #@pytest.mark.skip(reason="테스트 실행 대기중")
    def product_detail(self, driver:WebDriver):
        try:
            MOST_POPULAR_ITEM = '//div/ul/li/a/dl[contains(@class, "no-1")]'

            search_result_page = SearchResultPage(driver)
            search_result_page.open()
            time.sleep(random_wait)

            # 검색결과 페이지 진입
            wait = ws(driver, 10)
            wait.until(EC.url_contains("coupang.com/np/search?"))

            item_name =parse.quote("노트북")
            assert item_name in driver.current_url
            time.sleep(random_wait)

            most_popular_item = driver.find_element(By.XPATH, MOST_POPULAR_ITEM)
            most_popular_item.click()
            assert "itemId" in driver.current_url
            driver.save_screenshot(f"검색결과페이지_제품상세_진입_성공.png")
            logging.info("검색결과페이지 제품상세 진입 성공")
            time.sleep(random_wait)

        except NoSuchElementException as e:
            logging.exception(f"error: {e}")
            driver.save_screenshot('검색결과페이지_제품상세_진입_실패_NoSuchElementException.png')

        except TimeoutException as e:
            logging.exception(f"error: {e}")
            driver.save_screenshot('검색결과페이지_제품상세_진입_실패_TimeoutException.png')