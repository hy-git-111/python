from spreadsheet_reader import GoogleSheetReader
from prompt_generator import PromptGenerator
from file_manager import FeileManager
from test_code_generator import generate_test_code
import sys

# 터미널 인코딩 강제 설정
sys.stdout.reconfigure(encoding='utf-8')

# 설정
CREDENTIALS = "credentials.json"
SHEET_NAME = "Copy of 1차 프로젝트 오늘 뭐 먹지? - 4팀 Testcase_혜영테스트용"
OUTPUT_DIR = "prompts"

# 실행
reader = GoogleSheetReader(CREDENTIALS, SHEET_NAME)
file_manager = FeileManager(OUTPUT_DIR)

worksheets = reader.get_worksheets()[1:]    # 첫 시트는 Summary라 제외함

for worksheet in worksheets:
    sheet_name = worksheet.title
    print(f"처리 중: {sheet_name}")

    # 2행을 헤더로 간주하여 데이터 읽기
    rows = worksheet.get_all_records(head=2)

    # 이 시트의 모든 프롬프트를 하나의 텍스트로 묶기
    all_prompts = []
    for row in rows:
        prompt_json = PromptGenerator(row).generate()
        all_prompts.append(prompt_json)

    file_manager.save_prompt_json(all_prompts, sheet_name)  # 파일 이름: 시트 이름 기반

# 테스트코드 생성
prompt_text = file_manager.read_prompt_json(sheet_name)
response = generate_test_code(all_prompts)
file_manager.save_test_code(response, sheet_name)