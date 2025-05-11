from spreadsheet_reader import GoogleSheetReader
from prompt_generator import PromptGenerator
from file_manager import FeileManager
from test_code_generator import TestCodeGenerator
from initial_prompt import ui_requirement
import sys

# 터미널 인코딩 강제 설정
sys.stdout.reconfigure(encoding='utf-8')

# 설정
CREDENTIALS = "credentials.json"
SHEET_NAME = "Copy of 1차 프로젝트 오늘 뭐 먹지? - 4팀 Testcase_혜영테스트용"
OUTPUT_DIR = "prompts"
MAX_REQ_TOKENS  = 8_000      # 요청당 최대 출력 토큰
MAX_TOTAL_TOKENS = 180_000   # 전체 파일 한계

reader = GoogleSheetReader(CREDENTIALS, SHEET_NAME)
file_manager = FeileManager(OUTPUT_DIR)

worksheets = reader.get_worksheets()[1:]    # 첫 시트는 Summary라 제외함

# 구글시트 데이터를 프롬프트로 저장하기
for worksheet in worksheets:
    sheet_name = worksheet.title
    print(f"처리 중: {sheet_name}")

    # 구글시트에서 데이터 가져오기(2행을 헤더로 간주)
    rows = worksheet.get_all_records(head=2)

    # 데이터를 프롬프트이 시트의 모든 프롬프트를 하나의 텍스트로 묶기
    all_prompts = []
    for row in rows:
        prompt_json = PromptGenerator(row).generate()
        all_prompts.append(prompt_json)

    file_manager.save_prompt_json(all_prompts, sheet_name)  # 파일 이름: 시트 이름 기반
prompt_text = file_manager.read_prompt_json(sheet_name)

# 테스트 코드 생성
generator = TestCodeGenerator(
    model_name="claude-3-7-sonnet-20250219",
    temperature=0.3,
    system_prompt=ui_requirement,
    max_tokens_per_request=MAX_REQ_TOKENS
)

generated_code = generator.generate_code_with_token_check(
    all_prompts,
    max_total_tokens=MAX_TOTAL_TOKENS
)

# 테스트 코드 저장
file_manager.save_test_code(generated_code, sheet_name)