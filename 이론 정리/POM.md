 # POM
: 디자인 패턴 중 하나, 웹 페이지 또는 UI의 중요 컴포넌트를 하나의 클래스(객체)로 추상화

<span style="color:darkgray">**디자인 패턴 : 클래스의 복잡성으로 인해 사이드 이펙트 발생 > 이를 해결하기 위해 미리 클래스의 디자인을 제시한 것  
Builder : 디자인 패턴 중 하나, 빌드를 할때 형식을 미리 제시한 빌더 패턴**</span>

* 설계 원칙
    * 1 Class per Page/Component  
    : 클래스 하나 당 웹 애플리케이션의 각 페이지 또는 주요 UI 컴포넌트(로그인 폼, 헤더 등)마다 클래스 작성

    * Represent Elements(요소 표현)  
    : 클래스 내부에 해당 페이지의 Locator 정의

    * Encapsulate Actions(동작 캡슐화)  
    : 사용자가 HTML 코드를 보지 않아도 테스트코드를 이해할 수 있도록 작성

    * No Assertions in Page Objects  
    : 페이지 객체는 테스트 결과 검증(Assertion) 로직을 포함하지 않아야 함

    * Return Next Page Object (Optional but useful)  
    : 액션 수행 결과 다른 페이지로 이동하는 경우, 해당 페이지의 객체를 반환하여 페이지 체이닝 가능(Page Chaining)
        ```py
        class CurrentPage(BasePage):
            ...
            def method(self):
                ...
                return NextPage(self.driver)    # 다른 페이지 객체 반환
        ```

<br/>

## POM을 적용한 파일 구조
```
Root/
├── tests/              # 테스트 실행 스크립트와 fixture (conftest.py) 위치
│   └── conftest.py     # 전역 fixture, driver 초기화 등

├── reports/            # 테스트 리포트, 로그, 스크린샷 저장용
│   ├── logs/           # 테스트 로그 파일 저장
│   └── screenshots/    # 실패 시 자동 캡처 이미지 저장

├── src/                # 테스트 로직과 POM 관련 모듈
│   ├── utils/          # 공통 유틸 함수 (ex. 날짜 변환, 로깅 등)
│   ├── locators/       # 페이지별 로케이터 (By.ID 등)
│   ├── components/     # 공통 컴포넌트 클래스 (모달, 공통 버튼 등)
│   ├── pages/          # 각 페이지의 Page Object 정의
│   ├── resource/       # 테스트에 필요한 외부 데이터
│   │   └── data/       # CSV, JSON 등 테스트 데이터 파일
│   └── base_page.py    # 공통 페이지 액션 정의 (find_el 등)

├── requirements.txt    # 의존 패키지 리스트
├── pytest.ini          # Pytest 설정 (log level, 마커 등)
```

* \__init__.py
: 해당 디렉토리가 '패키지'임을 알려주는 역할

<br/>

### Root/
* requirements.txt : 필요한 라이브러리와 버전 명시
    ```
    pip freeze > requirements.txt   # 현재 환경의 패키지 목록 저장
    pip install -r requirements.txt # 파일에 명시된 라이브러리 일괄 설치
    ```

<br/>

* 환경설정파일
    * .env  
    : 보안에 유리함
        ```
        pip install python-dotenv
        ```

        ```.env
        ENV=qa
        BASE_URL=https://qa.example.com
        USERNAME=qa_user
        PASSWORD=qa_pass
        TIMEOUT=10
        ```

        ```py
        # page_object.py 또는 test_code.py
        from dotenv import load_dotenv
        import os

        # .env 파일 로드
        load_dotenv()

        # 환경변수 사용
        env = os.getenv("ENV")
        base_url = os.getenv("BASE_URL")
        username = os.getenv("USERNAME")
        timeout = int(os.getenv("TIMEOUT"))

        print(env, base_url, username, timeout)
        ```

    <br/>

    * config.ini  
    : 환경설정이 1~2단계로 단순할때 사용  
    파이썬 내장 라이브러리인 configparser와 함께 사용 가능
        ```ini
        # config.ini
        [QA]
        base_url = https://qa.example.com
        username = qa_user
        password = qa_pass
        ```
        
        ```py
        # page_object.py 또는 test_code.py
        from config_reader import get_config

        cfg = get_config("QA")
        url = cfg["base_url"]
        username = cfg["username"]
        password = cfg["password"]
        ```
    
    <br/>

    * config.yaml  
    : 문자열, 숫자, 불리언 등 데이터 타입을 자동으로 인식, 가독성 높고 복잡한 설정 표현에 적합  
    dynaconf(서드파티 라이브러리)와 함께 사용 가능
        
        ```
        pip install pyyaml
        ```
        
        ```yaml
        # config_yaml.py
        qa:
        base_url: https://qa.example.com
        username: qa_user
        password: qa_pass
        ```

        ```py
        # config_reader.py
        import yaml

        def get_config(env="dev"):
            with open("config.yaml", "r") as f:
                all_config = yaml.safe_load(f)
            return all_config.get(env, {})
        ```

        ```py
        # page_object.py 또는 test_code.py
        from config_reader import get_config

        cfg = get_config("qa")
        print(cfg["base_url"])  # https://qa.example.com
        print(cfg["username"])  # qa_user
        ```
<br/>

### src/
* BasePage.py  
: 여러 페이지 객체에서 공통으로 사용되는 요소나 메서드를 정의해놓은 클래스  
공통 액션 래퍼(wrapper)메서드는 내부 사용 목적임을 나타내기 위해 언더스코어(_) 접두사 사용
    * "내부" 사용 예시
        - BasePage 클래스 내부의 다른 메서드들이 호출할때
        - 서브클래스(BasePage를 상속받은 하위 페이지 객체)에서 사용할때
        - 같은 모듈(파일) 내 코드에서 사용할때
        - 같은 패키지(폴더) 내 코드에서 사용할 때 

    ```
    BasePage.py	# 특정 페이지에서 사용하는 함수
    └─ class BasePage
        ├─ def _explicit_wait하여_입력
        ├─ def _explicit_wait하여_클릭
        └─ def _explicit_wait하여_텍스트 출력	# 검증에서 사용하는 함수도 정의 가능
    ```
<br/>

* utils.py  
 : 특정 페이지와 관계없는 범용 **함수**들의 집합(class 없음)
    ```
    utils/
    ├─ utils.py
        ├─ def 랜덤 이메일 생성 함수
        ├─ def 날짜 변환 함수 
        ├─ def 임의의 문자열 생성 함수
    ```
<br/>

* page.py  
: 해당 페이지에서 사용되는 개별 메서드와 조합 메서드 정의  
BasePage를 상속받아 사용
    ```
    pages/
    ├─ 로그인 페이지.py
        └─ class 로그인(BasePage)
            ├─ def __init__(self, driver):
                super().__init__(driver)
            ├─ def id_입력
            ├─ def pw_입력
            ├─ def 로그인버튼_클릭
            ├─ def 로그인_진행   # 조합 메서드
    ```
<br/>

#### components/
* Component Objects  
: 페이지 내의 재사용 가능한 복잡한 UI 컴포넌트(예: 날짜 선택 위젯, 그리드 테이블)를 별도의 객체로 분리

<br/>

### reports