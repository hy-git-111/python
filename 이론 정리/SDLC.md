# SDLC, Software Developement Life Cycle
1. 계획  
: 사업계획, 리소스, 일정 계획, 위험요소 식별 

    * 산출물 : 프로젝트 계획서, 리스크 관리 보고서

2. 요구사항 정의  
: 요구사항 수집과 정의분석  
문서화, 기능 정의, 릴리즈 일정, 디자인 정의  

    * 산출물 : 기능 정의서, 요구사항 명세서, 사용자 시나리오

3. 설계  
: 서버, 아키텍처 설계  

    * 산출물 : DB 설계서, UI Prototype

4. 구현  
: 소스코드 구현 및 빌드

    * 산출물 : 소스 코드

5. 테스트, 배포  
: 기능 및 성능 검증, 결함 발견 및 수정

    * 산출물 : Test Case, 테스트 결과 보고서, 결함 목록

6. 유지보수

<br/>

## SDLC 모델
* Waterfall
    * 순차 개발, 기능 구현에 집중
    * 최종 제품 단계에서 고객 피드백 반영
    * 명확한 계획과 예측 가능성 필요

<br/>

* Agile
    * 반복적(iteration), 점진적(incremental) 개발
    * 스프린트마다 고객 피드백 반영
    * 관리 복잡성, 일정 예측이 어려움

<br/>

## SDLC 단계
### 계획
* 프로젝트 목표 설정 기준(SMART)
    * Specific : 구체적
    * Measurable : 측정 가능
    * Action-oriented : 실천 지향적
    * Realistic : 현실적
    * Time-limited : 기한 준수

<br/>

* 리소스와 일정 계획
    * 간트차트(Gantt)  
        : 마일스톤(주요 목표나 단계의 달성을 나타내는 이정표) 설정  
        일정관리, 작업 순서와 의존성 확인

<br/>

* 위험 평가 및 관리
    * 리스크 매트릭스

<br/>

* 계획 단계 성과 측정 방법
    * KPI, Key Performance Indicator
        * 계획 완료율
        * 리스크 식별률
        * 자원 할당 정확도
        * 테스트 툴 사용률
        * 스크립트 작성률

### 요구사항 정의
: 목표와 범위 구체화 과정, 사용자와 직군별 시점으로 기능에 대한 피드백 공유 

* 요구사항 수집 방법
    * 인터뷰
    * 설문조사
    * 워크숍

> <span style="color:darkgray">**모든 구성원이 참여하여  
개발 진행 방식, 데이터 흐름, 기능에 대한 이해(무엇을 만드는가)등  
프로젝트에 대한 이해를 마쳐야 함(애자일 기준)**</span>

<br/>

* 요구사항 분석
    1. 요구사항 분류
    2. 충돌 요구사항 해결
    3. 기술적 타당성 검토

<br/>

* 요구사항 분석 도구
    * UML, Unified Modeling Language
    : 개발을 위해 각 구성요소 간의 관계를 도식화(표준화)한 설계도

    * 구조 다이어그램(Structure Diagram)  
        Class Diagram
        : 클래스 - 메소드 간의 관계 도식화

    * 행위 다이어그램(Behavior Diagram)   
        유스케이스 다이어그램
        : 사용자 흐름을 시각적으로 표현

<br/>

* 요구사항 우선순위화 기법
    * MoSCow 기법
        * Must Have : 핵심 기능
        * Should Have : 필수는 아니지만 우선순위가 높은 기능
        * Could Have : 제품 혹은 서비스의 성공 여부에 큰 영향을 끼치지 않는 기능
        * Won't Have : 당장 필요로 하지 않는 기능

    * Kano 모델
        : 고객 만족과 불만에 영향을 주는 매력적 요소, 일원적 요소, 당연적 요소를 구분

> <span style="color:darkgray">**결론적으로, 제품의 핵심 기능이 우선순위가 높을 수 밖에 없음**</span>

<br/>

* 요구사항 변경 관리
    1. 변경 요청 수집
    2. 영향도 분석
    3. 승인 및 재 조정

