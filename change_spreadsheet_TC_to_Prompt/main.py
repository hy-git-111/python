from spreadsheet_reader import GoogleSheetReader
from prompt_generator import PromptGenerator
from file_writer import PromptSaver
import sys

# 터미널 인코딩 강제 설정
sys.stdout.reconfigure(encoding='utf-8')

# 설정
CREDENTIALS = "credentials.json"
SHEET_NAME = "Copy of 1차 프로젝트 오늘 뭐 먹지? - 4팀 Testcase_혜영테스트용"
OUTPUT_DIR = "prompts"

# 실행
reader = GoogleSheetReader(CREDENTIALS, SHEET_NAME)
saver = PromptSaver(OUTPUT_DIR)

worksheets = reader.get_worksheets()[1:]    # 첫 시트는 Summary라 제외함

for worksheet in worksheets:
    sheet_name = worksheet.title
    print(f"처리 중: {sheet_name}")

    # 2행을 헤더로 간주하여 데이터 읽기
    rows = worksheet.get_all_records(head=2)

    requirement_note = """
아래와 같은 디렉터리 구조로 테스트 자동화 프로그램을 만들고 싶습니다.
다음 테스트 케이스를 기반으로 각 파일에 들어갈 코드를 작성해주세요.

auto_test_project
├── main.py                # 실행 진입점
├── spreadsheet_reader.py  # 구글 시트 연동 클래스
├── prompt_generator.py    # 테스트 프롬프트 생성기
├── file_writer.py         # 파일로 저장
├── selenium_generator.py  # 프롬프트 → Selenium 테스트 코드 생성기
└── utils
    └── adf_parser.py      # ADF 파싱 유틸

main.py에서는 다음 작업을 수행합니다:
1. spreadsheet_reader로 모든 테스트 시트를 읽음
2. 각 시트를 루프 돌면서:
   - prompt_generator로 프롬프트 생성
   - file_writer로 저장
   - selenium_generator로 테스트 코드 생성

요구사항:
- Selenium Pytest 사용
- Chrome WebDriver 사용
- 각 step마다 주석 작성
- 가능한 경우 assert문으로 expected_result 체크
- 페이지 주소는 예시로 넣어도 괜찮음
- 파일 간 의존성은 명확하게 import
"""

    # 이 시트의 모든 프롬프트를 하나의 텍스트로 묶기
    all_prompts = []
    for row in rows:
        prompt = PromptGenerator(row).generate()
        all_prompts.append(prompt)

    full_prompt = requirement_note + "\n\n---\n\n".join(all_prompts)
    saver.save(full_prompt, sheet_name)  # 파일 이름: 시트 이름 기반