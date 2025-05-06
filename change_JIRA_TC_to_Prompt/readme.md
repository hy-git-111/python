# 개요
: LLM을 활용한 테스트 스크립트 작성을 위해 프롬프트 출력 코드 작성  
- JIRA에서 작성한 테스트케이스를 ADF(Atlassian Document Format)로 추출
- 추출한 ADF로 LLM이 이해하기 쉽도록 프롬프트 생성 

# 사용 방법
1. user_data.py 파일 생성 및 아래 내용 입력 
    ```py
    JIRA_URL = "https://{your_jira_url}"    # .atlassian.net
    EMAIL = "{your_email}"                  # JIRA 로그인 시 사용한 email
    API_TOKEN = "{your_jira_api_token}"     # JIRA에서 AIP TOKEN 발급하여 입력
    ```

<br/>

2. extract_jira_adf.py 설정
* Custom Field가 있는 경우
- 아래 url에서 Custom Field ID 확인하여 extract_json()의 params["field"]에 추가
    ```py
    {JIRA_URL}/rest/api/3/field
    ```
- extract_json()의 testcase 변수에 Custom Field 추가

* adf json 반환값 예시
```
{
  "test_case_id": "SCRUM-1",
  "title": "로그인 기능 정상 작동 확인",
  "description": {
    "type": "doc",
    "version": 1,
    "content": [
      {
        "type": "paragraph",
        "content": [
          {
            "type": "text",
            "text": "사용자가 정상적인 ID/PW로 로그인 시도할 경우, 성공 여부를 확인한다."
          }
        ]
      }
    ]
  },
  "사전 조건": null,
  "재현 절차": {
    "type": "doc",
    "version": 1,
    "content": [
      {
        "type": "orderedList",
        "attrs": {
          "order": 1
        },
        "content": [
          {
            "type": "listItem",
            "content": [
              {
                "type": "paragraph",
                "content": [
                  {
                    "type": "text",
                    "text": "아이디 입력 필드에 ‘test_user123’ 입력"
                  }
                ]
              }
            ]
          },
          {
            "type": "listItem",
            "content": [
              {
                "type": "paragraph",
                "content": [
                  {
                    "type": "text",
                    "text": "비밀번호 입력 필드에 ‘password123’ 입력"
                  }
                ]
              }
            ]
          },
          {
            "type": "listItem",
            "content": [
              {
                "type": "paragraph",
                "content": [
                  {
                    "type": "text",
                    "text": "‘확인’ 버튼 클릭"
                  }
                ]
              }
            ]
          }
        ]
      }
    ]
  }
}
```

<br/>

3. generate_prompt.py 실행

* 출력 예시
```
다음 JSON을 기반으로 Selenium Python 테스트 코드를 생성해줘:

테스트 ID: SCRUM-1
테스트 시나리오: 로그인 기능 정상 작동 확인
설명: ['사용자가 정상적인 ID/PW로 로그인 시도할 경우, 성공 여부를 확인한다.']
사전 조건 : []
재현 절차 : ['아이디 입력 필드에 ‘test_user123’ 입력', '비밀번호 입력 필드에 ‘password123’ 입력', '‘확인’ 버튼 클릭']
기대 결과 : ['url에 ‘login’ 포함되지 않음', "‘username님 안녕하세요' 문구 표시됨"]
구현 함수명 : None


요구사항:
- Chrome WebDriver 사용
- 각 step마다 주석 작성
- 가능한 경우 assert문으로 expected_result 체크
- 페이지 주소는 예시로 넣어도 괜찮음
```