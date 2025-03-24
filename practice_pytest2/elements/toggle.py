from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import time


class Toggle:
    # 웹페이지 실행
    def __init__(self, driver):
        self.driver = driver

    # 전체 폴더 목록 확장
    def expand_all_toggle(self):
        expand_btn = self.driver.find_element(By.CLASS_NAME, 'rct-icon-expand-all')
        expand_btn.click()

    # 전체 폴더 목록 축소
    def collapse_all_toggle(self):
        collapse_btn = self.driver.find_element(By.CLASS_NAME, 'rct-icon-collapse-all')
        collapse_btn.click()

    # 특정 폴더 목록 확장
    def toggle_expand(self, content: str):   # conftest에서 생성한 driver를 매개변수로 받음
        for _ in range(6):
            toggles = self.driver.find_elements(By.CLASS_NAME, 'rct-collapse-btn')
            for toggle in toggles:
                try:
                    toggle_folder = toggle.find_element(By.XPATH, './/following-sibling::label/span[@class="rct-title"]')
                    child_toggles = toggle.find_elements(By.XPATH, './/button[contains(@class, "rct-collapse-btn")]')
                except StaleElementReferenceException as e:
                    continue
                if toggle_folder.text == content:
                    toggle.click()
                    time.sleep(5)
                    return toggle
                else:
                    for child_toggle in child_toggles:
                        child_toggle.click()
                        time.sleep(5)
                    break   # for문 탈출, 토글 목록 재탐색
            else:
                continue
        raise Exception(f'{content}폴더를 찾지 못했습니다.')

        # toggles = self.driver.find_elements(By.CLASS_NAME, 'rct-collapse-btn')

        # for toggle in toggles:
        #     child_folders = toggle.find_element(By.XPATH, './/child::span[@class="rct-title"]')
        #     child_toggles = toggle.find_element(By.XPATH, './/child::button[contains(@class, "rct-collapse-btn")]')
        #     for folder in child_folders:        
        #         if folder.text != content:
        #             child_toggles.click()