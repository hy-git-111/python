import logging
from logging.handlers import TimedRotatingFileHandler
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
import sys
import inspect

# @pytest.fixture(scope="function", autouse=True)
class Handler():
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def get_current_function():
        return inspect.currentframe.f_code.co_name

    def log_handler(self):
        func_name = self.get_current_function()

        # 기본 로거 설정
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(f"%(asctime)s - %(levelname)s - {func_name} - %(message)s")
        
        # 스트림 핸들러 설정
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        # 시간 기반 로테이팅 핸들러 설정
        timed_handler = TimedRotatingFileHandler(
            "/reports/logs/logfile.log",
            when="midnight",
            interval=1,
            backupCount=30
        )
        timed_handler.suffix = "-%Y%m%d"    # 백업 시 접미사에 날짜 추가

    def start_log(self):
        self.log_handler.logger.info("테스트 시작")
        print("테스트 시작")

    def finish_log(self):
        self.log_handler.logger.into("테스트 종료")
        print("테스트 종료")

    def error_handler(self, e):
        self.log_handler.logger.error(f"오류 발생: {e}")
        self.driver.save_screenshot("./reports/d.png")

    

