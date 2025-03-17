from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import user_data

import clipboard
import random
import time

class LoginPage:
    url = "https://www.coupang.com/"
    #url = "https://login.coupang.com/login/login.pang?rtnUrl=https%3A%2F%2Fwww.coupang.com%2Fnp%2Fpost%2Flogin%3Fr%3Dhttps%253A%252F%252Fwww.coupang.com%252F"
    # SEARCH_BUTTON_ID = "headerSearchBtn"
    random_wait = random.randrange(1,11)

    # 객체 인스턴스화를 위한 세팅, 파이테스트의 'driver'를 받아 driver 객체에 넣는다.
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 메인 페이지 열기
    def open(self):
        self.driver.get(self.url)

    # def send_keys_slowly(self, string, element):
    #     letter_list = list(string)

    #     for letter in letter_list:
    #         element.send_keys(letter)
    #         time.sleep(1)

    def click_by_LINK_TEXT(self, link_text: str):
        login_button = self.driver.find_element(By.LINK_TEXT, link_text)
        login_button.click()
        
    # 로그인
    def input_user_data(self):
        EMAIL_ID = "login-email-input"
        PASSWORD_ID = "login-password-input"
        LOGIN_BTN_CLASS_NAME = "_loginSubmitButton"

        clipboard.copy(user_data.EMAIL)
        email_input_box = self.driver.find_element(By.ID, EMAIL_ID)
        email_input_box.click()
        clipboard.paste()
        time.sleep(self.random_wait)

        clipboard.copy(user_data.PASSWORD)
        password_input_box = self.driver.find_element(By.ID, PASSWORD_ID)
        password_input_box.click()
        clipboard.paste()
        time.sleep(3)

        login_btn = self.driver.find_element(By.CLASS_NAME, LOGIN_BTN_CLASS_NAME)
        login_btn.send_keys(Keys.ENTER)