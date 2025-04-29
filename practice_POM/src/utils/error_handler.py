import logging
from logging.handlers import TimedRotatingFileHandler
from selenium.webdriver.remote.webdriver import WebDriver
import inspect
import sys

class Handler():
    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.logger = logging.getLogger()

    @staticmethod
    def get_current_function():
        return sys._getframe(3).f_code.co_name

    def log_handler(self, message):
        func_name = self.get_current_function()
        print(func_name)

        # 기본 로거 설정
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(f"%(asctime)s - %(levelname)s - %{func_name}s - %{message}s")
        
        # 스트림 핸들러 설정
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(formatter)
        self.logger.addHandler(stream_handler)

        # 시간 기반 로테이팅 핸들러 설정
        timed_handler = TimedRotatingFileHandler(
            "/reports/logs/logfile.log",
            when="midnight",
            interval=1,
            backupCount=30
        )
        timed_handler.suffix = "-%Y%m%d"    # 백업 시 접미사에 날짜 추가

    def start_log(self):
        print("테스트 시작")
        self.log_handler(message="테스트 시작")

    def finish_log(self):
        print("테스트 종료")
        self.log_handler(message="테스트 시작")

    def error_handler(self, e):
        print(f"오류 발생: {e}")
        self.log_handler(message=f"오류 발생: {e}")
        self.driver.save_screenshot("./reports/d.png")

    

