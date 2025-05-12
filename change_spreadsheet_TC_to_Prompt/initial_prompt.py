ui_requirement = """
다음 테스트 케이스를 기반으로 각 파일에 들어갈 코드를 작성해주세요
토큰 제한에 걸리면 답변을 분할하여 연속적으로 전달해주세요
**모든 설명은 주석으로 작성해주세요**
코드를 작성하겠다는 말 없이 **바로 테스트코드만 작성해주세요**
연속적으로 전달 시 연속적으로 전달한다는 안내 없이 **코드만 작성해주세요**
**바로 실행 가능하도록** 작성해주세요

프론트엔드 코드: https://github.com/gothinkster/react-redux-realworld-example-app
base_url = http://localhost:4100/

요구사항:
- Selenium Pytest 사용
- **코드 시작 전 반드시 파일명을 주석으로 작성(# test.py)**
- 반드시 **파일구조**에 맞춰 작성
- 반드시 **Precondition과 Steps**을 포함하는 코드 작성성
- 각 step마다 주석 작성
- 명확한 import 문 작성
- 계정이 필요한데 **Precondition과 Steps에 없는 경우** 예시로 작성 가능

- test.py, conftest.py, test_data.py, locator.py 파일로 나누어 작성
- **conftest.py는 최초 1회만** 작성
- 각 테스트 케이스는 함수로 작성(1대1 대응)
- 각 테스트 케이스는 @pytest.mark.parametrize로 작성
- 테스트 수행 시 데이터 세팅이 필요없는 경우 @pytest.mark.before_set_data
- 테스트 수행 시 데이터 세팅이 필요한 경우 @pytest.mark.after_set_data

- 필요시 pytest.ini 생성

- 테스트 코드는 headless 모드로 작동
- 테스트 코드는 병렬 실행 가능
- 모든 테스트는 요소에 대한 명확한 locator를 사용
- 모든 테스트 코드는 emplicit wait을 사용
- **Expected Result**에 있는 **모든 항목 assert문으로 작성**
- 각 테스트 케이스는 try-except로 작성
- 각 테스트 케이스 수행 시 로그 추가, 로그파일 경로는 base_dir/reports/logs/로 설정, 파일명은 %Y%m%d.log 형식으로 설정
- 각 테스트 케이스 수행 시 스크린샷 추가, 스크린샷 파일명은 base_dir/reports/screenshoots/{test_case_name}_{function_name}.png 형식으로 설정

파일구조:
change_spreadsheet_TC_to_Prompt/
├── config/         # 설정 파일 (예: 기본 URL, 타임아웃)
│   └── config.py
├── data/           # 테스트 데이터 파일 (예: 사용자 인증 정보, 게시글 내용)
│   └── test_data.py  # 테스트 데이터 작성, Chrome WebDriver 사용
├── pages/          # 페이지 객체 모델(POM) 클래스
│   ├── __init__.py
│   ├── base_page.py    # 모든 페이지 객체가 상속받는 부모 클래스, Explicit Wait을 사용한 공통적인 Selenium 상호작용 메서드를 포함
│   ├── home_page.py
│   ├── login_page.py
│   ├── editor_page.py
│   ├── settings_page.py
│   ├── article_page.py   # 게시글 상세 페이지
│   └── profile_page.py   # 프로필 페이지
├── reports/        # 테스트 실행 보고서 (예: HTML 보고서) -.gitignore 처리 권장
│   └── report.html
├── tests/          # 테스트 스크립트 (pytest 사용)
│   ├── __init__.py
│   ├── conftest.py     # 프로젝트 수준의 fixture (예: WebDriver 설정)
│   ├── test_auth.py    # 인증 관련 테스트 (로그인, 회원가입, 로그아웃)
│   ├── test_article.py # 게시글 CRUD 관련 테스트
│   ├── test_settings.py# 설정 변경 관련 테스트
│   ├── test_comment.py # 댓글 관련 테스트
│   └── test_social.py  # 팔로우, 즐겨찾기 관련 테스트
├── utils/          # 특정 페이지나 테스트에 종속되지 않는 범용 헬퍼 함수나 클래스(예: 커스텀 로깅 설정, 랜덤 데이터 생성기, 날짜/시간 처리 유틸리티)를 포함합니다.
│   ├── __init__.py
│   └── helpers.py
├── venv/           # Python 가상 환경 -.gitignore 처리 권장
├── locator/        # 각 페이지의 locator 입력
├── .gitignore      # Git 추적 제외 파일 목록
├── pytest.ini      # pytest 실행 시 적용될 설정을 정의하는 파일
├── README.md       # 프로젝트 개요, 설정, 실행 방법 안내
└── requirements.txt# 프로젝트 실행에 필요한 모든 Python 패키지 목록을 명시
"""