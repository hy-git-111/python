# 단위테스트 절차
1. 환경 설정
2. 테스트 코드 작성
3. 테스트 실행

</br>

## 환경 설정 - 가상 환경
* 가상환경
    * 가상환경은 OS 호환이 되지 않는다.
    * Python에서는 버전에 따라 lib/pkg 충돌이 있을 수 있다. 따라서 가상환경을 통해 컨테이너화 하면, 프로젝트마다 충돌을 방지할 수 있다.

    > <span style="color:darkgray">**Python 이외의 다른 언어는 src > package.json을 활용해 일정한 환경을 유지할 수 있다.**</span>

* 가상환경 생성 : python -m venv venv

* 가상환경 활성화
    * Windows : venv\Scripts\activate
    * Mac/Linux : source venv/bin/activate

</br>

## 단위테스트 프레임워크
* unittest
    * 내장 라이브러리
    * 클래스 기반 테스트
    * 정형화된 메서드명 사용

* pytest  
: 확장성이 좋음, unittest 치환 가능
    * 외부 라이브러리
    * 함수 기반 테스트
    * 'test_'로 시작하는 메서드명 사용
    * Fixture 기능 제공
    : DB Set 등 테스트를 위해 필요한 자원을 미리 준비 가능

</br>

### unittest
* Unittest 실행 흐름  
: setUp() - 테스트 메서드 실행 - tearDown()

* Unittest 기본 구성 요소
    * Test Suit : 테스트 파일
    * Test Case : Class
    * Test Step : Method
    * Test Runner : 테스트 실행 및 결과 출력 도구
    * Assertions : 테스트 검증을 위한 명령

* Unittest 클래스의 주요 메서드
    * setUp() : 사전작업(셀레니움 url, 쿠키 정보 등)
    * tearDown() : 테스트 후 정리 작업
    * assertEqual() : 값이 같은지 확인
    * assertNotEqual()
    * assertTrue() : 조건이 참인지 확인
    * assertRaises() : 특정 예외 상황이 동작하는지 확인
    * assertIsNone() : 값이 None인지 확인

* Unittest 데코레이터  
: 특정 클래스나 함수에 추가적인 기능을 부여(기능 확장)하기 위해 사용
    * @unittest.skip('이 테스트 스텝은 넘어갑니다.') : 결과 출력 's'
    * @unittest.expectedFailure : 결과 출력 'x'

* 실행 명령어 : python -m unittest discover 디렉터리

</br>

### pytest
* pytest 데코레이터
    * @pytest.mark.parametrize() : 테스트 함수에 여러 개의 입력값을 제공하여 동일한 테스트를 반복 실행
    * @pytest.fixture() : 필요한 데이터나 객체 반환

* 실행 명령어  
: pytest 디렉터리/파일명.py::특정 함수

* 옵션
    * -v : verbose, 자세한 결과 출력
    * -q : quiet, 간략한 결과 출력
    * -x : 첫 번째 실패 시 즉시 종료
    * --maxfail=N : N개 실패 시 실행 종료
    * -k "키워드" : 특정 키워드를 포함한 테스트만 실행
* 플러그인
    * pytest-html : 결과를 html 리포트로 저장
    * pytest-cov : 코드 커버리지 분석 및 리포트 생성
    * pytest-xdist : 테스트 병렬 실행
    * pytest-rerunfailures : 테스트 실패 시 자동 재실행
    * pytest-mock : mock 객체 생성 및 관리

</br>

# 코드 작성 시 참고사항
* FIRST 원칙
    * Fast : 테스트는 빠르게 실행되어야 함
    * Independent : 각 테스트가 독립적이어야 함
    * Repeatable : 환경에 무관하게 항상 동일한 결과 보장
    * Self-validating : 테스트 결과가 성공/실패로 명확하게 나타나야 함
    * Timely : 코드를 작성한 직후에 테스트 작성

* AAA 패턴
: 테스트 코드를 3단계로 나누는 패턴
    * Arrange : 테스트 준비
    * Act : 실제 동작 수행
    * Assert : 결과 검증

* 유지보수를 위한 테스트 코드 5대 원칙
    * 명확한 테스트명 사용
    * 단일 책임의 원칙
    * 반복 코드 최소화
    * 실패 원인 명확화
    * 변경에 강한 구조