<br/>

### 설계
: 요구사항 정의 단계에서 도출된 정보를 바탕으로 구조와 동작 방식을 구체화  
sw 생명주기가 중단되지 않도록 설계해야함

> <span style="color:darkgray">**QA : 개발자 툴 세팅 지원, 테스트 계획/일정 수립, TC 작성**</span>

* sw 아키텍처
: 시스템 전반의 구조와 설계를 정의하는 틀, 지침서  
데이터 흐름과 설계 방식에 대해 문서화 하는 것

<br/>

* sw 아키텍처 설계 유형
    * Monolithic(계층형)  
    : FE, BE, DB를 계층적으로 분리하여 설계

    * Microservice Architecture  
    : 각 기능을 분리 설계하여 대규모 트래픽, 유지보수에 용이  
    비용이 많이들고 복잡성이 높음

    * Serverless  
    : 클라우드 플랫폼을 활용하여 서버 관리 부담 감소

<br/>

* 데이터 흐름 설계
    * 데이터 흐름 다이어그램(DFD)  
    : 데이터 입력, 처리, 저장및 출력 단계를 다이어그램으로 작성
    
        > <span style="color:darkgray">**DFD를 현업에서 잘 사용하지는 않음**</span>

<br/>

> <span style="color:darkgray">**각 구성원의 학습 수준, 일정 등을 고려하여 프로젝트를 설계해야 함**</span>

<br/>

### 구현
* 코딩 원칙
    * Clean Code
    : 가독성 있는 코드 작성
        * 코딩 표준, 아키텍처 표준, 설계 가이드 준수
        * 복잡함 최소화
        * 참조되거나 수정되는 코드는 기존 코드보다 가독성이 있어야 함
        * 반복성 최소화
        * 하나의 파일은 하나의 언어로 작성

    * DRY, Dont Repeat Yourself
    : 반복 코드 최소화

    * SOLID 원칙

<br/>

* 빌드 프로세스
    1. 코드 컴파일
    2. 의존성 설치
    3. 실행파일 생성
    4. 오류 검토 및 경고

<br/>

* 버전 관리  
: 소스 코드의 변경 사항을 추적하고, 팀원 간 협업을 지원하는 시스템

> <span style="color:darkgray">**구현 단계에서 QA가 개발자 코드에 테스트코드/스크립트를 작성하는 역할을 맡기도 함**</span>

<br/>

### 테스트
* 테스트 계획
    * 구성 : 테스트 범위, 목표, 일정, 리소스

<br/>

* 테스트 유형
    * 기능 테스트  
    : 요구된 기능을 제대로 수행하는지 검증

    * 성능 테스트  
    : Load Test(부하 테스트), Stress Test(스트레스 테스트)

    * 회귀 테스트  
    : 새로운 코드 변경이 기존 기능에 문제를 발새시키지 않는지 확인

    * 보안 테스트  
    : 시스템 보안 취약점 탐지

<br/>

* 테스트 자동화 툴
    * 웹 자동화
    : Selenium, Sypress
    * 단위테스트
    : JUnit, TestNG
    * API
    : Postman

> <span style="color:darkgray">**개발자가 사용할 테스트 코드 짜야하므로 대세인 자바를 아는게 좋음  
AI 관련된 것은 파이썬이 유리함**</span>

* 결함 관리 프로세스
    1. Defect Reporting
    2. Defect Analysis
    3. Detect Fixing
    4. Retest

<br/>

### 배포
* 배포 프로세스
    1. 준비
    2. 테스트 환경 준비
    3. 프로덕션 환경
    4. 사용자 제공

