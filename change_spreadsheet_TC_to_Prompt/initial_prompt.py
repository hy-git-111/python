ui_requirement = """
다음 테스트 케이스를 기반으로 각 파일에 들어갈 코드를 작성해주세요
토큰 제한에 걸리면 답변을 분할하여 연속적으로 전달해주세요
**모든 설명은 주석으로 작성해주세요**
코드를 작성하겠다는 말 없이 **바로 테스트코드만 작성해주세요**
연속적으로 전달 시 연속적으로 전달한다는 안내 없이 **코드만 작성해주세요**

프론트엔드 코드 : https://github.com/gothinkster/react-redux-realworld-example-app

요구사항:
- Selenium Pytest 사용
- **코드 시작 전 반드시 파일명을 주석으로 작성(# test.py)**
- 각 step마다 주석 작성
- 명확한 import 문 작성
- 계정이 필요한 경우 예시로 작성 가능

- test.py, conftest.py, test_data.py, locator.py 파일로 나누어 작성
- test.py : 테스트 케이스 작성
- conftest.py : fixture 작성
- test_data.py : 테스트 데이터 작성, Chrome WebDriver 사용
- locator.py : locator 작성

- 각 테스트 케이스는 함수로 작성(1대1 대응)
- 각 테스트 케이스는 @pytest.mark.parametrize로 작성
- 각 테스트 케이스는 assert문으로 작성
- 각 테스트 케이스는 try-except로 작성
- 각 테스트 케이스 수행 시 로그 추가
"""