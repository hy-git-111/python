# 봇 방지때문에 로그인이 안됨
# 로그인 전후 쿠키 출력해서 달라진점 확인해야함
# 로그인 문제 해결되면 최근 본 목록 코드 작성해야함

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from urllib import parse
import logging
import random
import pytest
import time


random_wait = random.randrange(1, 6)

@pytest.mark.usefixtures("driver")
class TestLoginPage:

    #@pytest.mark.skip(reason="아직 테스트케이스 발동 안함")
    def test_open_login_page(self, driver: WebDriver):
        try:

            MENU_LIST_XPATH = "//menu/li/a"

            login_page = LoginPage(driver)
            login_page.open()

            login_page.click_by_LINK_TEXT('로그인')
            time.sleep(6)

            wait = ws(driver, 10)
            wait.until(EC.url_contains("login.coupang.com"))


            # 쿠팡 페이지에 진입했는지 확인
            assert "login.coupang.com" in driver.current_url

            cookie_value = driver.get_cookies()
            for cookie in cookie_value:
                print(cookie)

            # 사용자 데이터 입력
            login_page.input_user_data()
            menu_list = driver.find_elements(By.XPATH, MENU_LIST_XPATH)
            user_name = driver.find_elements(By.LINK_TEXT)

            wait.until(EC.presence_of_element_located(menu_list))

            cookie_value = driver.get_cookies()
            time.sleep(60)
            for cookie in cookie_value:
                print(cookie)

            assert "coupang.com"in driver.current_url
            assert "님" in user_name
            driver.save_screenshot("로그인페이지_로그인_성공")
            logging.info("로그인페이지 로그인 성공")
            time.sleep(random_wait)

        except NoSuchElementException as e:
            logging.exception(f"error:{e}")
            driver.save_screenshot ("로그인페이지_로그인_실패_NoSuchElementException.png")
            assert False

        except TimeoutException as e:
            logging.exception(f"error: {e}")
            driver.save_screenshot ("로그인페이지_로그인_실패_TimeoutException.png")