* 배포 전략

    > <span style="color:darkgray">**일반적인 배포 방식  
    1.기존 서버 중단(점검중 화면 출력)  
    2.배포 완료 후 사이트 운영 개시**</span>

    * Blue/Green(무중단 배포)
        1. 기존 서버 운영 + 신규 서버 배포
        2. 신규 서버로 트래픽 연결
        3. 기존 서버로 연결된 트래픽이 없어지면 기존 서버 셧다운, 신규 서버만 운영

        * 로드밸런서 : 트래픽 분배를 위한 스위치

    * Canary
        1. 100% 사용자 중, 소규모 그룹에 먼저 배포하여 안정성 확인
        2. 신규 배포 사용자를 점차적으로 증가시킴

    * Rolling
        1. 기존 시스템 일부 셧다운, 신규 서버로 연결
        2. 이를 반복하여 순차적으로 교체하는 방식으로 새로운 버전 배포

<br/>

### 유지보수
* 종류
    * 수정 유지보수
    * 적응 유지보수
    * 예방 유지보수
    * 기능 추가 유지보수

<br/>

* 유지보수 핵심 원칙
    * 사용자 피드백을 기반으로 한 지속적인 개선
    * 문서화를 통한 이력 확보
    * 장기적인 안정성을 고려한 업데이트

<br/>

* 사용자 피드백
    * 애널리틱스 도구(Google Analytics, Firebase)
    * 사용자 리뷰 및 평가
    * 온라인 설문조사

<br/>

* 자동화 도구
    * Log 관리
    : Splunk, ELK Stack

    * 모니터링 도구
    : Grapana, New Relic, Datadog
    
    * 자동화 배포 도구
    : Jenkins, CI/CD

<br/>

# Agile
* Agile의 4가지 가치
    * 개인과 상호작용
    * 고객과의 협력
    * 변화에 대한 대응
    * 동작하는 소프트웨어

* Agile의 12가지 원칙
    * 초기부터 지속적으로 고객 만족
    * 요구사항 변경 수용
    * 짧은 배포 간격
    * 함께 일하기
    * 동기 부여된 팀원들로 프로젝트 팀 구성
    * 대면식 의사소통
    * 동작되는 SW로 진도 측정
    * 지속 가능한 개발 속도 유지
    * 좋은 기술, 설계에 관심두기
    * 단순성
    * 자기 조직화 팀
    * 정기적인 효율성 제고

<!-- 1. 문제 발견
: 조직과 구성원이 현재 느끼고 있는 문제

1 on 1 : 매니저와 멤버가 1:1로 대화를 나누는 것
Pulse Survey : 특정 주제와 관련된 주기적인 설문조사
Community : 커피타임, 랜덤런치, 길드와 같이 자연스러운 분위기를 유도하는 모임
Townhall : 고위 임원이나 CEO가 주도하는 전사적 모임, 기업의 가치관과 목표에 대한 이야기를 하는 시간
대표와 임원진이 참여하여 피드백을 공유
Farewell Committe : 사직자에게 의견을 듣는 것

설계 단계에서의 목표
1. 문제에 대한 정확한 이해
2. 문제를 해결하기 위한 액션과 가설을 설정 : 이유와 효과성

실행 단계에서의 목표

Agile 개발 방식의 철학
변화에 빠르게 대응하고, 고객 중심의 개발 강조
소통과 협력을 통한 팀 중심의 접근법
<br/> -->

<br/>

## Agile 프레임워크
* Scrum : 반복적, 점진적 Sprint 기반 관리
* Kanban : 작업과 기능을 중심으로 프로젝트 관리
* SAFe : Scaled Agile Framework, 대규모 조직에서 Agile 도입을 지원

    > <span style="color:darkgray">**< Scrum vs Kanban >  
    Scrum : 빠른 피드백과 적응성을 위해 도입 초기부터 스크럼 규칙을 반드시 준수해야 함  
    Kanban : 작업의 지속적 흐름 유지, 낭비 최소화를 위해 현재 조직 상태를 점진적으로 개선  
    <br/>
    < 칸반의 변화 관리 원칙 >  
    1.지금 상태 그대로 시작한다.  
    2.개선은 점진적 변화를 통해 추구한다는 데에 합의한다.  
    3.모든 계층의 리더십 행동을 장려한다.**</span>

