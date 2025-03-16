from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest
import logging
import os

# ✅ 기존 핸들러 제거 (중복 설정 방지)
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# 로그 파일 저장 위치 설정 (conftest.py가 있는 폴더 기준)
# log_filename = f"{date.today().strftime('%Y%m%d')}_coupang_test_result.log"
log_filename = os.path.join(os.path.dirname(__file__), "coupang_test_result.log")

# 로그 설정
logging.basicConfig(
    filename=log_filename,
    encoding="utf-8",
    errors="replace",  # 인코딩 문제 방지
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logging.info("pytest 실행 시 로그 설정 완료")

@pytest.fixture(scope="function")

def driver():
    # 크롬 옵션 설정
    chrome_options = Options()  # 쿠팡에서 자동화를 막아서 옵션 수정 필요
    # chrome_options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" # ✅ GPT 추가

    # proxy : 크롤링 중 ip가 차단되었을 때 vpn을 사용해서 ip 우회하는 것
    # 1) User-Agent 변경
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) Firefox/91.0")    # 사용자 접근 환경 강제 입력

    # 2) SSL 인증서 에러 무시
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--ignore-ssl-errors")

    # 4) Selenium이 automation된 브라우저임을 숨기는 몇 가지 설정 (js가 인식하지 못하도록 함)
    #    - (disable-blink-features=AutomationControlled) 제거
    #    - excludeSwitches, useAutomationExtension
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    # 혹은 다음 방식으로 Blink 특징을 비활성화할 수도 있으나
    # "AutomationControlled" 자체가 표기되지 않도록 한다.
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    # 5) 디버그 로깅 줄이기 (선택)
    # chrome_options.add_argument("--log-level=3") 

    # 6) Sandbox나 DevShm 사이즈 문제 우회 (리눅스 환경에서 발생 가능)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # 드라이버 객체 생성
    driver = webdriver.Chrome(service=Service(), options=chrome_options)   
    driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"Referer": "https://www.coupang.com/"}})
    
    #  대기시간 설정
    driver.implicitly_wait(5)
    driver.maximize_window()

    yield driver 

    # 테스트가 끝나면 드라이버 종료
    driver.quit()
