import sys
import io
import requests
from requests.auth import HTTPBasicAuth
import user_data

# print 출력 인코딩 utf-8로 설정
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8") 

def extract_json():

    JIRA_URL = user_data.JIRA_URL
    EMAIL = user_data.EMAIL
    API_TOKEN = user_data.API_TOKEN
    PROJECT_KEY = "SCRUM"
    ISSUE_TYPE = "Test Case"

    # JQL 쿼리
    jql = f"project = {PROJECT_KEY} AND issuetype = '{ISSUE_TYPE}'"

    # API 요청
    response = requests.get(
        f"{JIRA_URL}/rest/api/3/search",
        headers={"Accept": "application/json"},
        params={
            "jql": jql,
            "fields": "summary,description, customfield_10039, customfield_10040, customfield_10041, customfield_10042" # 사전 조건, 재현 절차, 기대 결과, 구현 함수명
        },
        auth=HTTPBasicAuth(EMAIL, API_TOKEN)
    )

    # JSON 출력
    if response.status_code == 200:
        issues = response.json()["issues"]
        testcases = []
        for issue in issues:
            testcase = {
                "test_case_id": issue["key"],
                "title": issue["fields"]["summary"],
                "description": issue["fields"]["description"],
                "사전 조건": issue["fields"]["customfield_10039"],
                "재현 절차": issue["fields"]["customfield_10040"],
                "기대 결과": issue["fields"]["customfield_10041"],
                "함수명": issue["fields"]["customfield_10042"],
            }
            
            # print(json.dumps(testcase, indent=2, ensure_ascii=False))
            testcases.append(testcase)
            
        # print(testcases)
        return testcases
    else:
        print("요청 실패:", response.status_code, response.text)


extract_json()