### Scrum
* 특징
    * Sprint  
    : 2~4주의 Sprint를 반복하여 점진적인 프로세스 진행
    
    * Cross-Functional  
    : 여러 이해관계자들이 모여 한 팀을 이루어 고객의 요구사항을 만족시킬때까지 프로젝트 진행
    
    * Backlog  
    : 요구사항, PO가 관리함
    
    * Daily Scrum

<br/>

* Scrum 프레임워크  
    1. 제품 백로그
    2. 스프린트 계획
    3. 스프린트 백로그
    4. 스프린트+일일스크럼
    5. 증분(INCREMENT)
    6. 스프린트 리뷰, 회고

<br/>

* Scrum 팀의 구성
    * PO, Product Owner  
    : 제품 백로그 관리, 고객 요구사항과 비즈니스 목표를 팀에 전달

    * Scrum Master  
    : 팀의 협업 조정 및 동기 부여, 작업 중단 최소화로 팀의 성과 극대화

    * 개발 팀  
    : 제품 설계 및 개발 실행

<br/>

* Sprint  
: 목표를 달성하기 위한 Scrum의 개발 주기  
명확한 목표, 장애물 제거, 효율적인 커뮤니케이션, 우선순위 관리가 중요함

    1. Sprint Planning, 계획 수립  
    : Product Backlog에서 작업 항목을 선정

    2. Daily Scrum, 일일 점검  
    : 팀원간 진행상황, 예정 업무, 문제점 공유

    3. Sprint Review, 성과 검토  
    : 작업 결과물을 이해관계자와 공유
        * Burn-down Chart  
        : 작업량 모니터링에 사용
        
        * Velocity  
        : 스프린트 횟수별 완료한 스토리 포인트의 합계를 그래프로 표시  
        매 스프린트마다 계획 대비 실제 완료율을 평가하는 정량적 지표로 사용

    4. Sprint Retrospective, 회고  
    : 팀의 문제 해결 능력 향상, 반복적인 문제 방지, 팀원의 만족도와 참여도 증가

    > <span style="color:darkgray">**Backlog : 프로젝트의 모든 작업 항목을 정리한 목록(요구사항)  
    Sprint Backlog ⊂ Product Backlog**</span>

<br/>

### Kanban
* Kanban의 특징
    * Kanbsn Board  
    : Workflow 시각화로 프로젝트가 진행되는 것을 팀원들이 인지하도록 함

    * WIP(Work In Process) 제한  
    : 우선순위를 바탕으로 현재 진행중인 업무의 수를 제한하여 작업의 병목 현상 방지

    * 업무 흐름 관리  
    : 업무 흐름 예측성을 위해 업무 흐름 중 진행 단계를 수치화하여 관리함
        * 리드타임 분포도  
        : 분포가 좁을수록 비즈니스 예측성이 높음  
        리드타임 분포도를 통해 업무 예상 종료일을 예측할 수 있음

        * 런차트(Run chart)  
        : 업무에 소요되는 시간이 많은 작업을 파악하기 쉬움  
        개선사항 논의에 사용

        * 누적 흐름도(CFD, Cumulative Flow Diagram)  
        : 업무 진행 속도 측정  
        일정 관리에 사용

        > <span style="color:darkgray">**업무 흐름 : 준비 - 진행(설계 + 구현) - 완료**</span>

    * 정책 명시화

    * 피드백 루프

    * 개선 & 발전 : 현재 상태에서 시작하여 함께 개선하고 프로세스 발전

## 개발 방법론
* TDD(Test Driven Development)  
: 요구사항 구현에 초점을 맞춘 테스트 주도 개발  
테스트 코드 작성 → 기능 구현 코드 작성 → 리팩토링 과정 반복

    * 기술적 구현 및 내부 로직 개발에 적용
    * 코드 품질 향상 및 리팩토링 용이
    * 요구사항 변경에 유연하지 못함

<br/>

