import sys, os

# 현재 함수명 반환 함수
@staticmethod
def get_current_function(n):
    return sys._getframe(n).f_code.co_name

# 현재 파일명 반환 함수
@staticmethod
def get_current_file(n):
    file_path = sys._getframe(n).f_code.co_filename # 전체 경로 반환
    file_name = os.path.basename(file_path) # 파일명 반환
    return os.path.splitext(file_name)[0] # splittext() return ('test_main_page', 'py')