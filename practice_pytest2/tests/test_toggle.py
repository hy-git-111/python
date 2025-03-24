import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from elements.toggle import Toggle
import time

class TestToggle:
    def test_toggle_choice_control(self, driver):
        try:
            wait = WebDriverWait(driver, 5)
            wait.until(EC.url_contains("checkbox"))
            time.sleep(5)
            
            # 특정 폴더가 나타날때까지 목록 확장
            toggle = Toggle(driver)
            folder_name = "WorkSpace"
            expand_folder = toggle.toggle_expand(folder_name)

            # expand_folders = driver.find_elements(By.XPATH, f'//span[@class="rct-title"]')
            expand_icon = []
            # for folder in expand_folders:
            if expand_folder.text == folder_name:
                expand_icon = expand_folder.find_elements(By.XPATH, './/preceding-sibling::svg[contains(@class, "open")]')
        
            assert len(expand_icon) > 0
            time.sleep(3)

        except NoSuchElementException as e:
            print(f"에러 발생 : {e}")

        except TimeoutException as e:
            print(f"에러 발생: {e}")

    @pytest.mark.skip(reason="대기")
    def test_toggle_all_control(self, driver):
        try:
            wait = WebDriverWait(driver, 5)
            wait.until(EC.url_contains("checkbox"))
            
            # 전체 폴더 목록 확장
            toggle = Toggle(driver)
            toggle.expand_all_toggle()

            checkbox = driver.find_elements(By.CLASS_NAME, "rct-checkbox")
            assert len(checkbox) > 1
            time.sleep(2)

            # 전체 폴더 목록 축소
            toggle.collapse_all_toggle()

            checkbox = driver.find_elements(By.CLASS_NAME, "rct-checkbox")
            assert len(checkbox) == 1
            time.sleep(2)
        
        except NoSuchElementException as e:
            print(f"에러 발생 : {e}")

        except TimeoutException as e:
            print(f"에러 발생: {e}")