* BDD(Behavior-Driven Development)
: 사용자 행동에 초점을 맞춘 테스트 주도 개발  
요구사항 → 행동 정의 → 코드 작성의 흐름을 보여줌

    * 비즈니스 요구사항과 사용자 중심 기능 개발에 적용
    * 개발자, 비즈니스 팀, QA팀 간의 협업 필요
    * 팀 간 협업 강화 및 명확한 요구사항 전달 가능

    > <span style="color:darkgray">**Cherkin 언어  
    : BDD에서 요구사항을 시나리오 형식으로 표현하기 위한 문법**</span>

    ````
    체르킨(Gherkin) 언어를 사용하여 시나리오 작성 예시  

    * Feafure : 기능의 대표 주제
    * Scenario : 특정 상황에서 시스템 동작 정의 
    * Steps
        * Given : 초기 상태 정의
        * When : 행위 정의
        * Then : 기대 결과 정의
        * And : 추가 사항
        * But : 예외 사항
    ````
    
## CI/CD
: Agile 방법론을 위한 핵심 활동  
변경 사항을 빠르게 확인하고 수정  
제품 품질과 배포 속도 향상

> <span style="color:darkgray">**CI : Continuous Integration, 지속적인 통합  
CD : Continuous Delivery, 승인 후 지속적인 제공  
CD : Continuous Deployment, 지속적인 자동 배포**</span>

* CI/CD 프로젝트 관리 툴
    * TestRail : TC 관리 및 결과 분석
    * Zephyr : Jira와 통합된 테스트 관리
    * QTest : 대규모 프로젝트 관리

### CI(Continuous Integration)
: 지속적인 통합, 자동화된 테스트로 품질 보증, 개발 환경에 적용
* CI 방법
    1. 코드 변경사항을 메인 저장소(Main Repository)에 주기적으로 병합(Merge)  
    : 가장 작은단위로 개발하고 통합해야함

    2. 통합을 위한 단계(빌드, 테스트, 병합)의 자동화  
    : 코드리뷰 후 주기적인 병합 > CI 서버에서 CI 스크립트를 통해 빌드와 테스트 자동 검토
        * 주기적인 병합으로 코드 충돌 최소화(개발 생산성 향상)
        * 작은 단위로 병합하므로 작은 단위로 버그 확인 가능 및 결함 수정 용이

* 사용 툴
    * Jenkins : 플러그인 지원으로 모든 환경에 적합
    * Circle CI : 통합 도구, 클라우드 기반의 빠르고 간단한 설정

<br/>

### CD(Continuous Delivery/Deployment)
: 개발과 배포 주기 단축, Staging, Production 환경에 적용

* CD 방법
    1. 병합한 코드를 릴리즈할 준비
    2. 릴리즈 검증(자동/수동)
    3. 배포(Deploy)
        * CD : Continuous Delivery, 승인 후 지속적인 제공  
        * CD : Continuous Deployment, 지속적인 자동 배포

* 사용 툴
    * Jenkins : 플러그인 지원으로 모든 환경에 적합
    * Gitlab CI/CD : GIt 저장소와 통합
    * GitHub Action
    * Docker : 컨테이너 기반 오픈소스 가상화 플랫폼
    * Kubernetes : 컨테이너화된 애플리케이션을 자동 배포/확장
    * Spinnaker : 멀티 클라우드를 지원하는 CD 플랫폼

> <span style="color:darkgray">**조건부 실행과 환경 변수  
조건부 실행 : 특정 조건에서만 CI/CD 단계 실행  
환경 변수 : 빌드 및 배포에 필요한 설정을 동적으로 전달**</span>

### CI/CD 파이프라인
: 코드의 빌드, 테스트, 배포 과정을 자동화한 워크플로우
Commit > Build > Test > Deploy
* CI/CD 파이프라인 단계
    * 커밋(Commit)  
    : 코드 저장소에 변경 사항을 저장하는것  
    Active > Partially Committed > Commit > Committed  
    (작업 완료 > 부분적 커밋 > 커밋 실행 > 커밋 완료)

        > <span style="color:darkgray">**롤백(Rollback)
        : 배포 후 문제가 발생했을 때 이전 버전으로 복구하는 작업  
        Active - Failed - Rollback - Aborted**</span>

    * 빌드(Build)  
    : 소스코드를 실행 가능 상태로 컴파일하여 배포 준비를 완료하는것  
    Maven, Gradle, npm, webpack

    * 테스트(Test)  
    : 단위테스트, 통합테스트, 종단 간 테스트(E2E Test)를 자동화 할 수 있음

    * 배포(Deploy)  
    : 스테이징 환경에서 테스트 수행 후 프로덕션 환경에 코드를 자동으로 배포

