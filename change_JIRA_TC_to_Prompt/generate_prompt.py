import os
from extract_jira_adf import extract_json

# ADF 필드를 받아서 텍스트를 문자열로 반환하는 함수
def extract_text_from_adf_field(adf_field):
    """
    Atlassian Document Format(ADF)에서 모든 텍스트를 재귀적으로 추출
    - paragraph, orderedList, listItem 등 다양한 구조 지원
    """
    result = []

    # 내부 함수(클로저) 구조
    # 계층구조 문서 포맷에서 엑스트 추출 
    def traverse(node):
        if isinstance(node, dict):
            node_type = node.get("type")
            if node_type == "text":
                result.append(node.get("text", ""))
            elif "content" in node:
                for child in node.get("content", []):
                    traverse(child)
        elif isinstance(node, list):
            for item in node:
                traverse(item)

    try:
        if isinstance(adf_field, dict) and adf_field.get("type") == "doc":
            traverse(adf_field.get("content", []))
    except Exception as e:
        print("ADF 파싱 오류:", e)

    return "\n".join(result).strip()

# ADF 필드를 받아서 텍스트로 추출하고 줄 단위로 나눠주는 함수
def parse_adf_to_lines(adf_field):
    """ADF 필드를 받아 텍스트 추출 후 줄 단위 리스트로 반환"""
    text = extract_text_from_adf_field(adf_field)
    return [line.strip() for line in text.split("\n") if line.strip()]


# ADF json 데이터를 입력받아 프롬프트를 출력하는 함수
def generate_prompt_from_testcase(json_data):
    if not isinstance(json_data, dict):
        json_data = {}
        
    test_case_id = json_data.get("test_case_id", "")
    title = json_data.get("title", "")

    description = parse_adf_to_lines(json_data.get("description", {}))
    pre_condition = parse_adf_to_lines(json_data.get("사전 조건", {}))
    steps = parse_adf_to_lines(json_data.get("재현 절차", {}))
    expected_result = parse_adf_to_lines(json_data.get("기대 결과", {}))

    script_func = json_data.get("함수명", [])

    # 요구사항 입력
    prompt = f"""
    다음 JSON을 기반으로 Selenium Python 테스트 코드를 생성해줘:

    테스트 ID: {test_case_id}
    테스트 시나리오: {title}
    설명: {description}
    사전 조건 : {pre_condition}
    재현 절차 : {steps}
    기대 결과 : {expected_result}
    구현 함수명 : {script_func}
    """

    # 추가 요구사항 입력
    prompt += """

    요구사항:
    - Chrome WebDriver 사용
    - 각 step마다 주석 작성
    - 가능한 경우 assert문으로 expected_result 체크
    - 페이지 주소는 예시로 넣어도 괜찮음
    """

    return prompt

# 프롬프트를 텍스트 파일로 저장하는 함수
def save_prompt_to_file(prompt_text, test_case_id, output_dir="prompts"):
    os.makedirs(output_dir, exist_ok=True)
    filename = os.path.join(output_dir, f"{test_case_id}.txt")
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(prompt_text)
        print(f"[저장 완료] → {filename}")
    except Exception as e:
        print(f"[저장 실패] {filename} - 오류: {e}")

# 실행
testcases = extract_json()
for tc in testcases:
    prompt = generate_prompt_from_testcase(tc)
    print(prompt)

    # 파일 저장
    test_case_id = tc.get("test_case_id", "unnamed")
    save_prompt_to_file(prompt, test_case_id)
