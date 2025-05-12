from spreadsheet_reader import GoogleSheetReader
from prompt_generator import PromptGenerator
from file_manager import FileManager
from test_code_generator import TestCodeGenerator
from initial_prompt import ui_requirement
import sys, time
import concurrent.futures  # 추가: 병렬 처리를 위한 라이브러리 임포트

# 터미널 인코딩 강제 설정
sys.stdout.reconfigure(encoding='utf-8')

# 설정
CREDENTIALS = "credentials.json"
SHEET_NAME = "Copy of 엘리스_2차_3조_팀프로젝트_사본"
OUTPUT_DIR = "prompts"
MAX_REQ_TOKENS  = 8_000      # 요청당 최대 출력 토큰
MAX_TOTAL_TOKENS = 180_000   # 전체 파일 한계
MAX_WORKERS = 3             # 추가: 병렬 처리시 최대 워커 수

# 단일 시트 처리 함수
def process_sheet(sheet_name, worksheet, file_manager, generator):
    try:
        print(f"\n[{sheet_name}] 처리 시작...")
        
        # 구글시트에서 데이터 가져오기(9행 1열부터 시작)
        header_row = worksheet.row_values(9)[1:]  # 9행의 헤더를 가져옴
        # print(f"헤더: {header_row}")  # 디버깅용 출력
        rows = worksheet.get_all_records(head=9, expected_headers=header_row)  # 데이터를 가져옴
        # print(f"데이터: {rows}")  # 디버깅용 출력

        # 3열 데이터 필터링
        # filtered_rows = []
        # for row in rows:
        #     if isinstance(row, dict):  # row가 딕셔너리인지 확인
        #         if row.get(header_row[2]) == "자동화":  # 3열 데이터가 "자동화"인 경우
        #             filtered_rows.append(row)
        #     else:
        #         print(f"잘못된 데이터 형식: {row}")  # 디버깅용 출력

        # 데이터를 프롬프트로 변환
        all_prompts = []
        for row in rows:
            prompt_json = PromptGenerator(row).generate()
            all_prompts.append(prompt_json)
        
        # 프롬프트 저장
        file_manager.save_prompt_json(all_prompts, sheet_name)
        print(f"[{sheet_name}] 프롬프트 생성 완료 ({len(all_prompts)}개)")
        
        return {"sheet": sheet_name, "status": "success", "all_prompts": all_prompts}
    
    except Exception as e:
        error_msg = f"[{sheet_name}] 오류 발생: {str(e)}"
        print(error_msg)
        return {"sheet": sheet_name, "status": "failed", "error": str(e)}

# 메인 실행
reader = GoogleSheetReader(CREDENTIALS, SHEET_NAME)
file_manager = FileManager(OUTPUT_DIR)

worksheets = reader.get_worksheets()[1:]    # 첫 시트는 제외함

# TestCodeGenerator 초기화
generator = TestCodeGenerator(
    model_name="claude-3-7-sonnet-20250219",
    temperature=0.3,
    system_prompt=ui_requirement,
    max_tokens_per_request=MAX_REQ_TOKENS
)

start_time = time.time()

# 프롬프트생성 병렬처리
print(f"병렬 처리 모드로 실행 (최대 {MAX_WORKERS}개 워커)")
results = []
all_prompts_dict = {}

with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
    # 각 워크시트에 대한 작업 제출
    future_to_sheet = {
        executor.submit(process_sheet, ws.title, ws, file_manager, generator): ws.title
        for ws in worksheets
    }

    # 작업 완료 시 결과 처리
    for future in concurrent.futures.as_completed(future_to_sheet):
        sheet_name = future_to_sheet[future]
        try:
            result = future.result()
            results.append(result)
            
            # 결과에 따라 상태 출력
            if result["status"] == "success":
                print(f"[{sheet_name}] 프롬프트 저장 완료")
                all_prompts_dict[sheet_name] = result.get("all_prompts", [])  # 프롬프트 저장
            else:
                print(f"[{sheet_name}] 프롬프트 저장 실패: {result.get('error', '알 수 없는 오류')}")
                
        except Exception as e:
            print(f"[{sheet_name}] 예외 발생: {e}")
            results.append({"sheet": sheet_name, "status": "failed", "error": str(e)})

# 모든 프롬프트 생성 작업이 완료될 때까지 기다림
print("\n프롬프트 파일 생성 완료. 테스트 코드 생성 시작...")

# 테스트 코드 생성 및 저장 (직렬 처리)
for ws in worksheets:
    sheet_name = ws.title
    try:
        # 해당 워크시트의 프롬프트 가져오기
        all_prompts = all_prompts_dict.get(sheet_name, [])
        if not all_prompts:
            print(f"[{sheet_name}] 프롬프트가 없어 테스트 코드 생성을 건너뜁니다.")
            continue

        # 테스트 코드 생성
        print(f"[{sheet_name}] 테스트 코드 생성 시작...")
        generated_code = generator.generate_code_with_token_check(
            all_prompts,
            max_total_tokens=MAX_TOTAL_TOKENS
        )
        
        # 테스트 코드 저장
        file_manager.save_test_code_as_multiple_files(generated_code, sheet_name)
        print(f"[{sheet_name}] 테스트 코드 생성 및 저장 완료")
            
    except Exception as e:
        print(f"[{sheet_name}] 예외 발생: {e}")
        results.append({"sheet": sheet_name, "status": "failed", "error": str(e)})
    
# 실행 결과 요약
end_time = time.time()
elapsed_time = end_time - start_time

success_count = sum(1 for r in results if r["status"] == "success")
failed_count = sum(1 for r in results if r["status"] == "failed")

print("\n" + "=" * 50)
print(f"작업 완료: {len(results)}개 시트 처리됨 (성공: {success_count}, 실패: {failed_count})")
print(f"총 소요 시간: {elapsed_time:.2f}초 ({elapsed_time/60:.2f}분)")

# 실패한 시트 목록
failed_sheets = [r["sheet"] for r in results if r["status"] == "failed"]
if failed_sheets:
    print(f"\n실패한 시트: {', '.join(failed_sheets)}")

print("=" * 50)