* 구성요소
    * VCS(버전관리 시스템) : 소스 코드 이력 관리
        * Git, GitHub, GitLab

    * CI/CD 서버 : 파이프라인 실행
        * Jenkins, GitHub Actions, GitLab CI/CD

    * 빌드 도구 : 코드를 실행파일/아티팩트로 변환
        * Maven, Gradle, npm, Webpack

    * 테스트 도구 : 코드 품질 검증
        * JUnit, Pytest, Cypress

    * 아티팩트 저장소 : 빌드된 결과물 저장 및 버전 관리

    * 배포 도구/환경 : 실행 환경에 코드 배포
        * Terraform : 운영 환경 배포, 인프라 코드화(IaC)
        
    * 모니터링/로깅 : 배포 후 서비스 상태 확인 및 문제 추적
        * Grafana
        * New Relic
        * Prometheus : CI/CD 파이프라인의 상태 및 성능 모니터링
        * SonarQube : CI/CD 환경에서 보안 취약점 탐지
<br/>

* CI/CD 파이프라인 최적화
    * 병렬처리 강화
    * 캐싱을 활용한 파이프라인 최적화
    * 파이프라인 실행 트리거 조건 설정
    * 불필요한 단계 제거

* CI/CD 파이프라인 보안 강화 전략
    * 정적 분석 보안 테스팅(SAST)
        * 코드 커밋/빌드 시 소스코드 취약점 자동 검사
        * SonarQube, Snyk Code 등

    * 동적 분석 보안 테스팅(DAST)
        * 실행 중인 애플리케이션 대상 취약점 스캔
        * 스테이징 환경 등에서 수행
        * OWASP, ZAP 등

    * 소프트웨어 구성 분석(SCA)
        * 사용하는 오픈소스 라이브러리 취약점 검사
        * OWASP Dependency-Check, Snyk Open Source

    * 컨테이너 이미지 스캔
        * Docker 이미지 빌드 후 취약점 검사
        * Trivy, Clair 등

## QA Ops(QA + DevOps)
* QA
    * 품질 기준 설정 및 모니터링
    * 자동화 테스트 작성 및 유지
    * 결과 분석 및 리포트

* DevOps(Development + Operation)
    * 배포 자동화 및 환경 설정
    * 운영 환경의 안정성 관리

* QA Ops(DevOps + QA)
    * 자동화와 지속적인 검증
    * 테스트 코드 작성 및 유지
    * 배포 이후 모니터링 데이터 분석(시스템 로그, 사용자 피드백과 성능 분석)
    * 품질 기준을 CI/CD에 통합
    * 테스트 자동화 툴 사용(Selenium, JUnit5, Pytest, Postman)

* DevSecOps(DevOps + Security + QA)
    * 개발, 보안, 운영이 통합된 직군을 나타내는 용어
    * 전체 IT 라이프사이클에 걸쳐 보안을 공동의 가치로 통합

    > <span style="color:darkgray">**DevOps를 위해서는 기본적으로 보안 관련 지식이 필요함**</span>

* QA 자동화 도구
: 빠른 피드백 제공으로 릴리즈 주기 단축
    * Selenium
        * WebDriver : 브라우저 제어
        * Selenium Grid : 병렬 테스트 가능
        * Selenium IDE : 테스트 기록 및 재생

    * JUnit : Java기반의 단위테스트 도구
    * TestNG : JUnit의 확장 버전, 병렬 실행, 테스트 그룹화, 데이터 기반 테스트 지원

    > <span style="color:darkgray">**웹훅 : http에서 호스트를 열어둠, 이후 특정 이벤트가 생기면 때 실시간으로 알림을 받을 수 있는 기능**</span>