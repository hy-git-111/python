from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from urllib import parse
import logging
import random
import pytest
import time


random_wait = random.randrange(1, 6)

@pytest.mark.usefixtures("driver")
class TestMainPage:
    # 최근 본 상품 페이지 작성해야함

    @pytest.mark.skip(reason="아직 테스트케이스 발동 안함")
    def test_open_main_page(self, driver: WebDriver):
        try:
            main_page = MainPage(driver)
            main_page.open()

            time.sleep(2)

            wait = ws(driver, 10)
            wait.until(EC.url_contains("coupang.com"))

            # 쿠팡 페이지에 진입했는지 확인
            assert "coupang.com" in driver.current_url
            time.sleep(2)






        except NoSuchElementException as e:
            logging.exception(f"error:{e}")
            assert False

# 메인페이지에서 로그인, 회원가입 진입
    @pytest.mark.skip(reason="아직 테스트케이스 발동 안함, Pass")
    def test_click_link_text(self, driver: WebDriver):
        try:
            main_page = MainPage(driver)
            main_page.open()
            time.sleep(2)

            wait = ws(driver, 10)
            wait.until(EC.url_contains("coupang.com"))
            # 쿠팡 페이지에 진입했는지 확인
            assert "coupang.com" in driver.current_url

            main_page.click_by_LINK_TEXT('로그인')

            assert "login" in driver.current_url
            driver.save_screenshot('메인페이지_로그인페이지_진입성공.png')
            time.sleep(2)

            driver.back()
            wait.until(EC.url_contains("coupang.com"))
            assert "coupang.com" in driver.current_url
            time.sleep(2)

            main_page.click_by_LINK_TEXT('회원가입')
            assert "memberJoinFrm" in driver.current_url
            driver.save_screenshot('메인페이지_회원가입페이지_진입성공.png')
            
        except NoSuchElementException as e:
            logging.exception(f"error:{e}")
            driver.save_screenshot('메인페이지_링크텍스트_실패_NoSuchElementException.png')
            assert False

        except TimeoutException as e:
            logging.exception(f"error:{e}")
            driver.save_screenshot('메인페이지_검색_실패_TimeoutException.png')
            assert False

# 메인페이지에서 장바구니, 마이쿠팡페이지 진입
    @pytest.mark.skip(reason="아직 테스트케이스 발동 안함, Pass")
    def test_click_img_name(self, driver: WebDriver):
        try:
            main_page = MainPage(driver)
            main_page.open()
            time.sleep(2)

            wait = ws(driver, 10)
            wait.until(EC.url_contains("coupang.com"))

            # 쿠팡 페이지에 진입했는지 확인
            assert "coupang.com" in driver.current_url
            time.sleep(2)

            main_page.click_by_IMG_NAME('cart') 
            
            # 장바구니 페이지 진입
            assert "cartView" in driver.current_url 
            logging.info("장바구니페이지 진입")
            driver.save_screenshot('메인페이지_장바구니페이지_진입성공.png')
            time.sleep(2)

            driver.back()
            wait.until(EC.url_contains("coupang.com"))
            assert "coupang.com" in driver.current_url
            time.sleep(2)

            # 마이쿠팡페이지 진입
            main_page.click_by_IMG_NAME('person')
            assert "login" in driver.current_url
            logging.info("마이쿠팡페이지 진입")
            driver.save_screenshot('메인페이지_마이쿠팡페이지_진입성공.png')

        except NoSuchElementException as e:
            logging.exception(f"error:{e}")
            driver.save_screenshot('메인페이지_이미지찾기_실패_NoSuchElementException.png')
            assert False

        except TimeoutException as e:
            logging.exception(f"error:{e}")
            driver.save_screenshot('메인페이지_이미지찾기_실패_TimeoutException.png')
            assert False

# 검색창에 "노트북" 입력하여 검색
    @pytest.mark.skip(reason="아직 테스트케이스 발동 안함")
    def test_search_items(self, driver: WebDriver):
        try:
            ITEM_XPATH = "//form//ul/li"
    
            main_page = MainPage(driver)
            main_page.open()
            time.sleep(random_wait)

            # 쿠팡 페이지 진입
            wait = ws(driver, 10)
            wait.until(EC.url_contains("coupang.com"))

            assert "coupang.com" in driver.current_url
            time.sleep(random_wait)

            # '노트북' 검색
            main_page.search_single_item('노트북')
            # wait = ws(driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, ITEM_XPATH)))
            items = driver.find_elements(By.XPATH, ITEM_XPATH)  # list
            item_name = parse.quote('노트북')   # str, " %EB%85%B8%ED%8A%B8%EB%B6%81"

            assert len(items) > 0
            assert item_name in driver.current_url
            driver.save_screenshot('메인페이지_검색_성공.png')
            logging.info("메인페이지 검색 성공")
            time.sleep(random_wait)

        except NoSuchElementException as e:
            logging.exception(f"error:{e}")
            driver.save_screenshot('메인페이지_검색_실패_NoSuchElementException.png')
            assert False

        except TimeoutException as e:
            logging.exception(f"error:{e}")
            driver.save_screenshot('메인페이지_검색_실패_TimeoutException.png')
            assert False