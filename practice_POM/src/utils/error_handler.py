import logging
from logging.handlers import TimedRotatingFileHandler
from selenium.webdriver.remote.webdriver import WebDriver
from utils.utils import get_current_file, get_current_function
import datetime
import os

class Handler():
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    def __init__(self, driver:WebDriver):
        self.driver = driver

        # 로그 설정을 위한 초기화
        self.test_page = get_current_file(2)
        self.test_case = get_current_function(2)
        self.logger = logging.getLogger(f"LoggerFor_{self.test_page}")

        # 디렉터리 생성
        log_dir = os.path.join(self.BASE_DIR, '..', 'reports', self.test_page, 'logs')
        screenshoot_dir = os.path.join(self.BASE_DIR, '..', 'reports', self.test_page, 'screenshoot')

        # 파일 생성
        today = datetime.date.today()
        now = datetime.datetime.now()
        date = now.strftime("%Y-%m-%d-%H-%M")
        
        os.makedirs(log_dir, exist_ok=True) # exist_ok=True : 이미 폴더가 있는 경우 pass
        os.makedirs(screenshoot_dir, exist_ok=True)

        self.log_file_path = os.path.join(log_dir, f'logfile_{today}.log')
        self.screenshoot_path = os.path.join(screenshoot_dir, f'{self.test_case}_{date}.png')
        
        self._log_setup()

    def _log_setup(self):
        # 기본 로거 설정
        self.logger.setLevel(logging.DEBUG)
        
        # 스트림 핸들러 설정
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)

        # 시간 기반 로테이팅 핸들러 설정
        time_handler = TimedRotatingFileHandler(
            self.log_file_path,
            when="midnight",
            interval=1,
            backupCount=30,
            encoding="utf-8"
        )

        # 포메터 추가       
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        stream_handler.setFormatter(formatter)
        time_handler.setFormatter(formatter)

        # 핸들러 적용
        if not self.logger.handlers:
            self.logger.addHandler(stream_handler)
            self.logger.addHandler(time_handler)

    # 로그 핸들러 - 로그 메세지 설정
    def log_handler(self, message, level = "info"):
        func_name = get_current_function(3)

        full_message = f"{func_name} - {message}"
        if level == "info":
            self.logger.info(full_message)
        elif level == "error":
            self.logger.error(full_message)

    # 테스트 시작 로그 함수
    def start_log(self):
        print("테스트 시작")
        self.log_handler(message="테스트 시작")

    # 테스트 종료 로그 함수
    def finish_log(self):
        print("테스트 종료")
        self.log_handler(message="테스트 종료")

    # 오류 발생 로그, 스크린샷 관리 함수
    def error_handler(self, e):
        error_type = type(e).__name__
        error_message = f"{error_type}\n{e}"

        print(f"오류 발생: {error_type}")
        self.log_handler(message=f"{error_message}", level="error")
        self.driver.save_screenshot(self.screenshoot_path)