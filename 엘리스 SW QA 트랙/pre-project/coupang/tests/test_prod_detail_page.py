from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from pages.prod_detail_page import ProdDetailPage
from urllib import parse
import logging
import random
import pytest
import time


random_wait = random.randrange(1, 6)

@pytest.mark.usefixtures("driver")
class TestProdDetailPage:

# 상품 옵션 변경
    def test_option_change(self, driver: WebDriver):
        try:
            MODEL_CONTAINER_XPATH = '//div[2]/div/div/button[contains(@class, "prod-option__selected") and contains(@class, "multiple")]'
            MODEL_CHOICE_XPATH = '//li[@data-attribute-id="3409256742"]'
            COLOR_CONTAINER_XPATH = '//div[1]/div/div/button[contains(@class, "prod-option__selected") and contains(@class, "multiple")]'
            COLOR_CHOICE_XPATH = '//li[@data-attribute-id="3116791567"]'

            prod_detail_page = ProdDetailPage(driver)
            prod_detail_page.open()
            time.sleep(random_wait)

            wait = ws(driver, 10)
            wait.until(EC.url_contains("vendorItemId"))

            current_quantity = prod_detail_page.quantity_plus()

            assert current_quantity > 1
            driver.save_screenshot("제품상세페이지_수량_증가_성공")
            logging.info("제품상세페이지 수량 증가 성공")
            time.sleep(random_wait)

            current_quantity = prod_detail_page.quantity_plus()

            assert current_quantity == 1
            driver.save_screenshot("제품상세페이지_수량_감소성공")
            logging.info("제품상세페이지 수량 감소 성공")
            time.sleep(random_wait)

            prod_detail_page.option_change(MODEL_CONTAINER_XPATH, MODEL_CHOICE_XPATH)

            assert "vendorItemId=91960139630" in driver.current_url
            driver.save_screenshot("제품상세페이지_모델명_변경_성공.png")
            logging.info("제품상세페이지 모델명 변경 성공")
            time.sleep(random_wait)

            prod_detail_page.option_change(COLOR_CONTAINER_XPATH, COLOR_CHOICE_XPATH)

            assert "vendorItemId=91960139738" in driver.current_url
            driver.save_screenshot("제품상세페이지_색상_변경_성공.png")
            logging.info("제품상세페이지 색상 변경 성공")
            time.sleep(random_wait)

        except NoSuchElementException as e:
            logging.exception(f"error:{e}")
            driver.save_screenshot('검색결과페이지_범위필터_적용_실패_NoSuchElementException.png')
            assert False

        except TimeoutException as e:
            logging.exception(f"error:{e}")
            driver.save_screenshot('검색결과페이지_범위필터_적용_실패_TimeoutException.png')
            assert False

# 장바구니에 담기
    #@pytest.mark.skip(reason="아직 작성 완료 안됨")
    def test_add_cart(self, driver: WebDriver):
        try:
            prod_detail_page = ProdDetailPage(driver)
            prod_detail_page.open()
            time.sleep(random_wait)

            wait = ws(driver, 10)
            wait.until(EC.url_contains("vendorItemId"))

            prod_detail_page.add_cart()
            go_to_carts = driver.find_elements(By.LINK_TEXT, "장바구니 바로가기 >")

            assert len(go_to_carts) != 0
            driver.save_screenshot("제품상세페이지_장바구니_담기_성공.png")
            logging.info("제품상세페이지 장바구니 담기 성공")
            time.sleep(random_wait)

        except NoSuchElementException as e:
            logging.exception(f"error:{e}")
            driver.save_screenshot('제품상세페이지_장바구니_담기_실패_NoSuchElementException.png')
            assert False

        except TimeoutException as e:
            logging.exception(f"error:{e}")
            driver.save_screenshot('제품상세페이지_장바구니_담기_실패_TimeoutException.png')
            assert False
        

